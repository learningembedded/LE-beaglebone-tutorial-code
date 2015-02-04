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

 import Adafruit_BBIO.PWM as PWM 	# import PWM module
 import time						          # import time
 PWM.start("P8_14", 0)            #begin pwm with channel and duty cycle 
 duty_c=raw_input(“Enter Brightness (0 to 100:”))# input data
 PWM.set_duty_cycle("P8_14", float(duty_c)) 	   # set duty cycle
 time.sleep(1) 									                 # sleep for 1 sec
 PWM.stop("P8_14") 								               # stop pwm
 PWM.cleanup() 									                 # cleanup pwm
