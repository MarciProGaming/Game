import random
import time


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

xpmin = 10
tries = 0

# Enemy stats
enhp = random.randint(1, 3)
endmg = random.randint(0, 1)

def phaseOne():
    global chname
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
                            print('The Game has been started! Get ready for the adventure.')
                            time.sleep(0.2)
                            print('Write <help> to list the commands.')
                            break
                    except:
                        print('An error has occurred, please restart The Game!')
                break
            elif pho == 'start':
                print('The Game has been started! Get ready for the adventure.')
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
enemy = [' found an angry Goblin.', ' has been attacked by a Little Dragon.']
commands = ['help', 'quit', 'attack', 'rest', 'explore', 'stats', 'level']
incombat = 0


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
    while True:
        try:
            q = input(chname + random.choice(caveent) + "\n")
            if q == "Yes" or q == "yes":
                print(chname + ' slowly goes to the cave entrance and goes in.')
                print(chname + ' entered the dark and mysterious cave! ')
                print('Write <help> to list the commands.')
                while True:
                    try:
                        global insc
                        insc = input('--->')
                        if insc == 'help':
                            print(commands)

                        elif insc == 'quit':
                            print('You leaved The Game! Bye!')
                            break
                            quit()

                        elif insc == 'explore':
                            if incombat == 1:
                                print(chname + " is currently under attack, and can't go past the enemy.");
                            elif incombat == 0:
                                print(chname + random.choice(enemy))
                                incombat = 1
                                enhp = random.randint(3, 15)

                        elif insc == 'stats':
                            print('Character: ' + ch)
                            print('HP: ' + str(hp))
                            print('Stamina: ' + str(stamina))
                            print('Damage: ' + str(dmg))
                            print('XP: ' + str(xp))
                            print('Level: ' + str(level))

                        elif insc == 'level':
                            print('Level: ' + str(level))
                            print('Enemy HP: ' + str(enhp))
                            print('Enemy damage: ' + str(endmg))

                        elif insc == 'attack':
                            if incombat == 0:
                                print('There is no enemy to attack')
                            elif incombat == 1:
                                print('You attacked the enemy')
                                xp += random.randint(1, 4)
                                hp -= endmg
                                stamina -= 1
                                enhp -= dmg
                                if enhp <= 0:
                                    print(chname + random.choice(ensucattack))
                                    incombat = 0
                                elif enhp > 0:
                                    print(chname + random.choice(enattack))
                                if xp >= 10:
                                    xp = 0
                                    level += 1
                                    dmg += random.randint(1, 3)
                                    endmg += random.randint (0, 2)
                                    print(chname + " levelled up, and is on currently level " + str(level) + ".")
                                if hp == 0:
                                    print('You died. The Game is over!')
                                    break
                                    quit()
                                elif hp < 3:
                                    print(chname + ' is low on health, and needs to rest.')
                                elif stamina == 0:
                                    print(chname + ' had no more energy, fall asleep, and never woke up.')
                                    break
                                    quit()
                                elif stamina < 3:
                                    print(chname + ' is really tired, and needs to rest immediately!')


                        elif insc == 'rest':
                            print(chname + random.choice(rest))
                            hp += random.randint(1, 5)
                            stamina += random.randint(4, 9)
                            if hp > 10:
                                hp = 10
                                print(chname + "'s health is full.")
                            if stamina > 15:
                                stamina = 15
                                print(chname + "'s stamina is full.")
                    except:
                        print('An error has occurred, please restart The Game!')
                break

            elif q == "No" or q == "no":
                print(chname + random.choice(noans))
                tries += 1
                if tries == 5:
                    time.sleep(0.3)
                    print(chname + ' tried to avoid the cave, but stepped wrong and fell into the cave.')
                    while True:
                        try:
                            print('Write <help> to list the commands.')
                            while True:
                                try:
                                    insc = input('--->')
                                    if insc == 'help':
                                        print(commands)

                                    elif insc == 'quit':
                                        print('You leaved The Game! Bye!')
                                        break
                                        quit()

                                    elif insc == 'explore':
                                        if incombat == 1:
                                            print(chname + " is currently under attack, and can't go past the enemy.");
                                        elif incombat == 0:
                                            print(chname + random.choice(enemy))
                                            incombat = 1
                                            enhp = random.randint(3, 15)

                                    elif insc == 'stats':
                                        print('Character: ' + ch)
                                        print('HP: ' + str(hp))
                                        print('Stamina: ' + str(stamina))
                                        print('Damage: ' + str(dmg))
                                        print('XP: ' + str(xp))
                                        print('Level: ' + str(level))

                                    elif insc == 'level':
                                        print('Level: ' + str(level))
                                        print('Enemy HP: ' + str(enhp))
                                        print('Enemy damage: ' + str(endmg))

                                    elif insc == 'attack':
                                        if incombat == 0:
                                            print('There is no enemy to attack')
                                        elif incombat == 1:
                                            print('You attacked the enemy')
                                            xp += random.randint(1, 4)
                                            hp -= endmg
                                            stamina -= 1
                                            enhp -= dmg
                                            if enhp <= 0:
                                                print(chname + random.choice(ensucattack))
                                                incombat = 0
                                            elif enhp > 0:
                                                print(chname + random.choice(enattack))
                                            if xp >= 10:
                                                xp = 0
                                                level += 1
                                                dmg += random.randint(1, 3)
                                                endmg += random.randint(0, 2)
                                                print(chname + " levelled up, and is on currently level " + str(
                                                    level) + ".")
                                            if hp == 0:
                                                print('You died. The Game is over!')
                                                break
                                                quit()
                                            elif hp < 3:
                                                print(chname + ' is low on health, and needs to rest.')
                                            elif stamina == 0:
                                                print(chname + ' had no more energy, fall asleep, and never woke up.')
                                                break
                                                quit()
                                            elif stamina < 3:
                                                print(chname + ' is really tired, and needs to rest immediately!')

                                    elif insc == 'rest':
                                        print(chname + random.choice(rest))
                                        hp += random.randint(1, 5)
                                        stamina += random.randint(4, 9)
                                        if hp > 10:
                                            hp = 10
                                            print(chname + "'s health is full.")
                                        if stamina > 15:
                                            stamina = 15
                                            print(chname + "'s stamina is full.")
                                except:
                                    print('An error has occurred, please restart The Game!')
                            break
                        except:
                            print('An error has occurred, please restart The Game!')
                    break


            elif q == 'quit':
                print('You left The Game! Bye!')
                break
                quit()
        except:
            print('An error has occurred, please restart The Game!')


explore()