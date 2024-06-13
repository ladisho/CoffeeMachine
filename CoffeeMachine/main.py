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

coffee_dilemma = True

cost = 0


def insert_coins():
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    print("Please insert coins: ")

    quarters = int(input("Quarter: "))
    quarter = quarter * quarters
    dimes = int(input("Dime: "))
    dime = dime * dimes
    nickels = int(input("Nickel: "))
    nickel = nickel * nickels
    pennies = int(input("Penny: "))
    penny = penny * pennies
    total = quarter + dime + nickel + penny
    rounded_total = round(total, 2)
    print(f"The total is: ${rounded_total} ")
    return rounded_total


def get_water():
    return resources.get("water")


def get_milk():
    return resources.get("milk")


def get_coffee():
    return resources.get("coffee")


while coffee_dilemma:

    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_choice == "off":
        coffee_dilemma = False

    elif coffee_choice == "report":
        water = get_water()
        milk = get_milk()
        coffee = get_coffee()

        print(f"Water : {water}\nMilk : {milk}\nCoffee : {coffee}\nMoney : ${cost} ")

    elif coffee_choice == "espresso":
        water = get_water()
        milk = get_milk()
        coffee = get_coffee()

        if water < 50:
            print("Sorry there is not enough water.")
            break
        elif coffee < 18:
            print("Sorry there is not enough coffee.")
            break

        total = insert_coins()

        if total < 1.5:
            print("Sorry that's not enough money. Money refunded.")
            coffee_dilemma = False
        elif total > 1.5:
            change = total - 1.5
            rounded_change = round(change, 2)
            print(f"Here is ${rounded_change} dollars in change.")

        resources.update({"water": water - 50})
        resources.update({"coffee": coffee - 18})

        # water_updated = get_water()
        # milk_updated = get_milk()
        # coffee_updated = get_coffee()

        cost += 1.5

        # print(f"Water : {water_updated}\nMilk : {milk_updated}\nCoffee : {coffee_updated}")

        print("Here is your Espresso. Enjoy!")

    elif coffee_choice == "latte":
        water = get_water()
        milk = get_milk()
        coffee = get_coffee()

        if water < 200:
            print("Sorry there is not enough water.")
            break
        if milk < 150:
            print("Sorry there is not enough milk.")
            break
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
            break

        total = insert_coins()

        if total < 2.5:
            print("Sorry that's not enough money. Money refunded.")
            coffee_dilemma = False
        elif total > 2.5:
            change = total - 2.5
            rounded_change = round(change, 2)
            print(f"Here is ${rounded_change} dollars in change.")

        resources.update({"water": water - 200})
        resources.update({"milk": milk - 150})
        resources.update({"coffee": coffee - 24})

        # water_updated = get_water()
        # milk_updated = get_milk()
        # coffee_updated = get_coffee()

        cost += 2.5

        # print(f"Water : {water_updated}\nMilk : {milk_updated}\nCoffee : {coffee_updated}\n")

        print("Here is your latte. Enjoy!")

    else:
        water = get_water()
        milk = get_milk()
        coffee = get_coffee()

        if water < 250:
            print("Sorry there is not enough water.")
            break
        if milk < 100:
            print("Sorry there is not enough milk.")
            break
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
            break

        total = insert_coins()

        if total < 3.0:
            print("Sorry that's not enough money. Money refunded.")
            coffee_dilemma = False
        elif total > 3.0:
            change = total - 3.0
            rounded_change = round(change, 2)
            print(f"Here is ${rounded_change} dollars in change.")

        resources.update({"water": water - 250})
        resources.update({"milk": milk - 100})
        resources.update({"coffee": coffee - 24})

        # water_updated = get_water()
        # milk_updated = get_milk()
        # coffee_updated = get_coffee()

        cost += 3.0

        # print(f"Water : {water_updated}\nMilk : {milk_updated}\nCoffee : {coffee_updated}")
        print("Here is your Cappuccino. Enjoy!")
