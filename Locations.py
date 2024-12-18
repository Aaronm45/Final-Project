deaths= 0
import Characters
import Opposition
import Weapons

def turn(attacker, defender, who):
    if who == "player":
        print("Pick an option: enter '1' or '2' ")
        print("1: Attack")
        print("2: Do Nothing")
        decision = input()
    else:
        decision ="1"
    if decision == "1":
        defender["Hp"] -= attacker["ATT"]
        print(f"{attacker["name"]} hits \
              {defender["name"]} for {attacker["ATT"]} damage")
    if decision == "2":
        print("You have chosen to do nothing")
    else: 
        decision == "2"
def battle(player, enemy):
    print(f"A {player["name"]} approuches {enemy["name"]}, ready to fight")

    while True:
        if player["SPD"] > enemy["SPD"]:
            turn(player, enemy, "player")
            turn(enemy, player, "enemy")
        else:
            turn(enemy, player, "enemy")
            turn(player, enemy, "player")
        print(f"{player['name']} has {player['Hp']} Hp left")
        print(f"{enemy['name']} has {enemy['Hp']} Hp left")
        if (player["Hp"] <= 0):
            return "player dead"
        if (enemy["Hp"] <= 0):
            return "enemy dead"
############ need to reset hp for player############
def Trail1(world):
    print("CHECKPOINT 2")
    print("You are traveling down the road towards The Evil Kingdom")
    print("You have come across a vile of a black liquidy substance- you have two choices:")
    print("Option 1: Drink the black liquidy substance")
    print("Option 2: Just leave it and keep traveling")
    userInput = input()
    if userInput.strip() == "1":
        print("You feel sick...")
        print("it might be from the ...(you see the sky starting to spin)")
        print("you've died of poison")
        print("GAME OVER")
        print()
        print()
        print("RESTART CHECKPOINT 2")
        deaths =+1
    if userInput.strip() =="2":
        world["loc"] = "goblinenc"
        return
        
       
       
    
def goblinenc(world):
    print("CHECKPOINT 3")
    print("You are traveling down the trail and you hear a woman screaming")
    print("You run towards the screams,")
    print("you see a Goblin mugging a woman- you have two choices")
    print("Option 1: Fight the goblin and save her")
    print("Option 2: Keep walking and ignore it")
    userInput = input()
    if userInput.strip() == "1":
        world["loc"] = "fight1"
        return
    if userInput.strip() == "2":
        print("You continued down the trail...")
        print("her screams get louder.... you see a huge shadow over pass")
        print("it's too late...")
        print("You have been eaten by the dragon ")
        print("GAME OVER")
        print()
        print()
        print("RESTART CHECKPOINT 2")
        deaths =+1
    return

def fight1(world):
    print("You have decided to fight the Goblin")
    #combat sequence
    battle(world["player"],Opposition.enemy1 )
    print("You have won the fight...")
    print("you have two options")
    print("Option 1: Continue down the trail")
    print("Option 2: Loot the goblin, it may have something valuble...")
    userInput =input()  
    if userInput.strip() == "1":
        world["loc"] = "trail2"
        return
    if userInput.strip() == "2": 
        '''world("player"+"dagger")'''######## FIGURE OUT HOW TO ADD TO STATS2

        print("You have looted the goblin, you have attained a Dagger(+5HP)(+1STR)(+2ATT) and 5 Goldpieces")
        world["loc"] = "trail2"
        return
 #if userInput.strip() =="1":
def trail2(world):
    print(" You have defeated the Goblin and are continuing down the trail....")
    print("You have come to fork in the trail...")
    print("To your left there are some mysterious shadowy woods.")
    print("To your right you see a town just in the distance, It is not very busy, It's called Smallton. you have two options")
    print("Option 1: The Mysterious Shadowy Woods")
    print("Option 2: Smallton")
    userInput =input()
    if userInput.strip() == "1":
        world["loc"] = "THEWOODS"
        return
    if userInput.strip() == "2":
        world["loc"] = "Smallton"
        return

def THEWOODS(world):
    print("CHECKPOINT 4")
    print("You have continued into the mysterious shadowy woods.")
    print("You get a chill down your spine...")
    print("The wind is howling throught the pine trees and the leaves are swirling...")
    print("They are swirling around you...")
    print("The swirling stops you have been teleported and in front of you a very large stump with something sticking out of it.. ")
    print("You walked towards it, to take a closer look...It's glicening black...jagged edges...")
    print("The Lengendary Obsidian Sword. It was crafted when the world was new, it's an enchanted blade it grants the user (+50hp)(+20STR)(+20ATT)")
    print("You have two options...")
    print("Option 1: Pull The sword and wield it")
    print("Option 2: Leave the sword and leave continue through the woods")
    userInput =input()
    if userInput.strip() == "1": 
        '''world('player' + 'dagger' + 'ObsidianSword')'''######## FIGURE OUT HOW TO ADD TO STATS
        print("You have pulled the Obsidian Sword, (+50HP)(+20STR)(+20ATT) ")
        world["loc"] = "cyclopsen1"
        return
    if userInput.strip() == "2":
        world["loc"] = "cyclopsen2"
        return
def cyclopsen1(world):
    print("When you pulled the Obsidian Sword a cyclops has awoken... He must have been guarding it. ")
    print("You have two choices...")
    print("Option 1: Run")
    print("Option 2: Fight the cyclops with your new found power.")
    userInput = input()
    if userInput.strip() == "2":
        world["loc"] = "fight2"
        return
    if userInput.strip() == "1":
        print("You ran from the cyclops...")
        print("you're in the clear.... you hear tree hurdling toward you")
        print("it's too late...")
        print("You have been speared by a pine tree and died ")
        print("GAME OVER")
        print()
        print()
        print("RESTART CHECKPOINT 4")
        deaths =+1
        world["loc"] = "THEWOODS"
        return
def cyclopsen2(world):
    print("You left the sword and are continuing through the woods...")
    print("A Cyclops has caught your scent he is running toward you")
    print("You have two choices...")
    print("Option 1: Run")
    print("Option 2: Fight the Cyclops.")
    userInput = input()
    if userInput.strip() == "2":
        world["loc"] = "fight2"
        return
    if userInput.strip() == "1":
        print("You ran from the cyclops...")
        print("you're in the clear.... you hear tree hurdling toward you")
        print("it's too late...")
        print("You have been speared by a pine tree and died ")
        print("GAME OVER")
        print()
        print()
        print("RESTART CHECKPOINT 4")
        deaths =+1
    return
def fight2(world):
    print("You have decided to fight the Cyclops")
    #combat sequence
    battle(world["player"],Opposition.enemy2 )
    print("You have won the fight...")
    print("you have two options")
    print("Option 1: Continue out of the woods")
    print("Option 2: Loot the Cyclops, it may have something valuble...")
    userInput =input()  
    if userInput.strip() == "1":
        world["loc"] = "edgeofwoods"
        return
    if userInput.strip() == "2": 
        world("player"+"dagger")
        print("You have looted the Cyclops, you have attained 20 Goldpieces")
        world["loc"] = "edgeofwoods"
        return
def edgeofwoods(world):
    print("CHECKPOINT 5")
    print("You see The Evil Kingdom")

def Smallton(world):
    print("You've walked intothe barren town you've seen a couple of passers by ")

def Firstown(world):
    print("CHECKPOINT 1")
    print("Welcome to Firstown. A buzzing town in the north of the countryside. There are lot's of people in this city.")
    print("You feel a tug on your hand, a small child,")  
    print("'Hey warrior, are you going to save us from the Skeleton King who lives in The Evil Kingdom to the south of The Countryside?'")
    print("You respond of course I will, I will protect all the people of The Countryside!")
    print("The city cheers for it's new protector")

    print("You have two options in Firstown")
    print("Answer with 1 or 2")
    print("Option 1: Stay in Firstown and see what's going on,")
    print("Option 2: Start to travel the road towards The Evil Kingdom")

    userInput = input()
    if userInput.strip() == "1":
        print("You've decided to stay in town.")
        print("Unfortunately...")
        print("An awoken ancient Dragon has burned Firstown")
        print("You have Burnt to a crisp, and Died")
        print("GAME OVER")
        print()
        print()
        print("RESTART CHECKPOINT 1")
        deaths =+1    
        return
    if userInput.strip() == "2":
        world["loc"] = "Trail1"
        return
        
    

def main():
    world = {}
    Characters.Queststart(world)
    world["loc"] = "Firstown"
    print("Please enter your name for this adventure")
    userInput = input()
    world["playerName"] = userInput
    world["Character"]= userInput
    world["inv"] = []

    while True:
        if world["loc"] == "Firstown":
            Firstown(world)
            continue
        if world["loc"]== "Trail1":
            Trail1(world)
            continue 
        if world["loc"]== "goblinenc":
            goblinenc(world)
            continue 
        if world["loc"]== "fight1":
            fight1(world)
            continue 
        if world["loc"]== "trail2":
            trail2(world)
            continue 
        if world["loc"]== "THEWOODS":
            THEWOODS(world)
            continue 
        if world["loc"]== "Smallton":
            Smallton(world)
            continue 
        if world["loc"]== "cyclopsen1":
            cyclopsen1(world)
            continue 
        if world["loc"]== "cyclopsen2":
            cyclopsen2(world)
            continue 
        if world["loc"]== "fight2":
            fight2(world)
            continue 
        if world["loc"]== "edgeofwoods":
            edgeofwoods(world)
            continue 
        '''
        if world["loc"] == "graveyard":
            showGraveyard(world)'''
        break # Exit the while true, game is over

main()
    