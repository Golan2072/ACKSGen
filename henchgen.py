# henchgen.py
# Henchman generator for the Adventurer Conqueror King System (ACKS).
# v0.2, February 9th, 2018.
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import os
import platform
import henchgenlib

#set functions

def dice(n,sides): #inputs number of dice, sides per die
	"""
	die-rolling function
	"""
	die=0
	roll=0
	while die<n:
		roll=roll+random.randint(1,sides)
		die+=1
	return roll #outputs die roll result

def yn():
	"""
	simple yes or no prompt filtering invalid results
	"""
	query = 1
	while query == 1:
		answer = str(input("Y/N: "))
		answer=answer.lower()
		if answer == "y":
			return "y"
			query = 0
		if answer == "n":
			return "n" #outputs "y" or "n"
			query = 0
		else:
			print ("Invalid Answer")

def current_dir():
	"""
	lists the current directory's contents on Windows or Linux
	"""
	if platform.system() == "Windows":
		directory=os.listdir(".\\")
	else:
		directory = os.getcwd()
	return directory
			
def check_file_exists(check_file):
	if check_file in os.listdir():
		file_exists = True
	else:
		file_exists = False
	return file_exists
 
def savefile():
	"""
	file-saving function
	"""
	filename=str(input("Please enter file name to generate: "))
	filecheck=filename+".sec"
	save = 1
	#directory=current_dir() #check if file already exists
	#filenumber=len(directory)
	#for i in range (0, filenumber):
	#  print(directory[i])
	#  #directory[i]=str(directory[i].lower())
	#  directory = "fred"
	#filecheck=filecheck.lower()
	if check_file_exists(filecheck):
		print(" ")
		print("File already exists. Overwrite?")
		overwrite=yn()
		if overwrite == "y":
			save=0
		if overwrite == "n":
			filename=input("Please enter new file name to generate: ")
	return filename #outpus File name

#def	chargen(serial): #inputs the character
#	"""
#	rolls characters and saves them to a text file - OLD
#	"""
#	outp.write("Character ", serial)
#	outp.write("===========")
#	outp.write("Strength:", dice(3,6))
#	outp.write("Dexterity:", dice(3,6))
#	outp.write("Constitution:", dice(3,6))
#	outp.write("Intelligence:", dice(3,6))
#	outp.write("Wisdom:", dice(3,6))
#	outp.write("Charisma:", dice(3,6))
#	outp.write("Gold:", 10*dice(3,6))
#	outp.write("")
#	return()

class character():
	"""
	character object
	"""
	
	def __init__ (self, level): #input character level
		self.level=level
		self.strength=dice(3,6) #ability generation
		self.dexterity=dice(3,6)
		self.constitution=dice(3,6)
		self.intelligence=dice(3,6)
		self.wisdom=dice(3,6)
		self.charisma=dice(3,6)
		self.strmod=henchgenlib.attribute_modifier(self.strength) #ability modifier calculation
		self.dexmod=henchgenlib.attribute_modifier(self.dexterity)
		self.conmod=henchgenlib.attribute_modifier(self.constitution)
		self.intmod=henchgenlib.attribute_modifier(self.intelligence)
		self.wismod=henchgenlib.attribute_modifier(self.wisdom)
		self.chamod=henchgenlib.attribute_modifier(self.charisma)
		self.attribute_list=[self.strength,self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma] #turning abilities into a list
		self.gold=10*dice(3,6) #generate starting gold
		self.sex=henchgenlib.sex_gen() #generate sex
		self.race=henchgenlib.race_gen(self.constitution) #generate race
		self.name=henchgenlib.name_gen(self.sex) #generate name
		self.cclass=henchgenlib.charclass(self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma, self.sex, self.race, self.level) #choose character class
		self.hp=henchgenlib.hp_gen(self.cclass, self.conmod, self.level) #generate hit points
		self.proficiencies=henchgenlib.profgen(self.intmod, self.level, self.cclass) #generate proficiencies
		self.weapon=henchgenlib.weapon_gen(self.cclass) #generate weapon
			
		
def test():
	"""
	testing the object and basic functions/methods
	"""
	character1=character(1)
	#i=0
	#for i in range(0, len(character1.attribute_list)):
	#	character1.attribute_list[i]=str(character1.attribute_list[i])	
	#attribute_string=", ".join(character1.attribute_list) #old ability stringer code
	#print (attribute_string)
	print ("%s, level %s %s %s %s, %s hit points" %(character1.name, character1.level, character1.sex, character1.race, character1.cclass, character1.hp))
	print ("STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %(character1.strength, character1.dexterity, character1.constitution, character1.intelligence, character1.wisdom, character1.charisma))
	proflist=", ".join(character1.proficiencies)
	print ("Proficiencies: %s" %(proflist))
	print (character1.weapon)

	"""	
def main():
	"""
	#old main program
	"""
	try:
		charsave=savefile()
		file_name=charsave+".txt"
		outp = open(file_name,"w")
		for i in range (1,6):
			outp.write("Character "+str(i)+'\r\n')
			outp.write("========"+'\r\n')
			outp.write("Strength: "+str(dice(3,6))+'\r\n')
			outp.write("Dexterity: "+str(dice(3,6))+'\r\n')
			outp.write("Constitution: "+str(dice(3,6))+'\r\n')
			outp.write("Intelligence: "+str(dice(3,6))+'\r\n')
			outp.write("Wisdom: "+str(dice(3,6))+'\r\n')
			outp.write("Charisma: "+str(dice(3,6))+'\r\n')
			outp.write("Gold: "+str(10*dice(3,6))+'\r\n')
			outp.write(""+'\r\n')
			i=+1
	finally: #added to make sure the file is always closed no matter what
		outp.close() #close file
"""

#Program Body
test()
