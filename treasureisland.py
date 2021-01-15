print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
door = input("You're at a Crossroad! Where'd ya wanna go? Left or Right?: ")
l = 'left'
ri = 'right'
s = 'swim'
w = 'wait'
r = 'red'
b = 'blue'
y = 'yellow'
if door.lower() == ri:
    print("Fell into a hole Game Oveaaar")
elif door.lower() == l:
    sec = input("You've arrived at a lake! Wait for a boat or swim? wanna Swim or wait?: ")
    if sec.lower() == s:
        print("Attacked by Crocodile, Game Ovaaaaaaerrrr")
    elif sec.lower() == w:
        tri = input("Boat got to an island with 3 doors!  What door u pick? Red, Blue or Yellow?:\n")
        if tri.lower() == y:
            print("You Win the Treasure, ohhoo Bade log")
        elif tri.lower() == b:
            print("Eaten by the Beasts Game Over")
        elif tri.lower() == r:
            print("Burned by Fire, Game Oveeear")
else:
    print("Attacked by Gost, Game Oveeaaar")



