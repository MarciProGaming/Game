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

enemy = [' found an angry Goblin.', ' has been attacked by a Little Dragon.']
commands = ['help', 'quit', 'attack', 'rest', 'explore', 'stats', 'level', 'auto', 'skills']
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
                                print("-----------------------------------------------------\n")

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

                        elif insc == 'quit':
                            print('You leaved The Game! Bye!')
                            break

                        elif insc == 'explore':
                            if incombat == 1:
                                print(chname + " is currently under attack, and can't go past the enemy.")
                            elif incombat == 0:
                                print(chname + random.choice(enemy))
                                incombat = 1
                                enhp = random.randint(3, 15)

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
                            print('Level: ' + str(level))
                            print('Enemy HP: ' + str(enhp))
                            print('Enemy damage: ' + str(endmg))

                        elif insc == 'attack':
                            if incombat == 0:
                                print('There is no enemy to attack')
                            elif incombat == 1:
                                print('You attacked the enemy')
                                xp += random.randint(1, 4) + xpplus
                                hp -= endmg
                                stamina -= random.randint(1, 4)
                                enhp -= dmg + dmgplus
                                if enhp <= 0:
                                    print(chname + random.choice(ensucattack))
                                    incombat = 0
                                    enhp = 0

                                elif enhp > 0:
                                    hp += hpsteal
                                    if hp > hpmax:
                                        hp = hpmax
                                    print("\n-----------------------------------------------------")
                                    print(f"Enemy health: {str(enhp)} (-{str(dmg + dmgplus)})")
                                    print(f"Your health: {str(hp)}/{str(hpmax)} (-{str(endmg)}) (+{str(hpsteal)})")
                                    print(f"Your stamina: {str(stamina)}/{str(stammax)}")
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