#IMPORTS
from random import randint

#INITIALISE GLOBAL VARIABLES
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
global speed
global cur_team

t1_runs = 0
t2_runs = 0
t1_name = str(input("What is the name of Team 1? "))
t2_name = str(input("What is the name of Team 2? "))
t1_outs = 0
t2_outs = 0
overs = int(input("How many overs do you wish to play? "))
ball = 6
innings = 1
bowl_type = 0
speed = 0
cur_team = 1
# FUNCTIONS

#def game(): #runs the functions together
#	pass
#	while innings = 1; #first half of the game
#		while overs >= 0;
#
	

def bowl():
	global overs
	global ball
	global bowl_type
	global speed
	bowl_type = str(input("Do you wish to bowl pace, spin or off-spin? [p/s/o] "))
	if bowl_type == "p":
		speed = randint(90,131)
		print("Bowled at " + str(speed) + "km/h.")
	if bowl_type == "s":
		speed = randint(70, 101)
		print("Bowled at " + str(speed) + "km/h.")
	if bowl_type == "o":
		speed = randint(70, 101)
		print("Bowled at " + str(speed) + "km/h")				 
	#Ball/over counting to go in batting function, so as to avoid missing hits of bowled balls due to bad number management
	
def bat():
	global speed
	global bowl_type
	if bowl_type == "p" and speed < 100:
		hit_chance = rand(0,1)
		if hit_chance < 0.1:
			print("Bowled out!")
			if 

def coin_flip():
	global t1_name
	global t2_name
	global cur_team
	flip = randint(0.2)
	t1_call = str(input("Team 1 heads or tails? [h/t] "))
	if flip == 1 and t1_call == "h":
		print("Heads!")
		choice=str(input(t1_name + ", do you wish to bat or bowl? [ba/bo] " ))
		if choice == "bo":
			print(t1_name + " has chosen to bowl first. " + t2_name ", ready your bats!")
 			cur_team = 2
	else:
                pass
                

# RUN FUNCTIONS
coinflip()
