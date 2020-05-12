# print('''Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!''')

mach_ingredients_list = [400, 540, 120, 9, 550]
action_list = ['buy', 'fill', 'take', 'remaining', 'exit']

def print_mach_ingredients():
    print("The coffee machine has:")
    print(str(mach_ingredients_list[0]) + " of water")
    print(str(mach_ingredients_list[1]) + " of milk")
    print(str(mach_ingredients_list[2]) + " of coffee beans")
    print(str(mach_ingredients_list[3]) + " of disposable cups")
    print(str(mach_ingredients_list[4]) + " of money")
    print()


def mach_action():
    n = 1
    while n > 0:
        print("Write action (buy, fill, take, remaining, exit):")
        act = input()
        print()
        if act == action_list[0]:
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            i = input()
            if i == 'back':
                continue
            else:
                r = update_mach_ingredients(int(i))
                if r == -1:
                    continue
        elif act == action_list[1]:
            update_mach_ingredients(4)
        elif act == action_list[2]:
            update_mach_ingredients(5)
        elif act == action_list[3]:
            print_mach_ingredients()
        elif act == action_list[4]:
            exit()


def update_mach_ingredients(x):
    if x == 1:
        res = espresso()
        if res == -1:
            return -1
    elif x == 2:
        res = latte()
        if res == -1:
            return -1
    elif x == 3:
        res = cappuccino()
        if res == -1:
            return -1
    elif x == 4:
        print("Write how many ml of water do you want to add:")
        mach_ingredients_list[0] = mach_ingredients_list[0] + int(input())
        print("Write how many ml of milk do you want to add:")
        mach_ingredients_list[1] = mach_ingredients_list[1] + int(input())
        print("Write how many grams of coffee beans do you want to add:")
        mach_ingredients_list[2] = mach_ingredients_list[2] + int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        mach_ingredients_list[3] = mach_ingredients_list[3] + int(input())
    elif x == 5:
        print("I gave you $" + str(mach_ingredients_list[4]))
        mach_ingredients_list[4] = 0


def espresso():
    if mach_ingredients_list[0] < 250:
        print("Sorry, not enough water!")
        return -1
    elif mach_ingredients_list[2] < 16:
        print("Sorry, not enough coffee!")
        return -1
    elif mach_ingredients_list[3] < 1:
        print("Sorry, not enough cups!")
        return -1
    else:
        mach_ingredients_list[0] = mach_ingredients_list[0] - 250
        mach_ingredients_list[2] = mach_ingredients_list[2] - 16
        mach_ingredients_list[3] = mach_ingredients_list[3] - 1
        mach_ingredients_list[4] = mach_ingredients_list[4] + 4
        print("I have enough resources, making you a coffee!\n")
        return 1


def latte():
    if mach_ingredients_list[0] < 350:
        print("Sorry, not enough water!")
        return -1
    elif mach_ingredients_list[1] < 75:
        print("Sorry, not enough milk!")
        return -1
    elif mach_ingredients_list[2] < 20:
        print("Sorry, not enough coffee!")
        return -1
    elif mach_ingredients_list[3] < 1:
        print("Sorry, not enough cups!")
        return -1
    else:
        mach_ingredients_list[0] = mach_ingredients_list[0] - 350
        mach_ingredients_list[1] = mach_ingredients_list[1] - 75
        mach_ingredients_list[2] = mach_ingredients_list[2] - 20
        mach_ingredients_list[3] = mach_ingredients_list[3] - 1
        mach_ingredients_list[4] = mach_ingredients_list[4] + 7
        print("I have enough resources, making you a coffee!\n")
        return 1


def cappuccino():
    if mach_ingredients_list[0] < 200:
        print("Sorry, not enough water!")
        return -1
    elif mach_ingredients_list[1] < 100:
        print("Sorry, not enough milk!")
        return -1
    elif mach_ingredients_list[2] < 12:
        print("Sorry, not enough coffee!")
        return -1
    elif mach_ingredients_list[3] < 1:
        print("Sorry, not enough cups!")
        return -1
    else:
        mach_ingredients_list[0] = mach_ingredients_list[0] - 200
        mach_ingredients_list[1] = mach_ingredients_list[1] - 100
        mach_ingredients_list[2] = mach_ingredients_list[2] - 12
        mach_ingredients_list[3] = mach_ingredients_list[3] - 1
        mach_ingredients_list[4] = mach_ingredients_list[4] + 6
        print("I have enough resources, making you a coffee!\n")
        return 1


mach_action()
