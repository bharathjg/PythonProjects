# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


resources = {'water': 0, 'milk': 0, 'coffee': 0, 'money': 0.0}
coins = {'quarter': 0.25, 'dime': 0.1, 'nickel': 0.05, 'penny': 0.01}
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


def report():
    print("Water: ", resources['water'], "ml")
    print("Milk: ", resources['milk'], "ml")
    print("Coffee: ", resources['coffee'], "g")
    print('Money: $', resources['money'])


def check(water, milk, coffee):
    if resources['water'] < water:
        print("Sorry, there isn't enough water")
        return False
    if resources['milk'] < milk:
        print("Sorry, there isn't enough milk")
        return False
    if resources['coffee'] < coffee:
        print("Sorry, there isn't enough coffee")
        return False

    return True


def process_coins():
    total = 0
    money = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}
    print("Insert coins (Quarters, Dimes, Nickels or Pennies). Type 'done' when finished.")
    while True:
        coin = input()
        coin = str.lower(coin)
        if coin == 'done':
            return total
        total += coins[coin]
        print(f"Current total: ${total}")
        money[coin] += 1


def check_transaction(cost, money):
    if money < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    if money >= cost:
        return True


def make_coffee(choice, water, milk, coffee, cost):
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    resources['money'] += cost
    print(f'Here is your {choice}. Enjoy!')
    return


def main(initial_resources):
    resources['water'] = initial_resources[0]
    resources['milk'] = initial_resources[1]
    resources['coffee'] = initial_resources[2]
    while True:
        print("Coffee Machine")
        print(f"What would you like? (Espresso: ${MENU['espresso']['cost']} /Latte: ${MENU['latte']['cost']} /Cappuccino: ${MENU['cappuccino']['cost']})")
        print("Type 'report' to see resources in Coffee Machine")
        print("Type 'off' to switch off Coffee Machine")
        choice = input()
        choice = str.lower(choice)
        if choice == 'off':
            sys.exit()
        if choice == 'report':
            report()
            continue
        water = MENU[choice]['ingredients']['water']
        if choice == 'espresso':
            milk = 0
        else:
            milk = MENU[choice]['ingredients']['milk']
        coffee = MENU[choice]['ingredients']['coffee']
        cost = MENU[choice]['cost']

        flag1 = check(water, milk, coffee)
        if flag1:
            money = process_coins()

        flag2 = check_transaction(cost, money)
        if flag2:
            change = round(money - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")

            make_coffee(choice, water, milk, coffee, cost)




# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    initial_resources = [300, 200, 100]
    main(initial_resources)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
