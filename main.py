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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns if order can be made or not"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough{i}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins insert"""
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or false if its insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the {change}")
        global profit #reach profit by global scope
        profit += drink_cost
        return True
    else:
        print("Sorry, thats not enough, money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for i in order_ingredients:
      resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}")



is_on = True

while is_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']} ml")
       print(f"Milk: {resources['milk']} ml")
       print(f"Coffee: {resources['coffee']} g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])




