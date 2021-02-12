
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


profit = 0

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


def check_resources(ingredients_drink):
    for item in ingredients_drink:
        if ingredients_drink[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True



def check_transaction(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that`s not enough money. Money refunded")
        return False


def make_coffee(drink_name, ingredients_drink):
    for item in ingredients_drink:
        resources[item] -= ingredients_drink[item]
    print(f"Here is your {drink_name}. Enjoy!")


def print_report():
    print(f"Water:  {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney ${profit}")

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
                if check_transaction(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])


play()



