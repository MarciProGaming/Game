import random
import time
from goto_py import goto


def gameStart():
    # Welcome message
    print("Welcome to The Game.")
    time.sleep(1)

    # Character choose
    print('There are 4 characters from which you can chose one.\nI. Wizard\nII. Berserker\nIII. Archer\nIV. Assassin')
    global ch
    while True:
        try:
            ch = input('Please choose the character by writing their name.\n---> ')
            # Wizard
            if ch == "Wizard":
                print("You've chosen the character: Wizard")
                break
            # Berserker
            elif ch == "Berserker":
                print("You've chosen the character: Berserker")
                break
            # Archer
            elif ch == "Archer":
                print("You've chosen the character: Archer")
                break
            # Assassin
            elif ch == "Assassin":
                print("You've chosen the character: Assassin")
                break
        except:
            print('An error has occurred, please restart The Game!')
        continue


gameStart()

# Stats
dmg = 1
hp = 10
xp = 0
level = 0
stamina = 15
lastchance = 1

last_auto_time = time.time()

#Levels and skills
skillpts = 0
xpmin = 10
tries = 0
xpplus = 0
dmgplus = 0
hpmax = 10
stammax = 15
hpsteal = 0
hpsklpts = 0
stmnsklpts = 0
fstlrnsklpts = 0
lfstlsklpts = 0
dmgsklpts = 0
upgrskl = "none"

#Final boss fight
bosshp = 500
bossdmg = 20

# Enemy stats
enhp = random.randint(1, 3)
endmg = random.randint(0, 1)

def phaseOne():
    global chname
    global ch
    chname = input('First, you need to give a name to your character.\n--->')
    print('Now you can list your characters statistics or you can start The Game.')
    while True:
        try:
            pho = input('To list the statistics write <stats>, to start The Game write <start>\n--->')
            if pho == 'stats':
                print('Name: ' + chname)
                print('Character: ' + ch)
                print('HP: ' + str(hp))
                print('Damage: ' + str(dmg))
                print('XP: ' + str(xp))
                print()
                while True:
                    try:
                        chs = input('Write <start> to start The Game!\n--->')
                        if chs == 'start':
                            print('The Game has been started! Get ready for the adventure.\n\n')
                            time.sleep(0.2)
                            print('Write <help> to list the commands.')
                            break
                    except:
                        print('An error has occurred, please restart The Game!')
                break
            elif pho == 'start':
                print('The Game has been started! Get ready for the adventure.\n\n')
                time.sleep(0.2)
                break
        except:
            print('An error has occurred, please restart The Game!')
        continue



phaseOne()

answers = [' explores a twisty passage.', ' found a little underground pond.']
caveent = [' found a dark cave entrance. Do you want to go in? (yes or no)',
           ' found a little hole by the wall, leading to a cave. Do you want to find out what is inside? (yes or no)',
           ' found a big hole on the ground. Do you want to  jump in the hole? (yes or no)']
noans = [' decided not to go in.\n', ' went past the entrance and continued the walk.\n',
         ' thought it was not a good idea to go inside.\n', ' just simply did not care about the cave.\n']
rest = [' found nothing to rest on, so just stood by the wall and tried to fall asleep.',
        ' found a little rock, and rested for a half an hour.', ' found a big rock, and rested for a whole day.']
enattack = [' damaged the enemy, but it is still alive.', ' tried to kill the enemy, but only did a small damage.']
ensucattack = [' executed the enemy.', ' killed the enemy.', " cut off the enemy's head."]

#Wizard
wizardskills = []
#Berserker
berserkerskills = []
#Archer
archerskills = []
#Assassin
assassinskills = []

enemy = ['Goblin', 'Little Dragon', 'Golem', 'Zombie',]
miniboss = [enemy, ]
boss = [miniboss, ]
finalboss = []
commands = ['help', 'quit', 'attack', 'rest', 'explore', 'stats', 'level', 'auto', 'skills', 'endgame']
skills = ['Life steal', 'More Stamina (1-2)', 'More Health (1-2)', 'Increase Damage (1-5)', 'Fast Learner']
incombat = 0


# noinspection PyTypeChecker
def explore():
    time.sleep(1)
    time.sleep(0.1)
    global q
    global hp
    global incombat
    global xp
    global level
    global xpmin
    global stamina
    global dmg
    global tries
    global enhp
    global endmg
    global last_auto_time
    global skillpts
    global xpplus
    global dmgplus
    global hpmax
    global stammax
    global hpsteal
    global hpsklpts
    global stmnsklpts
    global fstlrnsklpts
    global lfstlsklpts
    global dmgsklpts
    global upgrskl
    global lastchance
    global wizardskills
    global berserkerskills
    global assassinskills
    global archerskills
    global bosshp
    global bossdmg

    while True:
        try:
            q = input(chname + random.choice(caveent) + "\n")
            if q == "Yes" or q == "yes":
                print(chname + ' slowly goes to the cave entrance and enters.')
                print('Write <help> to list the commands.')
                while True:
                    try:
                        global insc
                        insc = input('--->')

                        if insc == 'help':
                            print(f"\n {str(commands)}\n")

                        elif insc == 'skills':
                            if skillpts >= 1:
                                print("\n-----------------------------------------------------")
                                print(f"Remaining skill points: {str(skillpts)}\n")
                                print("1. Life steal: " + str(lfstlsklpts) + " points.")
                                print("2. More Stamina: " + str(stmnsklpts) + " points.")
                                print("3. More Health: " + str(hpsklpts) + " points.")
                                print("4. Increase Damage: " + str(dmgsklpts) + " points.")
                                print("5. Fast Learner: " + str(fstlrnsklpts) + " points.")
                                print("-----------------------------------------------------\n")
                                skillupgr = input("Type in the number of the skill you want to upgrade.\n--->")
                                if skillupgr == "1" or skillupgr == "1.":
                                    lfstlsklpts += 1
                                    hpsteal += random.randint(1,2)
                                    upgrskl = "Life Steal"
                                    skillpts -= 1
                                    print(f"You upgraded the skill [{str(upgrskl)}]. It is now on level {str(lfstlsklpts)}")

                                elif skillupgr == "2" or skillupgr == "2.":
                                    stmnsklpts += 1
                                    stammax += random.randint(1, 3)
                                    upgrskl = "More Stamina"
                                    skillpts -= 1
                                    print(f"You upgraded the skill [{str(upgrskl)}]. It is now on level {str(stmnsklpts)}")

                                elif skillupgr == "3" or skillupgr == "3.":
                                    hpsklpts += 1
                                    hpmax += random.randint(1,2)
                                    upgrskl = "More Health"
                                    skillpts -= 1
                                    print(f"You upgraded the skill [{str(upgrskl)}]. It is now on level {str(hpsklpts)}")

                                elif skillupgr == "4" or skillupgr == "4.":
                                    dmgsklpts += 1
                                    dmgplus += random.randint(1,3)
                                    upgrskl = "Increase Damage"
                                    skillpts -= 1
                                    print(f"You upgraded the skill [{str(upgrskl)}]. It is now on level {str(dmgsklpts)}")

                                elif skillupgr == "5" or skillupgr == "5.":
                                    fstlrnsklpts += 1
                                    xpplus += random.randint(0,4)
                                    upgrskl = "Fast Learner"
                                    skillpts -= 1
                                    print(f"You upgraded the skill [{str(upgrskl)}]. It is now on level {str(fstlrnsklpts)}")

                            else:
                                print("\n-----------------------------------------------------")
                                print("1. Life steal: " + str(lfstlsklpts) + " points.")
                                print("2. More Stamina: " + str(stmnsklpts) + " points.")
                                print("3. More Health: " + str(hpsklpts) + " points.")
                                print("4. Increase Damage: " + str(dmgsklpts) + " points.")
                                print("5. Fast Learner: " + str(fstlrnsklpts) + " points.")
                                print("\nYou don't have any skill points.")
                                print("-----------------------------------------------------\n")

                        elif insc == 'endgame':
                            if level >= "50":
                                print("Are you sure you want to fight the final boss?")
                                fnboss = input("Yes or No\n--->")
                                if fnboss == "yes" or fnboss == "Yes":
                                    incombat = 1
                                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                    print("\n-----------------------------------------------------")
                                    print(f"{str(chname)} found a door-looking stone in a corner while exploring.")
                                    time.sleep(3)
                                    print(f"{str(chname)} got close and tried to push the 'door'. ")
                                    time.sleep(3)
                                    print("It had a really strange noise, and when opened a little wind came out.")
                                    time.sleep(3)
                                    print("It was cold, but felt really nice.")
                                    time.sleep(3)
                                    print("Suddenly a beam of sunlight lighted up the place.")
                                    time.sleep(3)
                                    print("It was a room, but it felt like it was for giants. Everything was huge.")
                                    time.sleep(3)
                                    print(f"{str(chname)} started walking inside the room.")
                                    time.sleep(3)
                                    print(f"Suddenly out of nowhere a giant got behind {str(chname)} and started talking.")
                                    time.sleep(3)
                                    print("\nGIANT - Who are you?")
                                    time.sleep(3)
                                    print(f"{str(chname)} - My name is {str(chname)}.")
                                    time.sleep(3)
                                    print("GIANT - And what are you doing here?")
                                    time.sleep(3)
                                    print(f"{str(chname)} - I don't really know, i just came through a door and found this place.")
                                    time.sleep(3)
                                    print("GIANT - Well, i don't like seeing anyone here.")
                                    time.sleep(3)
                                    print("GIANT - So you have 5 seconds to explain what you want or i'll kill you.")
                                    time.sleep(3)
                                    print("1. Would you like to fight the giant?")
                                    print("2. Would you like to talk with him and try to be friendly?")
                                    chend = input("You have to do something, but what will you choose? 1. or 2.?\n--->")
                                    if chend == "1" or chend == "1.":
                                        dmg = 500
                                        print("You took out your sword and pointed it at the giant.")
                                        time.sleep(3)
                                        print(f"{str(chname)} - And what if i would like to stay here?")
                                        time.sleep(3)
                                        print("GIANT - Then sadly i have to end your life.")
                                        time.sleep(3)
                                        print("\n-----------------------------------------------------")
                                        print("Enemy type: The Final Boss")
                                        print(f"Boss health: {str(bosshp)}")
                                        print(f"Boss damage: {str(bossdmg)}")
                                        print("-----------------------------------------------------\n")
                                        #FINAL FIGHT
                                        while True:
                                            try:
                                                finalin = input("\n--->")
                                                if finalin == "attack":
                                                    hp -= bossdmg
                                                    stamina -= random.randint(1, 4)
                                                    bosshp -= dmg + dmgplus
                                                    print('You attacked the boss')
                                                    if bosshp <= 0:
                                                        print("\n-----------------------------------------------------")
                                                        print(f"{str(chname)} defeated the boss, who is now laying on the floor.")
                                                        time.sleep(3)
                                                        print("GIANT - Well, it seems like i've met my fate.")
                                                        time.sleep(3)
                                                        print(f"GIANT - But i would like to say something to you {str(chname)} before i go.")
                                                        time.sleep(3)
                                                        print("\nPrepare for your worst nightmares!\n")
                                                        time.sleep(3)
                                                        print("As the last words left the giants mouth, he started to slowly fade away.")
                                                        time.sleep(3)
                                                        print(f"{str(chname)} - Wait! WAIT! WHAT DO YOU MEAN BY THAT???")
                                                        time.sleep(3)
                                                        print(f"When {str(chname)} ended talking the giant fully disappeared.")
                                                        time.sleep(3)
                                                        print("-----------------------------------------------------\n")
                                                        print("\n\n\n\n\n\n-------------------------------")
                                                        print("          Game Credits")
                                                        print("-------------------------------\n")

                                                        print("**Game Development Team:**\n")

                                                        print("**Lead Developer:**")
                                                        print("Polyák Marcell\n")

                                                        print("**Game Designers:**")
                                                        print("Molnár Maxim")
                                                        print("Polyák Marcell\n")
                                                        print("Tóth Ádám")

                                                        print("**Programmers:**")
                                                        print("Molnár Maxim")
                                                        print("Polyák Marcell\n")

                                                        print("**Artists:**")
                                                        print("Tóth Ádám")
#                                                        print("[Artist 2 Name]\n")

#                                                        print("**Quality Assurance:**")
#                                                        print("[QA Tester 1 Name]")
#                                                        print("[QA Tester 2 Name]\n")

 #                                                       print("-------------------------------\n")

#                                                        print("**Special Thanks:**\n")

#                                                        print("[Special Thanks 1]")
#                                                        print("[Special Thanks 2]")
#                                                        print("[Special Thanks 3]\n")

#                                                        print("-------------------------------\n")

#                                                        print("**Music:**")
#                                                       print("[Composer Name]\n")

#                                                        print("**Sound Effects:**")
#                                                        print("[Sound Effects Artist Name]\n")

#                                                        print("-------------------------------\n")

#                                                       print("**Additional Contributors:**\n")

#                                                        print(
#                                                            "[List any other individuals or organizations that contributed to the game.]\n")

#                                                        print("-------------------------------\n")

#                                                        print("**Powered by:**")
#                                                        print("[Game Engine/Library Used, if applicable]\n")

#                                                        print("-------------------------------\n")

                                                        print("Thank you to our players and supporters for making this game possible!\n")
                                                        print("© 2023 Realms of Adventures. All Rights Reserved.")
                                                        break

                                                    elif bosshp > 0:
                                                        hp += hpsteal
                                                        if hp > hpmax:
                                                            hp = hpmax
                                                        finalbossdmg = bossdmg + hpsteal
                                                        print("\n-----------------------------------------------------")
                                                        print(f"Boss health: {str(bosshp)} (-{str(dmg + dmgplus)})")
                                                        print(f"Your health: {str(hp)}/{str(hpmax)} (-{str(finalbossdmg)})")
                                                        print(f"Your stamina: {str(stamina)}/{str(stammax)}")
                                                        print("-----------------------------------------------------\n")

                                                    if hp <= 0:
                                                        if lastchance == 1:
                                                            print(f"You need to rest NOW, or {str(chname)} will die!")
                                                            lastchance = 0
                                                            hp = 1
                                                        elif lastchance == 0:
                                                            print("You couldn't compete with the giants power and you died.")
                                                            break

                                                elif finalin == "rest":
                                                    print(chname + random.choice(rest) + "\n")
                                                    resthp = random.randint(5, 10)
                                                    reststam = random.randint(5, 10)
                                                    hp += resthp
                                                    stamina += reststam
                                                    lastchance = 1

                                                    if hp < hpmax:
                                                        print(f"+{str(resthp)} health")
                                                    else:
                                                        hp = hpmax
                                                        print(f"{str(chname)}'s health is full")

                                                    if stamina < stammax:
                                                        print(f"+{str(reststam)} stamina\n")
                                                    else:
                                                        stamina = stammax
                                                        print(f"{str(chname)}'s stamina is full")

                                            except:
                                                print("An error has occurred, please restart the game!")

                                    elif chend == "2" or chend == "2.":
                                        print(f"{str(chname)} - Wait! I can explain everything.")
                                        time.sleep(3)
                                        print(f"{str(chname)} - Just hear me out")
                                        time.sleep(3)
                                        print("GIANT - I'm sorry but your time is over.")
                                        time.sleep(3)
                                        print("The giant picked you up and started to walk into the darkness.")
                                        time.sleep(3)
                                        print("Neither you nor the giant was seen ever again.")
                                        time.sleep(3)
                                        print("\n\n\n\n\n\n-------------------------------")
                                        print("          Game Credits")
                                        print("-------------------------------\n")
                                        time.sleep(3)
                                        print("**Game Development Team:**\n")
                                        time.sleep(3)
                                        print("**Lead Developer:**")
                                        print("Polyák Marcell\n")
                                        time.sleep(3)
                                        print("**Game Designers:**")
                                        print("Molnár Maxim")
                                        print("Polyák Marcell\n")
                                        time.sleep(3)
                                        print("**Programmers:**")
                                        print("Molnár Maxim")
                                        print("Polyák Marcell\n")
                                        time.sleep(3)
#                                       print("**Quality Assurance:**")
#                                       print("[QA Tester 1 Name]")
#                                       print("[QA Tester 2 Name]\n")

#                                       print("-------------------------------\n")

#                                       print("**Special Thanks:**\n")

#                                       print("[Special Thanks 1]")
#                                       print("[Special Thanks 2]")
#                                       print("[Special Thanks 3]\n")

#                                       print("-------------------------------\n")

#                                       print("**Music:**")
#                                       print("[Composer Name]\n")

#                                       print("**Sound Effects:**")
#                                       print("[Sound Effects Artist Name]\n")

#                                       print("-------------------------------\n")

#                                        print("**Additional Contributors:**\n")

#                                        print(
#                                           "[List any other individuals or organizations that contributed to the game.]\n")

#                                        print("-------------------------------\n")

#                                        print("**Powered by:**")
#                                        print("[Game Engine/Library Used, if applicable]\n")

#                                        print("-------------------------------\n")

                                        print("Thank you to our players and supporters for making this game possible!\n")
                                        print("© 2023 Realms of Adventures. All Rights Reserved.")

                                        break
                                    print("-----------------------------------------------------\n")
                                else:
                                    print(f"{str(chname)} choose to back down from the boss.")
                            else:
                                print("You need to be at least on level 50 to start the final boss fight.")

                        elif insc == 'auto':
                            current_time = time.time()
                            time_difference = current_time - last_auto_time
                            time_remaining = 600 - time_difference

                            if time_remaining <= 0:
                                print("\nYou're about to turn auto mode on.")
                                print("--- This will reduce your life and stamina to 1. ---")
                                print("Auto mode is usable every 10 minutes.")
                                automode = input("Are you sure you want to use auto mode? (yes or no)\n--->")

                                if automode == 'yes' or automode == 'Yes':
                                    last_auto_time = time.time()
                                    hp = 1
                                    stamina = 1
                                    autolvls = random.randint(2,5)
                                    level += autolvls
                                    print(f"\n{str(chname)} levelled up and is now on level {str(level)}.")

                                else:
                                    print("Auto mode cancelled.")
                            else:
                                print(f"You need to wait {int(time_remaining)} seconds before using auto mode again.")

                        elif insc == 'levelup':
                            level = input("---->")

                        elif insc == 'quit':
                            print('You leaved The Game! Bye!')
                            break

                        elif insc == 'explore':
                            if incombat == 1:
                                print(chname + " is currently under attack, and can't go past the enemy.")
                            elif incombat == 0:
                                currentenemy = random.choice(enemy)
                                enhp = random.randint(3, 15)
                                if currentenemy == "Maxim":
                                    enhp = 200
                                    endmg = 5
                                print(chname + " found an enemy.")
                                print("\n-----------------------------------------------------")
                                print(f"Enemy type: {str(currentenemy)}")
                                print(f"Health: {str(enhp)}")
                                print("-----------------------------------------------------\n")
                                incombat = 1

                        elif insc == 'stats':
                            print("\n-----------------------------------------------------")
                            print('Character: ' + ch)
                            print('HP: ' + f"{str(hp)}/{str(hpmax)}")
                            print('Stamina: ' + f"{str(stamina)}/{str(stammax)}")
                            print('Damage: ' + f"{str(dmg)} + {str(dmgplus)}")
                            print('XP: ' + f"{str(xp)} + {str(xpplus)}")
                            print('Level: ' + str(level))
                            print('Skillpoints: ' + str(skillpts))
                            print("-----------------------------------------------------\n")

                        elif insc == 'level':
                            print("\n-----------------------------------------------------")
                            print('Level: ' + str(level))
                            print('Enemy HP: ' + str(enhp))
                            print('Enemy damage: ' + str(endmg))
                            print("-----------------------------------------------------\n")

                        elif insc == 'attack':
                            if incombat == 0:
                                print('There is no enemy to attack')
                            elif incombat == 1:
                                xpgain = random.randint(1, 4) + xpplus
                                xp += xpgain
                                hp -= endmg
                                stamina -= random.randint(1, 4)
                                enhp -= dmg + dmgplus
                                print('You attacked the enemy')
                                if enhp <= 0:
                                    print("\n-----------------------------------------------------")
                                    print(f"{str(chname)}{str(random.choice(ensucattack))}")
                                    print("-----------------------------------------------------\n")
                                    incombat = 0
                                    enhp = 0

                                elif enhp > 0:
                                    hp += hpsteal
                                    if hp > hpmax:
                                        hp = hpmax
                                    finaldmg = endmg + hpsteal
                                    print("\n-----------------------------------------------------")
                                    print(f"Enemy health: {str(enhp)} (-{str(dmg + dmgplus)})")
                                    print(f"Your health: {str(hp)}/{str(hpmax)} (-{str(finaldmg)})")
                                    print(f"Your stamina: {str(stamina)}/{str(stammax)}")
                                    print(f"Gained Experience: {str(xpgain)} XP")
                                    print("-----------------------------------------------------\n")
                                if xp >= 10:
                                    hp = hpmax
                                    stamina = stammax
                                    xp = 0
                                    level += 1
                                    if level >= 3:
                                        endmg += random.randint(1, 3)
                                    skillpts += 1
                                    dmg += random.randint(1, 3)
                                    print(chname + " levelled up, and is on currently level " + str(
                                        level) + ".")
                                    print(f"{str(chname)} has {str(skillpts)} skillpoints.")
                                    print("Use the command <skills> to choose a new skill.")

                                if hp <= 0:
                                    if lastchance == 1:
                                        print(f"You need to rest NOW, or {str(chname)} will die!")
                                        lastchance = 0
                                        hp = 1
                                    elif lastchance == 0:
                                        print('You died. The Game is over!')
                                        break

                                elif hp < 3:
                                    print(chname + ' is low on health, and needs to rest.')
                                elif stamina == 0:
                                    print(chname + ' had no more energy, fall asleep, and never woke up.')
                                    break
                                elif stamina < 3:
                                    print(chname + ' is really tired, and needs to rest immediately!')

                        elif insc == 'rest':
                            print(chname + random.choice(rest) + "\n")
                            resthp = random.randint(1, 5)
                            reststam = random.randint(1, 5)
                            hp += resthp
                            stamina += reststam
                            lastchance = 1

                            if hp < hpmax:
                                print(f"+{str(resthp)} health")
                            else:
                                hp = hpmax
                                print(f"{str(chname)}'s health is full")

                            if stamina < stammax:
                                print(f"+{str(reststam)} stamina\n")
                            else:
                                stamina = stammax
                                print(f"{str(chname)}'s stamina is full")

                    except:
                        print('An error has occurred, please restart The Game!')
                break

            elif q == "No" or q == "no":
                print(chname + random.choice(noans))
                tries += 1
                if tries == 5:
                    time.sleep(0.3)
                    print(chname + ' tried to avoid the cave, but stepped wrong and fell into the cave.')
                    goto(173)
        except:
            print('An error has occurred, please restart The Game!')


explore()