
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}

MONEY = 0


# TODO: 1 input- report print resources
# TODO: 2 check resources is sufficient
# TODO: 3 Penny - 0.01, Nickel - 0.05, Dime - 0.1, Quarter - 0.25
# TODO: 4 Get flavour
# TODO: 5 get change


def proccess_coins():
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.1
    total += float(input("How many nickels?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return total


'''
def check_resources(user_drink):
    if resources['water'] >= MENU[user_drink]['ingredients']['water'] and resources['milk'] >= MENU[user_drink]['ingredients']['milk'] and resources['coffee'] >= MENU[user_drink]['ingredients']['coffee']:
        resources['water'] -= MENU[user_drink]['ingredients']['water']
        resources['milk'] -= MENU[user_drink]['ingredients']['milk']
        resources['coffee'] -= MENU[user_drink]['ingredients']['coffee']
        return True
    else:
        return False
'''

def check_resources(ingredients_drink):
    for item in  ingredients_drink:
        if ingredients_drink[item] >= resources[item]
            print(f"Sorry there is not enough {item}")
            return False
    return True



def check_transaction():
    if resources["cash"] >= MENU[user_drink]['cost']:
        resources["cash"] -= MENU[user_drink]['cost']
        return True
    else:
        return False


def print_report():
    print(f"Water:  {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney ${round(resources['cash'],2)}")

def play():
    turn_off = False

    while not turn_off:

        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice == 'report':
            print_report()
        elif choice == 'off':
            turn_off = True
        else:
            drink = MENU[choice]
            if check_resources(drink['ingredients']):
                payment = proccess_coins()
                if check_transaction(payment, drink['cost']:
                print("Sorry not enough resources")
                turn_off = True
            else:
                print(f"Enjoy your {choice}")


check_resources(MENU['latte']['ingredients'])