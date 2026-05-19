max_items = int(input("Enter maximum number of items: "))

current_package_weight = 0
packages_sent = 0
total_weight_sent = 0
total_unused_capacity = 0
largest_unused = 0
largest_unused_package = 0

for item in range(max_items):
    try:
        weight = int(input("Enter item weight: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if weight == 0:
            break
    if weight < 1 or weight > 10:
        print("Invalid weight. Must be between 1 and 10.")
        continue
    if current_package_weight + weight > 20:

        packages_sent += 1
        total_weight_sent += current_package_weight

        unused = 20 - current_package_weight
        total_unused_capacity += unused

        if unused > largest_unused:
            largest_unused = unused
            largest_unused_package = packages_sent

        current_package_weight = weight

    else:
        current_package_weight += weight

if current_package_weight > 0:
    packages_sent += 1
    total_weight_sent += current_package_weight

    unused = 20 - current_package_weight
    total_unused_capacity += unused

    if unused > largest_unused:
        largest_unused = unused
        largest_unused_package = packages_sent
print("\nResults:")
print("Packages sent:", packages_sent)
print("Total weight sent:", total_weight_sent)
print("Package with most unused capacity:", largest_unused_package)
print("Unused capacity in that package:", largest_unused)





