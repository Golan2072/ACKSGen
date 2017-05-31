# henchgenlib.py
# ACKS henchman and hireling generator data and rules library
# v1.0, May 29, 2017
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string

def random_choice(list): #input list
	"""
	randomly chooses an element from a list.
	"""
	element=list[random.randint(0,len(list)-1)]
	return element #output randomly-selected element

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

def	race_gen():	
	"""
	generates character race
	"""
	roll=dice(2,6)
	if roll <=7:
		race="Human"
	elif roll==8:
		race="Dwarf"
	elif roll > 9:
		race="Elf"
	else:
		race="Human"
	return race #output race
	
def	sex_gen(race): #input race string
	"""
	generates character's sex
	dwarves are more likely to be M in comparison to other races
	"""
	roll=dice(1,6)
	if race=="Human" or race=="Elf":
		if roll in [1, 2, 3]:
			sex="M"
		if roll in [4, 5, 6]:
			sex="F"
	elif race=="Dwarf":
		if roll in [1, 2, 3, 4, 5]:
			sex="M"
		if roll==6:
			sex="F"
	else:
		sex="M"
	return sex #output sex
	
def name_gen(sex, race): #input character sex and race strings
	"""
	randomly chooses a character name from a list
	"""
	name=""
	if sex=="M" and race=="Human":
		name=random_choice([\
		"Andrei",\
		"Alex",\
		"Omar",\
		"Caleb",\
		"Marcus",\
		"Adar",\
		"Bal",\
		"Maoz",\
		"Borbus",\
		"Zadok",\
		"Alan",\
		"Ivan",\
		"Arad",\
		"Oleg",\
		"Alva",\
		"Sergei",\
		"Baruch",\
		"Barak",\
		"Ake",\
		"Arvid",\
		"Asger",\
		"Asmund",\
		"Audun",\
		"Balder",\
		"Bard",\
		"Birger",\
		"Bjarke",\
		"Bjarni",\
		"Mikhail"])
	elif sex=="F" and race=="Human":
		name=random_choice([\
		"Anat",\
		"Alfhild",\
		"Asta",\
		"Astrid",\
		"Istrid",
		"Audhild",\
		"Bergjot",\
		"Aslaug",\
		"Aslog",\
		"Alvidla",\
		"Ase",\
		"Alva",
		"Hannah",\
		"Ariella"])
	elif sex=="M" and race=="Elf":
		name=random_choice([\
		"Oran",\
		"Malak",\
		"Kilon"])
	elif sex=="F" and race=="Elf":
		name=random_choice([\
		"Natiana",\
		"Enya",\
		"Naya"])
	elif sex=="M" and race=="Dwarf":
		name=random_choice([\
		"Norin",\
		"Barin",\
		"Korin"])
	elif sex=="F" and race=="Dwarf":
		name=random_choice([\
		"Gaelin",\
		"Olga",\
		"Miranna"])
	else:
		name=""
	return name #output random name

def	HP_gen(conmod): #input constitution modifier
	"""
	generates hit points, currently only supports level 0 "Normal Men"
	"""
	return dice (1,6) + conmod

def	armor_gen():
	"""
	generates character armor
	"""
	roll=dice(2, 6)
	if roll <= 6:
		armor="Clothes"
	elif roll == 7:
		armor="Hide/Fur"
	elif roll == 8:
		armor="Leather"
	elif roll in [9, 10]:
		armor="Scalemail"
	elif roll in [11, 12]:
		armor="Chainmail"
	else:
		armor="Clothes only (AC 0)"
	return armor #outpur armor type

def AC_gen(armor): #input armor type string	
	"""
	generates armor AC
	"""
	if armor=="Clothes":
		AC=0
	elif armor=="Hide/Fur":
		AC=1
	elif armor=="Leather":
		AC=2
	elif armor=="Scalemail":
		AC=3
	elif armor=="Chainmail":
		AC=4
	else:
		AC=0
	return AC #output armor class

def weapon_gen(race): #input race string
	"""
	generates weapons
	"""
	roll=dice(1, 20)
	if race=="Human":
		if roll < 3:
			weapon="Dagger"
		elif roll in [4, 5, 6, 7]:
			weapon="Spear"
		elif roll==8:
			weapon="Warhammer"
		elif roll in [9, 10]:
			weapon="Club"	
		elif roll==11:
			weapon="Mace"
		elif roll in [12, 13]:
			weapon="Shortsword"
		elif roll in [14,15]:
			weapon="Handaxe"
		elif roll in [16, 17]:
			weapon="Shortbow and Dagger"
		elif roll==18:
			weapon="Light Crossbow and Dagger"
		elif roll==19:
			weapon="Longsword"
		elif roll==20:
			weapon="Two-Handed Sword"
		else:
			weapon="Dagger"
	elif race=="Dwarf":
		if roll < 3:
			weapon="Dagger"
		elif roll in [4, 5, 6]:
			weapon="Club"
		elif roll ==7:
			weapon="Mace"
		elif roll in [8, 9]:
			weapon="Warhammer"
		elif roll in [10, 11]:
			weapon="Shortsword"
		elif roll in [12, 13, 14]:
			weapon="Handaxe"
		elif roll in [15, 16]:
			weapon="Battleaxe"
		elif roll in [17,18]:
			weapon="Great Axe"
		elif roll in [19, 20]:
			weapon="Light Crossbow and Dagger"
		else:
			weapon="Dagger"
	elif race=="Elf":
		if roll < 4:
			weapon="Dagger"
		elif roll in [5, 6]:
			weapon="Spear"
		elif roll in [7, 8, 9]:
			weapon="Shortwsord"
		elif roll in [10, 11]:
			weapon="Longsword"
		elif roll in [12, 13, 14, 15, 16, 17]:
			weapon="Shortbow and Dagger"
		elif roll in [18, 19, 20]:
			weapon="Longbow and Dagger"
		else:
			weapon="Dagger"
	else:
		weapon="Dagger"
	return weapon
	
#function test area


