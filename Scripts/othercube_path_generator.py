import sys

GRAVITY = 2457 # 0x999
START_SPEED = 4505 # 0x1199
OTHERCUBE_ACCELERATION = 26
START_ANGLE = 4096
ANGLE_SPEED_LIMIT = 61440 # 0xF000, found in game's code
ANGLE_THRESHOLD_GRAVITY = 57344 # 0xE000
ANGLE_THRESHOLD_RESET = 126976 # 0x1F000, guessed through experimenting

def simulate(steps, climb=[]):
	speed = START_SPEED
	angle_speed = 0
	angle = START_ANGLE
	
	step = 0
	timer = 0
	climbing = timer in climb
	climbed = False
	
	while step < steps:		
		# speed
		speed += OTHERCUBE_ACCELERATION
		
		# failsafe 1
		if angle_speed == 0:
			angle = START_ANGLE
		
		# gravity and angle speed
		if angle >= ANGLE_THRESHOLD_GRAVITY and not climbing:
			angle_speed += GRAVITY
		else:
			angle_speed -= GRAVITY
		
		if angle_speed + speed < ANGLE_SPEED_LIMIT:  # failsafe 2
			angle_speed += speed

		# angle
		angle += angle_speed
		
		# failsafe 3
		if angle < 0:
			angle_speed = 0
			angle = 0
		
		# reset
		if angle > ANGLE_THRESHOLD_RESET:
			if not climbing:
				if angle_speed > ANGLE_SPEED_LIMIT:  # failsafe 4
					angle = (angle // 4096 - 31) * 4096
				else:
					angle = 0
				
				angle_speed //= 10 if not climbed else 6
				climbed = False
				
				step += 1
				
				# climbing
				if step in climb:
					climbing = True
			else:
				angle = START_ANGLE
				climbing = False
				climbed = True
			
		
		timer += 1
		#print(f'{speed:5d} {angle_speed:6d} {angle:6d}')
	
	return timer

directions = {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West'}
def generate_path(input):
	timer = 0
	for i in input:
		if i[0] in directions:
			split = i.split('/')
			steps = int(split[0][1:])
			climb = [int(i) - 1 for i in split[1].split(',')] if len(split) > 1 and split[1] else []
			
			duration = simulate(steps, climb)
			print(f'<{directions[i[0]]}Down TimeOffset="{timer}"/>')
			print(f'<{directions[i[0]]}Up TimeOffset="{timer + duration}"/>')
			
			timer += duration + (2 if steps - 1 not in climb else 4)
		elif i[0] == 'p':
			timer += int(i[1:])

generate_path(sys.argv[1:])