#IMPORTS
from random import randint
from time import sleep

#INITIALISE GLOBAL VARIABLES
global t1_score
global t2_score
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
global overs_stored

t1_score = 0
t2_score = 0
t1_name = "Still"
t2_name = "Testing!"
t1_outs = 0
t2_outs = 0
overs_stored = int(input("How many overs do you wish to play? "))
overs = overs_stored
ball = 0
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
	
def setup(): #Hoping to further develop this to be much more complex, but for now is very simple
	global t1_name
	global t2_name
	global overs

	t1_name = str(input("What is the name of Team 1? "))
	t2_name = str(input("What is the name of Team 2? "))
	overs = int(input("How many overs do you wish to play? "))


def bowl():
	global overs
	global bowl_type
	global speed
	bowl_type = str(input("Do you wish to bowl pace, spin or off-spin? [p/s/o] "))
	if bowl_type == "p":
		speed = randint(90,131)
		print("Bowled at " + str(speed) + "km/h.")
	elif bowl_type == "s":
		speed = randint(70, 101)
		print("Bowled at " + str(speed) + "km/h.")
	elif bowl_type == "o":
		speed = randint(70, 101)
		print("Bowled at " + str(speed) + "km/h")				 
	#Ball/over counting to go in batting function, so as to avoid missing hits of bowled balls due to bad number management
	
def bat():
	global speed
	global bowl_type
	global cur_team
	global t1_outs
	global t2_outs
	global innings
	global ball	
	if bowl_type == "p" and speed < 100:
		hit_chance = rand(0,1)
		if hit_chance < 0.1:
			print("Bowled out!")
			out()
		if 0.1 < hit_chance < 0.2:
			pass		
	
	if ball < 6:
		ball += 1
	elif ball == 6 and overs > 0:
		overs -= 1
	elif overs == 0:
		if cur_team == 1 and innings = :
			print("Innings done! Final score for " + str(t1_name) + " is " + str(t1_out) + "/" + str(t1_score))
			print("Change sides!")
			
def print_score(): #Displays score according to team currently batting
	global cur_team
	global t1_outs
	global t2_outs
	global t1_score
	global t2_score
	if cur_team == 1:
		print("Current Score: " + str(t1_outs) + "/" + str(t1_score))	
	elif cur_team == 2:
		print("Current Score: " + str(t2_outs) + "/" + str(t2_score))
	
def out(): #Moves code for out checking to a separate function to keep batting function cleaner
	global t1_outs
	global t2_outs 
	global t1_score
	global t2_score
	if innings == 1:
		if cur_team == 1:
			t1_outs += 1
			if t1_outs == 9: #Check to see if all out
				print("All out for " + str(t1_score) + ", change sides!")
				cur_team = 2
			else:
				print_score()
		if cur_team == 2:
			t2_outs += 1 	
			if t2_outs == 9:
				print("All out for " + t2_score + ", change sides!")
				cur_team = 1
			else:
				print_score()
def suspense(): #Function to slow down pace of game, makes it easier to follow and adds, as it says, suspense
	print(". " , end='', flush=True)
	sleep(0.5)
	print(". ", end='', flush=True)
	sleep(0.5)
	print("." , flush=True)
	sleep(0.5)

def coin_flip(): #Coin toss to decide who bats/bowls first
	global t1_name
	global t2_name
	global cur_team
	flip = randint(0,2)
	if flip == 0:
		flip = "h"
	else:
		flip = "t"

	t1_call = str(input("Team 1 heads or tails? [h/t] "))
	suspense()
	if flip == t1_call:
		if flip == "h":
			flip_long = "Heads!"
		else:
			flip_long = "Tails!"
		print("",flush=True)
		sleep(1)
		print(flip_long)
		choice=str(input(t1_name + ", do you wish to bat or bowl? [ba/bo] " ))
		if choice == "bo":
			print( t1_name + " has chosen to bowl first. ")
			print( t2_name + ", ready your bats!")
			cur_team = 2
		elif choice == "ba":
			print( t1_name + " has chosen to bat first. ")
			print( t2_name + ", to your positions!")
	else:
		if flip == "h":
			flip_long = "Heads!"
		else:
			flip_long = "Tails!"
		print(flip_long)
		choice=str(input(t2_name + ", do you wish to bat or bowl? [ba/bo] " ))
		if choice == "bo":
			print( t2_name + " has chosen to bowl first. ")
			print( t1_name + ", ready your bats!")
			cur_team = 2
		elif choice == "ba":
			print( t2_name + " has chosen to bat first. ")
			print( t1_name + ", to your positions!")
 
		
# RUN FUNCTIONS
#coin_flip()
print_score()
