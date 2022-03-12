import machineData # DataBase for coffee machine


def val_coffee_req():
    """This function will ask the user for a coffee, check that the input is correct and return the request as a
    string. "report" request will print the resources and "quit" request will quit the program """
    str = "" # initialize string to be returned

    # loop until meet condition for valid request:
    while str != "espresso" and str != "latte" and str != "cappuccino" and str != "report" and str != "quit":
        str = (input("What would you like? (Espresso, Latte, Cappuccino) ")).lower()
        if str == "espresso" or str == "latte" or str == "cappuccino" or str == "report" or str == "quit":
            return str # return request for machine
        else:
            print(f"'{str}' Is not a valid request.\n")


def print_report():
    """This function will print the Coffee Machine resources"""
    print(f"Available resources:")
    print(f"Water: {machineData.resource['water']}ml")
    print(f"Milk: {machineData.resource['milk']}ml")
    print(f"Coffee: {machineData.resource['coffee']}g")


def coffee_prep(coffee_type):
    """This function will verify the amount of resources in the machine is sufficient for making user request
        return true if resources are sufficient, else return false"""
    # Check that water and coffee amount in the machine is equal or bigger than user requested coffee:
    for item in machineData.menu[coffee_type]: # loop through ingredients
        if (item != "price") and (machineData.menu[coffee_type][item]) > (machineData.resource[item]):
            return False # resources are not sufficient
    return True # resources are sufficient (water and coffee)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def transaction(coffee_topay):
    """This function will ask user for payment in coins and verify the amount is sufficient
        return true if all amount is paid, else return false"""
    coffee_price = (machineData.menu[coffee_topay]["price"]) # initialize coffee price
    # Ask for coins:
    print(f"\nThe {coffee_topay} will cost {'{:.2f}'.format(coffee_price)}.") # return price with two digits after the decimal point
    print("Types of coins accepted: Half Shekels = 0.50, Shekels = 1.00, Shnekels = 2.00, Five Shekels = 5.00, Ten Shekels = 10.00.\n")
    print("Please insert coins:")
    half_shekels = input("How many Half Shekels? ")
    shekels = input("How many Shekels? ")
    shnekels = input("How many Shnekels? ")
    five_shekels = input("How many Five Shekels? ")
    ten_shekels = input("How many Ten Shekels? ")

    # Check that user inserted valid coins (using function isfloat()):
    if isfloat(half_shekels) and isfloat(shekels) and isfloat(shnekels) and isfloat(five_shekels) and isfloat(ten_shekels):
        # Calculate coins to a total amount:
        total = (float(half_shekels) * machineData.coins["Half Shekel"]) + (float(shekels) * machineData.coins["Shekel"]) +\
                (float(shnekels) * machineData.coins["Shnekel"]) + (float(five_shekels) * machineData.coins["Five Shekel"]) +\
                (float(ten_shekels) * machineData.coins["Ten Shekel"])
        if total < coffee_price:
            print("Insufficient payment amount\n\n")
            return False
        else:
            if total == coffee_price:
                return True
            else:
                print(f"Change returned: {'{:.2f}'.format(total - coffee_price)} Shnekels.\n") # return change with two digits after the decimal point
                return True
    else:
        print("Coin input was in valid.\n")


def make(coffee_make):
    """This function will make coffee and subtract the amount of resources used to make the coffee"""
    for item in machineData.menu[coffee_make]: # loop through ingredients
        if (item != "price"):
            machineData.resource[item] = machineData.resource[item] - machineData.menu[coffee_make][item]


def check_maintenance():
    """Check if coffee machine have sufficient resources to make coffee -
        if maintenance is needed (to refill resources) - return true"""
    if machineData.resource["water"] < machineData.menu["espresso"]["water"] \
            or machineData.resource["coffee"] < machineData.menu["espresso"]["coffee"]:
        return True # need maintenance


def coffee_machine():
    """Main coffee machine function"""
    # Take user coffee request:
    coffee_req = val_coffee_req()

    # If request is report or quit:
    if coffee_req == "quit":
        return # quit program
    if coffee_req == "report":
        print_report() # print report of current machine resources
        coffee_machine() # recall main function
    else: # else - if user request is a coffee
        # else: if make_coffee is false - insufficient ingredients for that coffee, else payment func:
        make_coffee = coffee_prep(coffee_req)
        if not make_coffee:
            print(f"Insufficient ingredients. Sorry, {coffee_req} is not available right now.\n")
        else:
            make_coffee = transaction(coffee_req) # payment func
        if make_coffee: # if payment succeeded - call make() print enjoy
            make(coffee_req)
            print(f"Enjoy! Your {coffee_req}!\n")
        maintenance = check_maintenance() # check resource is sufficient
        if not maintenance:
            coffee_machine()
        else:
            print("The machine in maintenance. Sorry.\n")


# Main:
coffee_machine()
