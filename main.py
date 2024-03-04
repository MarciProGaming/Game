import random
import sys
import time
import threading
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
xpupgrd = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
gold = 0
goldbonus = 0
armor = 0

#Final boss fight
bosshp = 500
bossdmg = 20

# Enemy stats
enhp = random.randint(1, 3)
endmg = random.randint(0, 1)

# Buyable items
level1 = ["Bronze sword", "bow"]

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


def print_help():
    print("\n-----------------------------------------------------")
    print("Available Commands:")
    print("help - Display this help menu.")
    print("quit - Exit the game.")
    print("attack - Engage in combat with an enemy.")
    print("rest - Rest to regenerate health and stamina.")
    print("explore - Search for enemies to battle.")
    print("stats - Display your character's statistics.")
    print("level - Show information about the current enemy.")
    print("auto - Automatically fight enemies and level up.")
    print("skills - View and upgrade your character's skills.")
    print("shop - Browse buyable items.")
    print("-----------------------------------------------------\n")

def print_stats():
    print("\n-----------------------------------------------------")
    print('Character: ' + ch)
    print('HP: ' + f"{str(hp)}/{str(hpmax)}")
    print('Stamina: ' + f"{str(stamina)}/{str(stammax)}")
    print('Damage: ' + f"{str(dmg)} + {str(dmgplus)}")
    print('XP: ' + f"{str(xp)} + {str(xpplus)}")
    print('Level: ' + str(level))
    print('Skillpoints: ' + str(skillpts))
    print('Gold: ' + f"{str(gold)} gold coin(s)")
    print("-----------------------------------------------------\n")

def print_quit():
    print('You left The Game! Bye!')

def print_level():
    print("\n-----------------------------------------------------")
    print('Level: ' + str(level))
    print('Enemy HP: ' + str(enhp))
    print('Enemy damage: ' + str(endmg))
    print("-----------------------------------------------------\n")

def print_skills():
    global skillpts, lfstlsklpts, stmnsklpts, hpsklpts, dmgsklpts, fstlrnsklpts, hpsteal, stammax, hpmax, dmgplus, xpplus
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
            hpsteal += random.randint(1, 2)
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
            hpmax += random.randint(1, 2)
            upgrskl = "More Health"
            skillpts -= 1
            print(f"You upgraded the skill [{str(upgrskl)}]. It is now on level {str(hpsklpts)}")

        elif skillupgr == "4" or skillupgr == "4.":
            dmgsklpts += 1
            dmgplus += random.randint(1, 3)
            upgrskl = "Increase Damage"
            skillpts -= 1
            print(f"You upgraded the skill [{str(upgrskl)}]. It is now on level {str(dmgsklpts)}")

        elif skillupgr == "5" or skillupgr == "5.":
            fstlrnsklpts += 1
            xpplus += random.randint(0, 4)
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

def print_auto():
    global hp, stamina, level

    last_auto_time = time.time()
    current_time = time.time()
    time_difference = current_time - last_auto_time
    time_remaining = 600 - time_difference

    if time_remaining <= 0:
        print("\nYou're about to turn auto mode on.")
        print("--- This will reduce your life and stamina to 1. ---")
        print("Auto mode is usable every 10 minutes.")
        automode = input("Are you sure you want to use auto mode? (yes or no)\n--->")

        if automode == 'yes' or automode == 'Yes':
            hp = 1
            stamina = 1
            autolvls = random.randint(2, 5)
            level += autolvls
            print(f"\n{str(chname)} levelled up and is now on level {str(level)}.")

        else:
            print("Auto mode cancelled.")
    else:
        print(f"You need to wait {int(time_remaining)} seconds before using auto mode again.")

def print_explore():
    global incombat, enhp, endmg
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

def print_attack():
    global incombat, xp, endmg, hp, stamina, enhp, xpmin, level, skillpts, lastchance, dmg, gold
    if incombat == 0:
        print('There is no enemy to attack')
    elif incombat == 1:
        xpgain = random.randint(1, 4) + xpplus
        xp += xpgain
        armoreddmg = endmg - armor
        hp -= armoreddmg
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
            goldearned = random.randint(0, 3) + goldbonus
            gold += goldearned
            if hp > hpmax:
                hp = hpmax
            finaldmg = endmg - armor + hpsteal
            print("\n-----------------------------------------------------")
            print(f"Enemy health: {str(enhp)} (-{str(dmg + dmgplus)})")
            print(f"Your health: {str(hp)}/{str(hpmax)} (-{str(finaldmg)})")
            print(f"Your stamina: {str(stamina)}/{str(stammax)}")
            print(f"Gained Experience: {str(xpgain)} XP")
            print(f"Gold coins: {str(gold)} (+{str(goldearned)})")
            print("-----------------------------------------------------\n")
        if xp >= xpmin:
            xpmin = xpmin * random.choice(xpupgrd)
            hp = hpmax
            stamina = stammax
            xp = 0
            level += 1
            if level >= 3:
                endmg += random.randint(1, 4)
            elif level >= 5:
                endmg += random.randint(1, 6)
            elif level >= 10:
                endmg += random.randint(3, 10)
            elif level >= 15:
                endmg += random.randint(5, 13)
            elif level >= 20:
                endmg += random.randint(7, 16)
            elif level >= 25:
                endmg += random.randint(9, 20)
            elif level >= 50:
                endmg += random.randint(20, 50)
            skillpts += 1
            print(chname + " levelled up, and is on currently level " + str(
                level) + ".")
            print(f"{str(chname)} has {str(skillpts)} skill points.")
            print("Use the command <skills> to choose a new skill.")

        if hp <= 0:
            if lastchance == 1:
                print(f"You need to rest NOW, or {str(chname)} will die!")
                lastchance = 0
                hp = 1
            elif lastchance == 0:
                print('You died. The Game is over!')
                sys.exit()

        elif hp < 3:
            print(chname + ' is low on health, and needs to rest.')
        elif stamina == 0:
            print(chname + ' had no more energy, fall asleep, and never woke up.')
            sys.exit()
        elif stamina < 3:
            print(chname + ' is really tired, and needs to rest immediately!')

def print_rest():
    global stamina, hp, lastchance
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

def print_shop():
    shop.run_shop()
class Shop:
    def __init__(self):
        self.all_items = [
            {"name": "Common Item 1", "rarity": "Common", "price": 10, "dmgplus": 2, "goldbonus": 0, "armorplus": 2, "item_type": "armor"},
            {"name": "Common Item 2", "rarity": "Common", "price": 10, "dmgplus": 1, "goldbonus": 0, "armorplus": 0, "item_type": "weapon"},
            {"name": "Uncommon Item 1", "rarity": "Uncommon", "price": 20, "dmgplus": 4, "goldbonus": 0, "armorplus": 2, "item_type": "armor"},
            {"name": "Uncommon Item 2", "rarity": "Uncommon", "price": 20, "dmgplus": 3, "goldbonus": 0, "armorplus": 0, "item_type": "weapon"},
            {"name": "Rare Item 1", "rarity": "Rare", "price": 30, "dmgplus": 6, "goldbonus": 2, "armorplus": 2, "item_type": "armor"},
            {"name": "Rare Item 2", "rarity": "Rare", "price": 30, "dmgplus": 5, "goldbonus": 1, "armorplus": 0, "item_type": "weapon"},
        ]
        self.current_items = []
        self.refresh_time = 5 * 60  # 5 minutes in seconds
        self.refresh_timer = None

    def refresh_shop(self):
        print("Refreshing the shop...")
        self.current_items = random.choices(self.all_items, k=5)
        self.start_refresh_timer()

    def show_shop(self):
        print("----- Shop -----")
        for i, item in enumerate(self.current_items, 1):
            if item['item_type'] == "weapon":
                print(f"{i}. {item['name']} ({item['rarity']}) Damage: +{item['dmgplus']} - Price: {item['price']} gold.")
            else:
                print(f"{i}. {item['name']} ({item['rarity']}) Armor: +{item['armorplus']} - Price: {item['price']} gold.")
        print("----------------")

    def start_refresh_timer(self):
        if self.refresh_timer is not None and self.refresh_timer.is_alive():
            print("Timer is still running. Please wait until it resets.\n")
        else:
            print(f"Next shop refresh in {self.refresh_time // 60} minutes. Timer started.\n")
            self.refresh_timer = threading.Timer(self.refresh_time, self.refresh_shop)
            self.refresh_timer.start()

    def purchase_item(self, choice):
        global gold, dmgplus, goldbonus, armor
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.current_items):
                item = self.current_items[choice - 1]
                if gold >= item['price']:
                    print(f"\nYou purchased {item['name']} for {item['price']} coins.")
                    gold -= item['price']
                    print(f"Remaining gold: {gold}")
                    # Update player modifiers
                    goldbonus += item['goldbonus']
                    dmgplus += item['dmgplus']
                    armor += item['armorplus']

                    print(f"Gold bonus from {item['name']}: +{item['goldbonus']}")
                else:
                    print("Not enough gold to purchase this item.")
            else:
                print("Invalid choice. Please choose a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run_shop(self):
        if self.refresh_timer is not None and self.refresh_timer.is_alive():
            print(f"{self.refresh_time // 60} minutes until the shop refresh.\n")
            self.show_shop()
            purchase_option = input("Do you want to purchase an item? (y/n): ")
            if purchase_option.lower() == 'y':
                choice = input("Enter the number of the item you want to purchase: ")
                self.purchase_item(choice)
        else:
            self.refresh_shop()
            self.show_shop()
            purchase_option = input("Do you want to purchase an item? (y/n): ")
            if purchase_option.lower() == 'y':
                choice = input("Enter the number of the item you want to purchase: ")
                self.purchase_item(choice)
shop = Shop()


# noinspection PyTypeChecker
def explore():
    time.sleep(1.1)
    global hp, hpmax, hpsteal, xp, xpmin, xpplus, level, stamina, stammax, dmg, dmgplus, incombat, armor
    global tries, enhp, endmg, lastchance, bosshp, bossdmg
    global skillpts, fstlrnsklpts, lfstlsklpts, upgrskl, hpsklpts, stmnsklpts, dmgsklpts
    global wizardskills, berserkerskills, assassinskills, archerskills
    global gold, goldbonus

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
                            print_help()

                        elif insc == 'auto':
                            print_auto()

                        elif insc == 'skills':
                            print_skills()

                        elif insc == 'levelup':
                            level = input("---->")

                        elif insc == 'quit':
                            print_quit()
                            break

                        elif insc == 'explore':
                            print_explore()

                        elif insc == 'stats':
                            print_stats()

                        elif insc == 'level':
                            print_level()

                        elif insc == 'attack':
                            print_attack()

                        elif insc == 'rest':
                            print_rest()

                        elif insc == 'shop':
                            print_shop()

                    except:
                        print('An error has occurred, please restart The Game!')
                break

            elif q == "No" or q == "no":
                print(chname + random.choice(noans))
                tries += 1
                if tries == 5:
                    time.sleep(0.3)
                    print(chname + ' tried to avoid the cave, but stepped wrong and fell into the cave.')
                    goto(474)
        except:
            print('An error has occurred, please restart The Game!')


explore()