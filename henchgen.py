# henchgen.py
# Henchman generator for the Adventurer Conqueror King System (ACKS).
# v1.0, March 29th, 2018.
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import os
import platform
import stellagama
import henchgenlib

#set functions

class character():
	"""
	character object
	"""
	
	def __init__ (self, level): #input character level
		self.level=level
		self.strength=stellagama.dice(3,6) #ability generation
		self.dexterity=stellagama.dice(3,6)
		self.constitution=stellagama.dice(3,6)
		self.intelligence=stellagama.dice(3,6)
		self.wisdom=stellagama.dice(3,6)
		self.charisma=stellagama.dice(3,6)
		self.strmod=henchgenlib.attribute_modifier(self.strength) #ability modifier calculation
		self.dexmod=henchgenlib.attribute_modifier(self.dexterity)
		self.conmod=henchgenlib.attribute_modifier(self.constitution)
		self.intmod=henchgenlib.attribute_modifier(self.intelligence)
		self.wismod=henchgenlib.attribute_modifier(self.wisdom)
		self.chamod=henchgenlib.attribute_modifier(self.charisma)
		self.attribute_list=[self.strength,self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma] #turning abilities into a list
		self.gold=10*stellagama.dice(3,6) #generate starting gold
		self.sex=henchgenlib.sex_gen() #generate sex
		self.race=henchgenlib.race_gen(self.constitution) #generate race
		self.name=henchgenlib.name_gen(self.sex) #generate name
		self.cclass=henchgenlib.charclass(self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma, self.sex, self.race, self.level) #choose character class
		self.hp=henchgenlib.hp_gen(self.cclass, self.conmod, self.level) #generate hit points
		self.proficiencies=henchgenlib.profgen(self.intmod, self.level, self.cclass) #generate proficiencies
		self.weapon=henchgenlib.weapon_gen(self.cclass) #generate weapon
		self.armor=henchgenlib.armor_gen(self.cclass) #generate armor
		self.trinket=stellagama.random_line("trinkets.txt") #generates trinket
		self.quirk=stellagama.random_line("quirks.txt") #generates quirk
			
		
def test():
	"""
	testing the object and basic functions/methods
	"""
	character1=character(3)
	#i=0
	#for i in range(0, len(character1.attribute_list)):
	#	character1.attribute_list[i]=str(character1.attribute_list[i])	
	#attribute_string=", ".join(character1.attribute_list) #old ability stringer code
	#print (attribute_string)
	print ("%s, level %s %s %s %s, %s hit points" %(character1.name, character1.level, character1.sex, character1.race, character1.cclass, character1.hp))
	print ("STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %(character1.strength, character1.dexterity, character1.constitution, character1.intelligence, character1.wisdom, character1.charisma))
	proflist=", ".join(character1.proficiencies)
	print ("Proficiencies: %s" %(proflist))
	print (character1.quirk)
	print ("%s, %s, %s" %(character1.weapon, character1.armor, character1.trinket))

	"""	
def main():
	"""
	#old main program
	"""
	try:
		charsave=stellagama.savefile()
		file_name=charsave+".txt"
		outp = open(file_name,"w")
		for i in range (1,6):
			outp.write("Character "+str(i)+'\r\n')
			outp.write("========"+'\r\n')
			outp.write("Strength: "+str(stellagama.dice(3,6))+'\r\n')
			outp.write("Dexterity: "+str(stellagama.dice(3,6))+'\r\n')
			outp.write("Constitution: "+str(stellagama.dice(3,6))+'\r\n')
			outp.write("Intelligence: "+str(stellagama.dice(3,6))+'\r\n')
			outp.write("Wisdom: "+str(stellagama.dice(3,6))+'\r\n')
			outp.write("Charisma: "+str(stellagama.dice(3,6))+'\r\n')
			outp.write("Gold: "+str(10*stellagama.dice(3,6))+'\r\n')
			outp.write(""+'\r\n')
			i=+1
	finally: #added to make sure the file is always closed no matter what
		outp.close() #close file
"""

def chargen (level0number, level0die, level1number, level1die, level2number, level2die, level3number, level3die, level4number, level4die): #input dice numbers and types for all four potential character levels
	"""
	generates NPCs in numbers based on the dice numbers and types received
	"""
	filename=stellagama.savefile("txt")
	with open (filename, "w") as output:
		for i in range (0, stellagama.dice(level0number, level0die)):
			character1=character(0)
			output.write ("%s, level %s %s %s %s, %s hit points" %(character1.name, character1.level, character1.sex, character1.race, character1.cclass, character1.hp)+'\r\n')
			output.write ("STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %(character1.strength, character1.dexterity, character1.constitution, character1.intelligence, character1.wisdom, character1.charisma)+'\r\n')
			proflist=", ".join(character1.proficiencies)
			output.write ("Proficiencies: %s" %(proflist)+'\r\n')
			output.write (character1.quirk+'\r\n')
			output.write ("%s, %s, %s" %(character1.weapon, character1.armor, character1.trinket)+'\r\n')
			output.write('\r\n')
		for i in range (0, stellagama.dice(level1number, level1die)):
			character1=character(1)
			output.write ("%s, level %s %s %s %s, %s hit points" %(character1.name, character1.level, character1.sex, character1.race, character1.cclass, character1.hp)+'\r\n')
			output.write ("STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %(character1.strength, character1.dexterity, character1.constitution, character1.intelligence, character1.wisdom, character1.charisma)+'\r\n')
			proflist=", ".join(character1.proficiencies)
			output.write ("Proficiencies: %s" %(proflist)+'\r\n')
			output.write (character1.quirk+'\r\n')
			output.write ("%s, %s, %s" %(character1.weapon, character1.armor, character1.trinket)+'\r\n')
			output.write('\r\n')
		for i in range (0, stellagama.dice(level2number, level2die)):
			character1=character(2)
			output.write ("%s, level %s %s %s %s, %s hit points" %(character1.name, character1.level, character1.sex, character1.race, character1.cclass, character1.hp)+'\r\n')
			output.write ("STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %(character1.strength, character1.dexterity, character1.constitution, character1.intelligence, character1.wisdom, character1.charisma)+'\r\n')
			proflist=", ".join(character1.proficiencies)
			output.write ("Proficiencies: %s" %(proflist)+'\r\n')
			output.write (character1.quirk+'\r\n')
			output.write ("%s, %s, %s" %(character1.weapon, character1.armor, character1.trinket)+'\r\n')
			output.write('\r\n')
		for i in range (0, stellagama.dice(level3number, level3die)):
			character1=character(3)
			output.write ("%s, level %s %s %s %s, %s hit points" %(character1.name, character1.level, character1.sex, character1.race, character1.cclass, character1.hp)+'\r\n')
			output.write ("STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %(character1.strength, character1.dexterity, character1.constitution, character1.intelligence, character1.wisdom, character1.charisma)+'\r\n')
			proflist=", ".join(character1.proficiencies)
			output.write ("Proficiencies: %s" %(proflist)+'\r\n')
			output.write (character1.quirk+'\r\n')
			output.write ("%s, %s, %s" %(character1.weapon, character1.armor, character1.trinket)+'\r\n')
			output.write('\r\n')
		for i in range (0, stellagama.dice(level4number, level4die)):
			character1=character(4)
			output.write ("%s, level %s %s %s %s, %s hit points" %(character1.name, character1.level, character1.sex, character1.race, character1.cclass, character1.hp)+'\r\n')
			output.write ("STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %(character1.strength, character1.dexterity, character1.constitution, character1.intelligence, character1.wisdom, character1.charisma)+'\r\n')
			proflist=", ".join(character1.proficiencies)
			output.write ("Proficiencies: %s" %(proflist)+'\r\n')
			output.write (character1.quirk+'\r\n')
			output.write ("%s, %s, %s" %(character1.weapon, character1.armor, character1.trinket)+'\r\n')
			output.write('\r\n')

def market_gen (market): #input ACKS market class
	"""
	Calls chargen() according to market type
	"""
	if market=="VI":
		chargen (1, 2, 1, 1, 1, 1, 0, 0, 0, 0)
	elif market=="V":
		chargen (1, 6, 1, 1, 1, 1, 1, 1, 0, 0)
	elif market=="IV":
		chargen (3, 4, 1, 2, 1, 1, 1, 1, 0, 0)
	elif market=="III":
		chargen (4, 8, 1, 4, 1, 3, 1, 1, 1, 1)
	elif market=="II":
		chargen (5, 20, 2, 6, 2, 4, 1, 3, 1, 2)
	elif market=="I":
		chargen (4, 100, 5, 10, 3, 10, 1, 10, 1, 6)
	else:
		print ("Unknown market type")

	
#Program Body
input_loop=True
while input_loop==True:
	print("ACKS Henchman Generator v1.0 by Omer Golan-Joel")
	market = input ("Please enter market class: I, II, III, IV, V, VI \n")
	if market in ["I", "II", "III", "IV", "V", "VI"]:
		input_loop=False
	else:
		print ("Unknown market type")
market_gen (str(market))