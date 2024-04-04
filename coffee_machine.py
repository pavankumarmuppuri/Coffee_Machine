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

Profit = 0

def is_resources_sufficient(ordered_drink):
    try:
        for item in ordered_drink:
            if ordered_drink[item] > resources[item]:
                print(f"Sorry {item} is not sufficient ")
                return False
        return True
    except KeyError:
        print("Sorry, resource not found.")
        return False

def coins_received():
    try:
        print("Please insert the coins ")
        pennies = int(input("How many pennies ?  "))
        nickels = int(input("How many nickels ?  "))
        dimes = int(input("How many dimes ?  "))
        quarters = int(input("How many quarters ?  "))
        total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
        return total
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        #return 0

def is_payment_successful(coins_received, coffee_cost):
    try:
        if coins_received >= coffee_cost:
            global Profit
            Profit += coffee_cost
            change = round(coins_received - coffee_cost,2)
            print(f"Here is your $ {change} in change ")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded ")
            return False
    except TypeError:
        print("Invalid data type for calculation.")
        return False

def make_coffee(coffee_name, coffee_ingredients):
    try:
        for item in coffee_ingredients:
            resources[item] -= coffee_ingredients[item]
        print(f"Here is your {coffee_name} ... Enjoy")
    except KeyError:
        print("Ingredient not found.")

machine_on = True
while machine_on:
    choice = input("Preferred Drink ? ESPRESSO / LATTE / CAPPUCCINO  ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water = {resources['water']} ml ")
        print(f"Milk = {resources['milk']} ml ")
        print(f"Coffee = {resources['coffee']} gms ")
        print(f"Profit = $ {Profit}")
    else:
        try:
            coffee_type = MENU[choice]
            print(coffee_type)
            if is_resources_sufficient(coffee_type['ingredients']):
                payment = coins_received()
                if is_payment_successful(payment, coffee_type['cost']):
                    make_coffee(choice, coffee_type['ingredients'])
        except KeyError:
            print("Invalid choice. Please select from the menu.")
