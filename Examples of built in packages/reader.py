import csv
import os
import sys


# Check command-line arguments
if len(sys.argv) < 3:
    print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
    sys.exit()

src = sys.argv[1]
dst = sys.argv[2]
changes = sys.argv[3:]

# Check if source file exists
if not os.path.isfile(src):
    print(f"Error: '{src}' does not exist or is not a file.")

    directory = os.path.dirname(src)
    if directory == "":
        directory = "."

    if os.path.isdir(directory):
        print("\nFiles in the same directory:")
        for filename in os.listdir(directory):
            print(filename)

    sys.exit()

# Read CSV file
with open(src, newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

# Apply changes
for change in changes:
    try:
        x, y, value = change.split(",", 2)
        x = int(x)
        y = int(y)

        data[y][x] = value

    except (ValueError, IndexError):
        print(f"Invalid change: {change}")

# Display modified CSV
print("Modified CSV:")
for row in data:
    print(",".join(row))

# Save modified CSV
with open(dst, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"\nModified file saved to '{dst}'")