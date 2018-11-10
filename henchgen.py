# henchgen.py
# Henchman generator for the Adventurer Conqueror King System (ACKS).
# v1.1, November 10th, 2018.
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import os
import platform
import stellagama
import henchgenlib
import henchgenchar

#Program Body
input_loop=True
while input_loop==True:
	print("ACKS Henchman Generator v1.1 by Omer Golan-Joel")
	market = input ("Please enter market class: 1 through 6 \n")
	if int(market) in range(1,7):
		input_loop=False
	else:
		print ("Unknown market type")
henchoutput = henchgenchar.market_gen (int(market))
output = open(stellagama.savefile("txt"),"w")
output.write(henchoutput)
output.close()