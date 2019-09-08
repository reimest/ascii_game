import getch
import os
import time
import random
import forest
import shop


os.system('clear')


load = ["|",chr(47),"-",chr(92)]
for i in range(40):
	print("WASD - movement\nC - character\nI - inventory\n\n\nCreating table..."+load[i%4])
	time.sleep(0.05)
	os.system('clear')

player_xy = [2,2]
table = [
"_______________________________________________________________________________________________________________",
"|.............................................................................................................|",
"|................................#.#.#........................................................................|",
"|...................88..........[]____........................................................................|",
"|...................||........./ _   /\____...................................................................|",
"|##....,......88............../_/ \_//____/\.......&&.........................................................|",
"|####.........||...........&&.|_[.]_|||__|||..................................................................|",
"|######.......................................&&..............................................................|",
"|...###........,,.............................................................................................|",
"|....#####....................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"|.............................................................................................................|",
"_______________________________________________________________________________________________________________"
]

for _ in range(len(table)): 
	table[_] = list(table[_])


inventory = ["test1","test2"]
character = {"name":"Scarlet","att":5,"def":3,"hp":100,"hp_now":100, "lvl":1, "exp": 10, "exp_now":0,"gold":500}
obj = ["+","|",chr(47),chr(92), "-","_","[","]","#","8","&"]
character["name"] = input("\n\n\n\n\n\n\n\n\n\n\n                    Select name for your hero: ")
os.system('clear')
def show_city():
	for x_ in table:
		y_ = ''
		for y__ in x_:
			y_ = y_ + y__
		print(y_)
		
table[player_xy[1]][player_xy[0]] = "@" #x = 6, y = 5
show_city()


while True:
	input_char = getch.getch()
	os.system('clear')
	if input_char.upper() == "A":
		table[player_xy[1]][player_xy[0]] = "."
		player_xy[0] = player_xy[0] - 1
		if table[player_xy[1]][player_xy[0]] in obj:
			player_xy[0] = player_xy[0] + 1
			print("You can't move there!")
		table[player_xy[1]][player_xy[0]] = "@"
	if input_char.upper() == "D":
		table[player_xy[1]][player_xy[0]] = "."
		player_xy[0] = player_xy[0] + 1
		if table[player_xy[1]][player_xy[0]] in obj:
			player_xy[0] = player_xy[0] - 1
			print("You can't move there!")
		table[player_xy[1]][player_xy[0]] = "@"
	if input_char.upper() == "W":                        
		table[player_xy[1]][player_xy[0]] = "."		
		player_xy[1] = player_xy[1] - 1
		if table[player_xy[1]][player_xy[0]] in obj:
			player_xy[1] = player_xy[1] + 1
			print("You can't move there!")
		table[player_xy[1]][player_xy[0]] = "@"
	if input_char.upper() == "S":
		table[player_xy[1]][player_xy[0]] = "."
		player_xy[1] = player_xy[1] + 1
		if table[player_xy[1]][player_xy[0]] in obj:
			player_xy[1] = player_xy[1] - 1
			print("You can't move there!")
		table[player_xy[1]][player_xy[0]] = "@"
	if input_char.upper() == "I":
		print("----Invetory----")
		for item in inventory:
			print(item)
		getch.getch()
	if input_char.upper() == "C":
		print("----Character----")
		print("Name: " + str(character["name"]))
		print("Level: " + str(character["lvl"]) + "(" + str(character["exp_now"]) + "/" + str(character["exp"]) + ")")
		print("Gold: " + str(character["gold"]))
		print("Attack: " + str(character["att"]))
		print("Defense: " + str(character["def"]))
		print("Hit Points: " + str(character["hp_now"]) + "/" + str(character["hp"]))
		getch.getch()
	if player_xy == [33,6]:
		shop.join()
	if (player_xy[0] > 0 and player_xy[0] < 4) and player_xy[1] == 8:
		forest.join(1)
	show_city()
	