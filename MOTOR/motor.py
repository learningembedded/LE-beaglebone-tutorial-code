#!/usr/bin/python
# Author: LearningEmbedded.com
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this code and associated documentation files , to use, copy, modify, merge,
# publish, distribute when you agree to the following conditions:
# Attribution — You must give appropriate credit, provide a link to the license, 
#               and indicate if changes were made. You may do so in any reasonable
#               manner, but not in any way that suggests the licensor endorses you 
#               or your use.
# No additional restrictions — You may not apply legal terms or technological 
#                              measures that legally restrict others from doing
#                              anything the license permits.

# http://learningembedded.com/

import Adafruit_BBIO.GPIO as GPIO 	# import GPIO module
import Adafruit_BBIO.PWM as PWM  	  # import PWM module
import time 						            # import time
enable_pin = 'P8_18' 				        # initialize variable
in1_pin = 'P8_12' 					        # initialize variable
in2_pin = 'P8_14' 					        # initialize variable
GPIO.setup(enable_pin, GPIO.OUT) 	# define pin as output
GPIO.setup(in1_pin, GPIO.OUT) 		# define pin as output
GPIO.setup(in2_pin, GPIO.OUT) 		# define pin as output
PWM.start(enable_pin,50,500,0) 	  # begin PWM with PWM.start(channel, duty, freq, polarity)
def clockwise(): 					        # define function for clockwise
  GPIO.output(in1_pin, GPIO.HIGH) # set pin as high
	GPIO.output(in2_pin, GPIO.LOW) 	# set pin as low
def counter_clockwise(): 			    # define function for anticlockwise
	GPIO.output(in1_pin, GPIO.LOW) 	# set pin as low
	GPIO.output(in2_pin, GPIO.HIGH) # set pin as high
while True:
	cmd = raw_input("Command, f/r 0..9, E.g. f5 :") # input command
	direction = cmd[0] 							               	# check the direction
	if direction == "f":
		clockwise()
	else:
		counter_clockwise()
speed = int(cmd[1]) * 10 							    # check the speed
PWM.set_duty_cycle("P8_18", speed) 				# change duty cycle
