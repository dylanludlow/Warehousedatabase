import os
from ast import literal_eval


class AccountingSystem:
    DATA_FILE = "data.txt"

    def __init__(self):
        self.balance = 0.0
        self.warehouse = {}
        self.operations = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.DATA_FILE):
            return

        try:
            with open(self.DATA_FILE, "r") as file:
                data = literal_eval(file.read())

            self.balance = data.get("balance", 0.0)
            self.warehouse = data.get("warehouse", {})
            self.operations = data.get("operations", [])

        except Exception:
            print("Could not load saved data.")

    def save_data(self):
        data = {
            "balance": self.balance,
            "warehouse": self.warehouse,
            "operations": self.operations,
        }

        with open(self.DATA_FILE, "w") as file:
            file.write(str(data))


class Manager:
    def __init__(self, system):
        self.system = system
        self.actions = {}

    def assign(self, name):
        def decorator(func):
            self.actions[name] = func
            return func
        return decorator

    def execute(self, command):
        action = self.actions.get(command)

        if action:
            action()
            self.system.save_data()
        else:
            print("Unknown command.")


system = AccountingSystem()
manager = Manager(system)


@manager.assign("balance")
def balance():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    comment = input("Comment: ")

    system.balance += amount
    system.operations.append(("balance", amount, comment))

    print(f"Current balance: {system.balance}")


@manager.assign("purchase")
def purchase():
    product = input("Product name: ")

    try:
        price = float(input("Unit price: "))
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    cost = price * quantity

    if cost > system.balance:
        print("Insufficient funds.")
        return

    system.balance -= cost
    system.warehouse[product] = system.warehouse.get(product, 0) + quantity
    system.operations.append(("purchase", product, price, quantity))

    print("Purchase recorded.")


@manager.assign("sale")
def sale():
    product = input("Product name: ")

    if product not in system.warehouse:
        print("Product not found.")
        return

    try:
        price = float(input("Unit price: "))
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    if quantity > system.warehouse[product]:
        print("Not enough stock.")
        return

    system.warehouse[product] -= quantity

    if system.warehouse[product] == 0:
        del system.warehouse[product]

    income = price * quantity
    system.balance += income

    system.operations.append(("sale", product, price, quantity))

    print("Sale recorded.")


@manager.assign("account")
def account():
    print(f"Balance: {system.balance}")


@manager.assign("list")
def list_products():
    if not system.warehouse:
        print("Warehouse is empty.")
        return

    for product in system.warehouse:
        print(product)


@manager.assign("warehouse")
def warehouse():
    product = input("Product name: ")

    print(system.warehouse.get(product, 0))


@manager.assign("review")
def review():
    if not system.operations:
        print("No operations recorded.")
        return

    try:
        start = int(input("Start index: "))
        end = int(input("End index: "))
    except ValueError:
        print("Invalid input.")
        return

    if start < 0 or end >= len(system.operations) or start > end:
        print("Invalid range.")
        return

    for operation in system.operations[start:end + 1]:
        print(operation)


def menu():
    print("\nAvailable commands:")
    print("balance")
    print("purchase")
    print("sale")
    print("account")
    print("list")
    print("warehouse")
    print("review")
    print("end")


while True:
    menu()

    command = input("Command: ").lower()

    if command == "end":
        system.save_data()
        print("Program ended.")
        break

    manager.execute(command)