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

def individual_chargen(levelNumber, levelDie, characterLevel):
	charstring = ""
	for i in range (0, stellagama.dice(levelNumber, levelDie)):
		character1=character(characterLevel)
		charstring += "%s, level %s %s %s %s, %s hit points" %(character1.name, character1.level, character1.sex, character1.race, character1.cclass, character1.hp)+'\r\n'
		charstring += "STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %(character1.strength, character1.dexterity, character1.constitution, character1.intelligence, character1.wisdom, character1.charisma)+'\r\n'
		proflist=", ".join(character1.proficiencies)
		charstring += "Proficiencies: %s" %(proflist)+'\r\n'
		charstring += character1.quirk+'\r\n'
		charstring += "%s, %s, %s" %(character1.weapon, character1.armor, character1.trinket)+'\r\n'
		charstring += '\r\n'
	return charstring

def chargen (level0number, level0die, level1number, level1die, level2number, level2die, level3number, level3die, level4number, level4die): #input dice numbers and types for all four potential character levels
	"""
	generates NPCs in numbers based on the dice numbers and types received
	"""
	charstring = ""

	charstring += individual_chargen(level0number, level0die, 0)
	charstring += individual_chargen(level1number, level1die, 1)
	charstring += individual_chargen(level2number, level2die, 2)
	charstring += individual_chargen(level3number, level3die, 3)
	charstring += individual_chargen(level4number, level4die, 4)
	return charstring

def market_gen (market:int, small=False): #input ACKS market class
	"""
	Calls chargen() according to market type
	"""
	if market==6:
		return chargen (1, 2, 1, 1, 1, 1, 0, 0, 0, 0)
	elif market==5:
		return chargen (1, 6, 1, 1, 1, 1, 1, 1, 0, 0)
	elif market==4:
		return chargen (3, 4, 1, 2, 1, 1, 1, 1, 0, 0)
	elif market==3:
		return chargen (4, 8, 1, 4, 1, 3, 1, 1, 1, 1)
	elif market==2:
		return chargen (5, 20, 2, 6, 2, 4, 1, 3, 1, 2)
	elif market==1:
		if small:
			return chargen (0, 0, 5, 10, 3, 10, 1, 10, 1, 6)
		else:
			return chargen (4, 100, 5, 10, 3, 10, 1, 10, 1, 6)
	else:
		return "Unknown market type"

