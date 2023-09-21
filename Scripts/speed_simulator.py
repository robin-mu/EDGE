import sys
import pandas as pd
import plotly.express as px

GRAVITY = 2457 # 0x999
START_SPEED = 4505 # 0x1199
MINICUBE_SPEED = 16384
OTHERCUBE_ACCELERATION = 26
START_ANGLE = 4096
SPEED_LIMIT = 8192
ANGLE_SPEED_LIMIT = 61440 # 0xF000, found in game's code
ANGLE_THRESHOLD_GRAVITY = 57344 # 0xE000
ANGLE_THRESHOLD_RESET = 126976 # 0x1F000, guessed through experimenting

columns = 'Tick Steps Accel Speed ASpeed  Angle'

def log(msg, per_tick=False, verbose=False):
	if per_tick or verbose:
		print(msg)

def simulate(ticks, steps_since_last_prism, const_speed=None, climbing=False, minicube=False, othercube=False, output_per_tick=False, verbose_output=False):
	speed = START_SPEED if const_speed is None else const_speed
	angle_speed = 0
	angle = START_ANGLE
	climbed = False
	
	steps = 0
	last_step = 0
	
	tps_sequence = []
	angle1_sequence = []
	angle2_sequence = []
	max_angle1 = 0
	max_angle2 = 0
	
	angle_speed_values = []
	angle_values = []
	
	log(columns, per_tick=output_per_tick)
	
	for i in range(ticks):
		if const_speed is not None:
			speed = const_speed
		
		# acceleration
		acceleration = int(1023 - min(22, steps_since_last_prism) * 45.36) if not climbing else 0
		
		# speed
		if othercube:
			speed += OTHERCUBE_ACCELERATION
		elif minicube:
			speed = MINICUBE_SPEED
		else:
			speed = min(SPEED_LIMIT, speed + acceleration)
		log(f'{i:4d} {steps_since_last_prism:5d} {acceleration:5d} {speed:5d} {angle_speed:6d} {angle:6d}', verbose=verbose_output)
		
		if angle > ANGLE_THRESHOLD_GRAVITY and max_angle1 == 0:
			max_angle1 = angle - angle_speed
		
		if angle_speed == 0:
			angle = START_ANGLE
		
		# angle speed and gravity
		if angle >= ANGLE_THRESHOLD_GRAVITY and not climbing:
			angle_speed += GRAVITY
		else:
			angle_speed -= GRAVITY
		log(f'{i:4d} {steps_since_last_prism:5d} {acceleration:5d} {speed:5d} {angle_speed:6d} {angle:6d}', verbose=verbose_output)
		
		if angle_speed + speed < ANGLE_SPEED_LIMIT:  # maybe >=
			angle_speed += speed
			log(f'{i:4d} {steps_since_last_prism:5d} {acceleration:5d} {speed:5d} {angle_speed:6d} {angle:6d}', verbose=verbose_output)
		
		# angle
		angle += angle_speed
		
		if angle < 0:
			angle_speed = 0
			angle = 0
		log(f'{i:4d} {steps_since_last_prism:5d} {acceleration:5d} {speed:5d} {angle_speed:6d} {angle:6d}', verbose=verbose_output)
		
		# reset
		if angle > ANGLE_THRESHOLD_RESET:
			max_angle2 = angle - angle_speed
			
			if not climbing:
				if angle_speed > ANGLE_SPEED_LIMIT:
					angle = (angle // 4096 - 31) * 4096
				else:
					angle = 0
				log(f'{i:4d} {steps_since_last_prism:5d} {acceleration:5d} {speed:5d} {angle_speed:6d} {angle:6d}', verbose=verbose_output)
				
				angle_speed //= 10 if not climbed else 6
				climbed = False
				log(f'{i:4d} {steps_since_last_prism:5d} {acceleration:5d} {speed:5d} {angle_speed:6d} {angle:6d}', verbose=verbose_output)
			else:
				angle = START_ANGLE
				climbing = False
				climbed = True
			
			steps_since_last_prism += 1
			
			tps = i - last_step
			tps_sequence.append(tps)
			angle1_sequence.append(max_angle1)
			angle2_sequence.append(max_angle2)
			
			steps += 1
			log(f'Step {steps}: {i - last_step} ticks', per_tick=output_per_tick)
			log(columns, per_tick=output_per_tick)
			last_step = i
			
			max_angle1 = 0
			max_angle2 = 0
		
		log(f'{i:4d} {steps_since_last_prism:5d} {acceleration:5d} {speed:5d} {angle_speed:6d} {angle:6d}', per_tick=output_per_tick)
		
		if output_per_tick:
			angle_speed_values.append(angle_speed)
			angle_values.append(angle)

	if output_per_tick:
		return angle_speed_values, angle_values
	
	return tps_sequence, angle1_sequence, angle2_sequence

def periodic_sequence(seq):
	rev = list(reversed(seq))
	highscore = 0
	highsize = None
	for size in range(1, len(seq)):
		slices = [rev[i*size:i*size+size] for i in range(len(seq) // size)]
		score = 0
		for s in slices:
			if s == slices[0]:
				score += 1
			else:
				break
		if score > highscore:
			highscore = score
			highsize = size
	
	period = seq[-highsize:]
	rotations = [period[i:] + period[:i] for i in range(highsize)]
	
	for i in range(len(seq)):
		if seq[i:i+highsize] in rotations:
			return seq[:i], seq[i:i+highsize]
	
	return None

def speed_with_acceleration():
	for i in range(23):
		print(simulate(100, i)[0])

def speed():
	columns=['Speed (Without Acceleration)', 
			 'Angle Speed', 
			 'Ticks per Step (First)', 
			 'Ticks per Step (Periodic)', 
			 'Ticks per Step (Average)', 
			 'Steps per Second', 
			 'Angles Before Gravity (First)', 
			 'Angles Before Gravity (Periodic)', 
			 'Angles Before Gravity (Average)', 
			 'Angles Before Reset (First)', 
			 'Angles Before Reset (Periodic)', 
			 'Angles Before Reset (Average)']

	df = pd.DataFrame(columns=columns)
	for spd in range(2458, 8193):
		tpbs, a1, a2 = simulate(1000, 22, const_speed=spd-25)

		p = periodic_sequence(tpbs)
		a1 = periodic_sequence(a1)
		a2 = periodic_sequence(a2)	
		
		tps_first = ', '.join(str(s) for s in p[0])
		tps_periodic = ', '.join(str(s) for s in p[1])
		tps_avg = round(sum(p[1]) / len(p[1]), 2)
		sps = round(30 / tps_avg, 2)
		
		a1_first = ', '.join(str(s) for s in a1[0])
		a1_periodic = ', '.join(str(s) for s in a1[1])
		a1_avg = int(sum(a1[1]) / len(a1[1]))
		
		a2_first = ', '.join(str(s) for s in a2[0])
		a2_periodic = ', '.join(str(s) for s in a2[1])
		a2_avg = int(sum(a2[1]) / len(a2[1]))
		
		df = pd.concat([df, pd.DataFrame(dict(zip(columns, [[spd], [spd - 2457], [tps_first], [tps_periodic], [tps_avg], [sps], [a1_first], [a1_periodic], [a1_avg], [a2_first], [a2_periodic], [a2_avg]])))])
		print(f"{spd:4d} {spd-2457:4d} {tps_first:12s} {tps_periodic:20s} {tps_avg:5.2f} {sps:5.2f} {a1_first:20s} {a1_periodic:35s} {a1_avg:5d} {a2_first:25s} {a2_periodic:40s} {a2_avg:6d}")

	df.set_index('Speed (Without Acceleration)').to_csv('speed.csv')

def speed_condensed():
	columns = ['Speed (Without Acceleration)', 'Angle Speed', 'Ticks per Step', 'Steps per Second']
	df = pd.DataFrame(columns=columns)
	interval_start = 2458
	tps_avg = 26
	for spd in range(2458, 8193):
		tpss, _, _ = simulate(1000, 22, const_speed=spd-25)
		
		p = periodic_sequence(tpss)
		
		old_tps_avg = tps_avg
		tps_avg = round(sum(p[1]) / len(p[1]), 2)
		
		if old_tps_avg != tps_avg or spd == 8192:
			sps = round(30 / old_tps_avg, 2)
			if interval_start == spd - 1:
				df = pd.concat([df, pd.DataFrame(dict(zip(columns, [[interval_start], [interval_start - 2457], [old_tps_avg], [sps]])))])
			else:
				df = pd.concat([df, pd.DataFrame(dict(zip(columns, [[f'{interval_start}-{spd - 1}'], [f'{interval_start - 2457}-{spd - 2457 - 1}'], [old_tps_avg], [sps]])))])
			print(f"{interval_start:4d}-{spd - 1:4d} {interval_start - 2457:4d}-{spd - 2457 - 1:4d} {old_tps_avg:5f} {sps:5f}")
			interval_start = spd

	df.set_index('Speed (Without Acceleration)').to_csv('speed_condensed.csv')

def time_angle_plot(speed):
	aspd_seq, angle_seq = simulate(1000, 22, const_speed=speed-25, output_per_tick=True)
	
	aspd = periodic_sequence(aspd_seq)
	angle = periodic_sequence(angle_seq)
	
	aspd_data = aspd[0] + 2 * aspd[1]
	angle_data = angle[0] + 2 * angle[1]
	
	df_aspd = pd.DataFrame(data={'time': list(range(1, len(aspd_data) + 1)), 'angle_speed': aspd_data})
	df_angle = pd.DataFrame(data={'time': list(range(1, len(angle_data) + 1)), 'angle': angle_data})
	
	px.scatter(df_angle, x='time', y='angle').show()

simulate(4500, 22, othercube=True, output_per_tick=True)