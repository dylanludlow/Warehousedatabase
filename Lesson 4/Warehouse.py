balance = 0.0
warehouse = {}
operations = []

while True:
    print("\nAvailable commands:")
    print("balance")
    print("sale")
    print("purchase")
    print("account")
    print("list")
    print("warehouse")
    print("review")
    print("end")

    command = input("Enter command: ").lower()

    if command == "end":
        print("Program ended.")
        break

    elif command == "balance":
        try:
            amount = float(input("Amount to add/subtract: "))
            balance += amount
            operations.append(("balance", amount))
        except ValueError:
            print("Invalid amount.")

    elif command == "purchase":
        try:
            product = input("Product name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            cost = price * quantity

            if balance - cost < 0:
                print("Purchase rejected. Insufficient funds.")
                continue

            balance -= cost

            if product in warehouse:
                warehouse[product]["quantity"] += quantity
                warehouse[product]["price"] = price
            else:
                warehouse[product] = {
                    "price": price,
                    "quantity": quantity
                }

            operations.append(
                ("purchase", product, price, quantity)
            )

        except ValueError:
            print("Invalid input.")

    elif command == "sale":
        try:
            product = input("Product name: ")
            price = float(input("Sale price: "))
            quantity = int(input("Quantity: "))

            if product not in warehouse:
                print("Product not found.")
                continue

            if warehouse[product]["quantity"] < quantity:
                print("Not enough stock.")
                continue

            warehouse[product]["quantity"] -= quantity
            balance += price * quantity

            operations.append(
                ("sale", product, price, quantity)
            )

        except ValueError:
            print("Invalid input.")

    elif command == "account":
        print(f"Account balance: {balance}")

    elif command == "list":
        if not warehouse:
            print("Warehouse is empty.")
        else:
            for product, data in warehouse.items():
                print(
                    f"{product}: "
                    f"Price={data['price']}, "
                    f"Quantity={data['quantity']}"
                )

    elif command == "warehouse":
        product = input("Product name: ")

        if product in warehouse:
            print(
                f"{product}: "
                f"Price={warehouse[product]['price']}, "
                f"Quantity={warehouse[product]['quantity']}"
            )
        else:
            print("Product not found.")

    elif command == "review":
        start = input("From index (leave blank for all): ")
        end = input("To index (leave blank for all): ")

        if start == "" and end == "":
            for index, operation in enumerate(operations):
                print(index, operation)
        else:
            try:
                start = int(start)
                end = int(end)

                if start < 0 or end >= len(operations):
                    print("Index out of range.")
                    continue

                for index in range(start, end + 1):
                    print(index, operations[index])

            except ValueError:
                print("Invalid indices.")

    else:
        print("Unknown command.")