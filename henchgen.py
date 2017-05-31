# henchgenlib.py
# ACKS henchman and hireling generator data and rules library
# v0.1, May 31, 2017
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import os
import platform
import henchgenlib

for i in range (1, 21):
	race=henchgenlib.race_gen()
	sex=henchgenlib.sex_gen(race)
	HP=henchgenlib.HP_gen(0)
	armor=henchgenlib.armor_gen()
	weapon=henchgenlib.weapon_gen(race)
	armorclass=henchgenlib.AC_gen(armor)
	print ("%s\t\t%s %s\t\t%s %s\t%s" % (henchgenlib.name_gen(sex, race), sex, race, HP, armor, weapon))
input()