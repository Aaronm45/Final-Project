# This is gonna be the library for payer characters
# game/quest backstory
def Queststart(world):
    print("Welcome player, in this world there are monsters heros and a quest to complete...")
    print("In this world in the land of The Countryside you will choose a hero with their own distinguished stat differences.")
    print("Please choose your character, enter 1,2,3")
    print("Option 1 : The Brute , he's the largest and strongest with the most Hp, but he is slow")
    print("Stats: Hp= 30 STR= 25 ATT= 18 SPD= 6 ")
    print("Option 2 : The Knight , he is above average in all stats and is skilled in speed and strength")
    print("Stats: Hp= 20 STR= 18 ATT= 15 SPD= 15 ")
    print("Option 3 : The Cavalier , he is a specialist in speed and will always attack first, but lacks in strength")
    print("Stats: Hp= 18 STR= 12 ATT= 12 SPD= 25")
    userInput = input()
    if userInput.strip() == "1":
        world["player"] = char1
    if userInput.strip() == "2":
        world["player"] = char2
    if userInput.strip() == "3":
        world["player"] = char3
char1= {
    "name" : "The Brute",
    "Hp"  :  30,
    "STR" :  25,
    "ATT" :  18,
    "SPD" :  6,
}


char2={
     "name" : "The Knight",
    "Hp"  :  20,
    "STR" :  18,
    "ATT" :  15,
    "SPD" :  15,
}


char3={
     "name" : "The Cavalier",
    "Hp"  :  18,
    "STR" :  12,
    "ATT" :  12,
    "SPD" :  25,
}


    