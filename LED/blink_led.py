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

import Adafruit_BBIO.GPIO as GPIO  # import gpio module
 import time 					             # import time
 GPIO.setup("P8_14", GPIO.OUT) 		 # set pin as output
 while True: 						           # infinite loop
 GPIO.output("P8_14", GPIO.HIGH) 	 # set pin high or 1
 time.sleep(1) 					           # sleep for 1 sec
 GPIO.output("P8_14", GPIO.LOW) 	 # set pin low or 0
 time.sleep(1) 						         # sleep for 1 sec
