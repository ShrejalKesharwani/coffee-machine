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
units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

coins = {
    "pennies": 0,
    "nickles": 0,
    "dimes": 0,
    "quarter": 0
}

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        for key in resources:
            print(f"{key}: {resources[key]}{units[key]}")
        print(f"money: ${money}")

    elif choice == "off":
        is_on = False

    else:
        for key in MENU[choice]["ingredients"]:
            flag = 0
            if MENU[choice]["ingredients"][key] > resources[key]:
                print(f"Sorry, there is not enough {key}.")
                flag += 1
                break
        if flag == 0:
            print("Please insert coins.")
            for key in coins:
                coins[key] = int(input(f"How many {key}?:"))

            amount = coins["pennies"]*0.01 + coins["nickles"]*0.05 + coins["dimes"]*0.10 + coins["quarter"]*0.25
            price = MENU[choice]["cost"]

            if amount > price:
                print(f"Here is ${amount - price} in change.")
                print(f"Here is your {choice} ☕ Enjoy!")
                money += price
                for key in MENU[choice]["ingredients"]:
                    resources[key] -= MENU[choice]["ingredients"][key]

            elif amount == price:
                print(f"Here is your {choice} ☕ Enjoy!")
                money += price
                for key in MENU[choice]["ingredients"]:
                    resources[key] -= MENU[choice]["ingredients"][key]

            else:
                print("Sorry you have not inserted sufficient coins. Please enter sufficient coins.")





