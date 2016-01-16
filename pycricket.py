#Initialise global variables
global t1_runs
global t2_runs
global t1_name
global t2_name
global t1_outs
global t2_outs
global overs
global ball
global innings
global bowl_type


# FUNCTIONS

def game(): #runs the functions together
	pass
#	while innings = 1; #first half of the game
#		while overs >= 0;
#
	

def bowl():
	global overs
	global ball
	global bowl_type
	bowl_type = str(input("Do you wish to bowl pace, spin or off-spin? [p/s/o]: "))
	if bowl_type = "p":
		speed = randint(90,131)
		print("Bowled at " + speed + "km/h.")
	if bowl_type = "s":
		speed = randint(70, 101)
		print("Bowled at " + speed + "km/h.")
	if bowl_type = "o":
		speed = randint(70, 101)
		print("Bowled at " + speed + "km/h")				 
	#Ball/over counting to go in batting function, so as to avoid missing hits of bowled balls due to bad number management
	

