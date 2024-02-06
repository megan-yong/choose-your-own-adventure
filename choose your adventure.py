### Linguistic Computations Project - Ashleigh Hockey, Megan Yong

# Import
import sys, string, time, os, random 

global chosen_weapon

chosen_weapon = ""

# Typewriter effect for Write and Input
def typingWrite(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

def typingInput(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    value = input().strip()  
    return value  

# Clear output screen 
def clearScreen():
    os.system("cls")

# Reference for if error while option for restart
def General_Restart():
    General_Restart = typingInput("Oops! You died. Do you want to restart from the castle? \n").lower()

    if General_Restart in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
        start_adventure(playerName)  

    elif General_Restart in ["no", "n", "nah", "nope", "not really", "never"]:
        time.sleep(0.4)
        clearScreen()
        typingWrite("Game ended!")
        sys.exit()

    else:
        typingWrite("Error! Answer again.\n")
        General_Restart()
        
### Intro 

# Welcome
while True:
    ready = typingInput("Welcome!\nThis is a Choose Your Own Adventure Game by Ashleigh and Megan.\nAre you ready to play? ").lower()

    if ready in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay", "ready"]:
        playerName = typingInput("Great! What is your name? ").capitalize()
        typingWrite("Welcome, %s! Let the adventure begin!\n\n" % (playerName))
        time.sleep(0.4)    # Text delay
        break

    elif ready in ["no", "n", "nah", "nope", "not really", "never"]:
        time.sleep(0.4)
        clearScreen()
        typingWrite("Game ended!")
        sys.exit()

    else:
        typingWrite("Error! Answer again.\n")
        ready
        

# Adventure begins
def start_adventure(playerName):
    global chosen_weapon
    typingWrite("Hello Knight %s! The King has tasked you with a quest to find a treasure chest in this magical realm.\n" % (playerName))

    armoury = typingInput("You are now in the King's castle. Do you want to enter the armoury? ").lower()

    if armoury in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
        typingWrite("\nYou enter the castle's armoury. The room is filled with an array of weapons. ")

        weapon_choices = ["Sword", "Axe", "Bow", "Mace"]
        typingWrite("You see the following weapons: ")
        for weapon in weapon_choices:
            typingWrite("-%s " % (weapon))
        time.sleep(0.4)

        chosen_weapon = typingInput("\nWhich weapon will you choose? ").capitalize()

        if chosen_weapon in weapon_choices:
            typingWrite("You have chosen the %s. Good choice! Prepare for your adventure, brave %s!\n\n" %  (chosen_weapon, playerName))
            time.sleep(0.4)
            # Continues to Obstacle 1 function with the chosen weapon
            obstacle_1(playerName, chosen_weapon)

        else:
            typingWrite("Invalid choice. Try again.\n")
            start_adventure(playerName)  # Recursive call to restart the opening scene

    elif armoury in ["no", "n", "nah", "nope", "not really", "never"]:
        typingWrite("You must be great at martial arts! Prepare for your adventure, brave %s!\n\n" % (playerName))
        time.sleep(0.4)
        # Continues to Obstacle 1 function with no weapon
        obstacle_1(playerName, None)

    else:
        typingWrite("Error! Answer again.\n")
        start_adventure(playerName)

### Obstacle 1 - Directions
obstacle1 = {
        'N': 'As you wander North towards the sea, you admire the view. \nSuddenly, you slip and fall off the edge of the cliff.\n\n',
        'W': 'You trek West and further into the forest.\n\n',
        'E': 'You turn back towards the East, the way you came, and head back into the castle and give up.\n\n',
        'S': 'You follow the river South, to continue your quest.\n\n'
        }

def obstacle_1(playerName, chosen_weapon):

        user_choice = typingInput("Pick a direction (North/West/East/South): ").capitalize()
        time.sleep(0.4)
        typingWrite(f"You chose: {user_choice}\n")
        time.sleep(0.4)
    
        if user_choice in ["W", "West"]:
            direction = "W"
            typingWrite(obstacle1[direction])
            obstacle_2(playerName, chosen_weapon)

        elif user_choice in ["S", "South"]:
            direction = "S"
            typingWrite(obstacle1[direction])
            obstacle_3(playerName, chosen_weapon)

        elif user_choice in ["N", "North"]:
            direction = "N"
            typingWrite(obstacle1[direction])
            restart_1 = typingInput("Oops! You died. Do you want to restart from the castle? \n")

            if restart_1 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
                start_adventure(playerName)  

            elif restart_1 in ["no", "n", "nah", "nope", "not really", "never"]:
                time.sleep(0.4)
                clearScreen()
                typingWrite("Game ended!")
                sys.exit()

            else:
                typingWrite("Error! Answer again.\n")
                General_Restart()

        elif user_choice in ["E", "East"]:
            direction = "E"
            typingWrite(obstacle1[direction])
            restart_2 = typingInput("Are you sure you want to go back to the castle? \n")

            if restart_2 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
                start_adventure(playerName)  

            elif restart_2 in ["no", "n", "nah", "nope", "not really", "never"]:
                obstacle_1(playerName, chosen_weapon)

            else:
                typingWrite("Error! Answer again.\n")
                General_Restart()

        else:
            typingWrite("That isn't a direction. Please try again. ")
            obstacle_1(playerName, chosen_weapon)

### Obstacle 2 - Elves (Ending 1)
def obstacle_2(playerName, chosen_weapon):
    challenge_options = {
        "Option one" : "Say no thank you", 
        "Option two" : "Run away", 
        "Option three" : "Agree to the duel"
    }

    typingWrite("As you walk between the trees, you hear a whistle.\n")
    time.sleep(0.4)
    typingWrite("An arrow comes flying in your direction. You duck. The arrow hits a tree.\nSuddenly, three elves jump down from the trees. They challenge you to a duel.\n\nYou can either:\n")

    for option, description in challenge_options.items():
        typingWrite("%s, %s.\n" % (option, description))

    while True:
        chosen_option = typingInput("Which option do you pick? ").lower()

        if chosen_option in ["option one", "option 1", "one", "1"]:
            typingWrite("\nYou politely decline the duel. The elves start laughing and call you lazy. \nYou begin feeling woozy and feel your eyes shut. \n\n")
            time.sleep(0.4)
            typingWrite("You open your eyes to find yourself back in the castle...\n\n")
            start_adventure(playerName)

        elif chosen_option in ["option two", "option 2", "two", "2"]:
            typingWrite("\nYou decide to run away. The elves begin shouting and shoot a few more arrows. You manage to dodge them.\n\n")
            time.sleep(0.4)
            typingWrite("You suddenly get hit by a poison arrow! You meet your unfortunate end.\n\n")
            restart_3 = typingInput("Oops! You died. Do you want to restart from the castle? \n")

            if restart_3 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
                start_adventure(playerName) 

            elif restart_3 in ["no", "n", "nah", "nope", "not really", "never"]:
                time.sleep(0.4)
                clearScreen()
                typingWrite("Game ended!")
                sys.exit()

            else:
                typingWrite("Error! Answer again. ")
                General_Restart()

        elif chosen_option in ["option three", "option 3", "three", "3"]:
            if chosen_weapon == None:
                restart_4 = typingInput("You don't have a weapon! You have surrendered! Do you want to restart from the castle? \n")
        
                if restart_4 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
                    start_adventure(playerName)  

                elif restart_4 in ["no", "n", "nah", "nope", "not really", "never"]:
                    time.sleep(0.4)
                    clearScreen()
                    typingWrite("Game ended!")
                    sys.exit()

                else:
                    typingWrite("Error! Answer again. ")
                    General_Restart()

            else:
                typingWrite(f"\nYou agree to the challenge. You draw your {chosen_weapon}, and the battle begins.\n\n")
                time.sleep(0.4)
                typingWrite("The elves are skilled fighters, but you manage to hold your ground. \nWith each move, you overpower them, and they finally surrender.\n\nThe elves agree to take you to the treasure.\n")
                Ending_1(playerName, chosen_weapon)

        else:
            typingWrite("That is not an option. Try again. ")
            obstacle_2(playerName, chosen_weapon)


### Ending 1 - Elves 
def Ending_1(playerName, chosen_weapon):
    typingWrite("They walk with you through the forest until you arrive in front of a waterfall. \n\nIn a cove behind the waterfall, a chest of gold glitters back at you. \nYou collect the treasure triumphantly, and return victoriously to the castle!\n\n")
    time.sleep(0.4)
    typingWrite("Congrats! You found the treasure! You are brave and noble, Knight %s." % (playerName))
    time.sleep(0.4)
    clearScreen()
    typingWrite("Game ended! Ending 1 of 3 found.")
    sys.exit()

### Obstacle 3 - Trolls
def obstacle_3(playerName, chosen_weapon):
    typingWrite("You come to a bridge spanning over the river.\n")
    time.sleep(0.4)
    typingWrite("As you approach, you suddenly spot a massive troll blocking your path. The troll asks, 'Who dares to cross my bridge?' You steel yourself and respond.\n")
    typingWrite("The troll grins and declares, 'I'll let you cross, but only if you can guess the number I'm thinking of. It's between 1 and 3.'\n")

    # Generate a random number between 1 and 3 for the troll
    troll_number = random.randint(1, 3)

    while True:
        # Ask the player to guess the number
        guess = int(typingInput("Take a guess: "))

        if 1 <= guess <= 3:
            if guess == troll_number:
                typingWrite("The troll nods in approval. 'Correct! You may pass. Safe travels, adventurer.'\nWith the troll satisfied, you successfully cross the bridge. Your adventure continues...\n\n")
                time.sleep(0.4)
                obstacle_4(playerName, chosen_weapon)

            else:
                typingWrite("The troll grumbles, 'Wrong! Try again.'\n")

        else:
            typingWrite("The troll gets angry, 'Do you not know how to count?' ")
            ending_options = ["throws you off the bridge", "stomps on you"]
            chosen_ending = random.choice(ending_options)
            typingWrite("In a fit of rage, the troll %s. You meet your unfortunate end.\n" % (chosen_ending))
            restart_5 = typingInput("Oops! You died. Do you want to restart from the castle? \n")

            if restart_5 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
                start_adventure(playerName) 

            elif restart_5 in ["no", "n", "nah", "nope", "not really", "never"]:
                time.sleep(0.4)
                clearScreen()
                typingWrite("Game ended!")
                sys.exit()

            else:
                typingWrite("Error! Answer again. ")
                General_Restart()

### Obstacle 4 dictonary - Escaping Goblins  
actions4 = {
    'climb' : 'You quickly climb a tree!\nThe goblins gather around the bottom and begin to shake it! \nYou loose your grip and fall!\n\n',
    'hide' : 'You spot a cave and run into the darkness!\n\n',
    'fight' : 'You prepare for a fight!\n\n'
    }

### Ending 2 dictonary - Fighting Knight
Ending2 = {
    'yes' : 'You hold your weapon steady. They take a swing at you, but you easily dodge and sweep the legs. You have beaten them!\n\n',
    'no' : 'You instead turn on your heel and sprint away, towards a cave!\n\n'
    }

### Ending 2 - Fighting Knight
def Ending_2(playerName, chosen_weapon):
    if chosen_weapon == None:
        restart_6 = typingInput("You don't have a weapon! You have surrendered! Do you want to restart from the castle? \n")
        if restart_6 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
            start_adventure(playerName)  

        elif restart_6 in ["no", "n", "nah", "nope", "not really", "never"]:
            time.sleep(0.4)
            clearScreen()
            typingWrite("Game ended!")
            sys.exit()

        else:
            typingWrite("Error! Answer again. ")
            Ending_2(playerName, chosen_weapon)
                
    typingWrite(f"As you draw your {chosen_weapon}, something springs out the bushes!\n\n")
    time.sleep(0.4)
    typingWrite("It's another Knight! They are working with the Goblins!\n")
    time.sleep(0.4)
    user_choice = typingInput("They challenge you to a duel. You bargain for the treasure they are hiding. Are you ready to fight the other knight? ").lower()
    typingWrite(f"You chose: {user_choice}\n")

    if user_choice in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
        choices = "yes"
        typingWrite(Ending2[choices])
        typingWrite("The Knight slowly stands and then bows. \nYou smile, and follow them towards a beautiful waterfall. \n\nIn a cove behind the waterfall, a chest of gold glitters back at you. \nYou collect the treasure triumphantly, and return victoriously to the castle!\n\n")
        time.sleep(0.4)
        typingWrite("Congrats! You found the treasure! You are brave and noble, Knight %s." % (playerName))
        time.sleep(0.4)
        clearScreen()
        typingWrite("Game ended! Ending 2 of 3 found.")
        sys.exit()

    elif user_choice in ["no", "n", "nah", "nope", "not really", "never"]:
        choices = "no"
        typingWrite(Ending2[choices])
        obstacle_5(playerName, chosen_weapon)

    else:
        typingWrite("That isn't an option! Pick one of the options! ")
        Ending_2(playerName, chosen_weapon)

### Ending 3 - Fairy
def Ending_3(playerName, chosen_weapon):
    typingWrite("Suddenly a fairy appears!\n\n")
    time.sleep(0.4)
    typingWrite("In a flash of light, you are outside flying through the air! \nThe fairy tells you she has been watching you, and was impressed by your noble tactics.\n")
    time.sleep(0.4)
    typingWrite("You are lowered to the ground in front of a waterfall. \n\nIn a cove behind the waterfall, a chest of gold glitters back at you. \nYou collect the treasure triumphantly, and return victoriously to the castle!\n\n")
    time.sleep(0.4)
    typingWrite("Congrats! You found the treasure! You are brave and noble, Knight %s." % (playerName))
    time.sleep(0.4)
    clearScreen()
    typingWrite("Game ended! Ending 3 of 3 found.")
    sys.exit()

### Obstacle 4  - Goblins     
def obstacle_4(playerName, chosen_weapon):

    user_choice = typingInput("You are suddenly chased by Goblins! \nQuick! Pick your next action: (climb/hide/fight): ").lower()
    typingWrite(f"You chose: {user_choice}\n")

    if user_choice in actions4:
        typingWrite(actions4[user_choice])

        if user_choice == 'hide':
           obstacle_5(playerName, chosen_weapon)

        elif user_choice == 'fight':
            Ending_2(playerName, chosen_weapon)

        elif user_choice == 'climb':
            restart_7 = typingInput("You have died! Do you want to restart from the castle? \n")

            if restart_7 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
                start_adventure(playerName) 

            elif restart_7 in ["no", "n", "nah", "nope", "not really", "never"]:
                time.sleep(0.4)
                clearScreen()
                typingWrite("Game ended!")
                sys.exit()

            else:
                typingWrite("Error! Answer again. ")
                General_Restart()

    else:
        typingWrite("That isn't an option! Pick one of the 3 choices! ")
        obstacle_4(playerName, chosen_weapon)

### Obstacle 5 Dictonary - Escaping Bear
actions5 = {
    "run away" : "As you noisly run backwards towards the light, the shape gets closer... \nIt's a bear! \nIt quickly catches up to you... \n...\n...\n...\nand eats you!\n\n",
    "go forward" : "You stumble forward... \nA bear suddenly wakes and moves towards you! \nYou're too close! \n...\nIt lashes out and hits you, knocking you into a wall!\n\n",
    "back away" : "You slowly and quietly walk backwards, facing the shape. \nYou can see it's a bear, rolling in its sleep. \n...\n you suddenly kick a stone... and it wakes!\n\n"
    }

### Obstacle 5 - Bear
def obstacle_5(playerName, chosen_weapon):
    user_choice = typingInput("As your eyes adjust to the darkness, you spot a large shape moving... \nWhat do you do? (run away/go forward/back away): ").lower()
    typingWrite(f"You chose: {user_choice}\n")

    if user_choice in actions5:
        typingWrite(actions5[user_choice])

        if user_choice == 'back away':
            Ending_3(playerName, chosen_weapon)

        elif user_choice == 'run away':
            restart_8 = typingInput("You have died! Do you want to restart from the castle? \n")

            if restart_8 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
                start_adventure(playerName) 

            elif restart_8 in ["no", "n", "nah", "nope", "not really", "never"]:
                time.sleep(0.4)
                clearScreen()
                typingWrite("Game ended!")
                sys.exit()

            else:
                typingWrite("Error! Answer again. ")
                General_Restart()

        elif user_choice == 'go forward':
            restart_9 = typingInput("You have died! Do you want to restart from the castle? \n")

            if restart_9 in ["yes", "y", "yeah", "yea", "yup", "yeap", "sure", "okay"]:
                start_adventure(playerName)  

            elif restart_9 in ["no", "n", "nah", "nope", "not really", "never"]:
                time.sleep(0.4)
                clearScreen()
                typingWrite("Game ended!")
                sys.exit()
            
            else:
                typingWrite("Error! Answer again. ")
                General_Restart()

    else:
        typingWrite("That isn't an option! Pick one of the 3 choices! ")
        obstacle_5(playerName, chosen_weapon)


### Start the adventure
start_adventure(playerName)