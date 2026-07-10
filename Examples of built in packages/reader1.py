import csv
import json
import pickle
import os
import sys


class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def load(self):
        pass

    def save(self, filename):
        pass

    def display(self):
        for row in self.data:
            print(",".join(row))

    def apply_changes(self, changes):
        for change in changes:
            try:
                x, y, value = change.split(",", 2)
                x = int(x)
                y = int(y)
                self.data[y][x] = value
            except (ValueError, IndexError):
                print(f"Invalid change: {change}")


class CSVHandler(FileHandler):
    def load(self):
        with open(self.filename, newline="") as file:
            reader = csv.reader(file)
            self.data = list(reader)

    def save(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.data)


class JSONHandler(FileHandler):
    def load(self):
        with open(self.filename, "r") as file:
            self.data = json.load(file)

    def save(self, filename):
        with open(filename, "w") as file:
            json.dump(self.data, file, indent=4)


class PickleHandler(FileHandler):
    def load(self):
        with open(self.filename, "rb") as file:
            self.data = pickle.load(file)

    def save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)


def get_handler(filename):
    extension = os.path.splitext(filename)[1].lower()

    if extension == ".csv":
        return CSVHandler(filename)
    elif extension == ".json":
        return JSONHandler(filename)
    elif extension == ".pickle":
        return PickleHandler(filename)
    else:
        print("Unsupported file type.")
        sys.exit()


def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
        return

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.isfile(src):
        print(f"Error: '{src}' does not exist or is not a file.")

        directory = os.path.dirname(src)
        if directory == "":
            directory = "."

        print("\nFiles in the same directory:")
        for file in os.listdir(directory):
            print(file)

        return

    handler = get_handler(src)

    handler.load()
    handler.apply_changes(changes)
    handler.display()

    destination_handler = get_handler(dst)
    destination_handler.data = handler.data
    destination_handler.save(dst)

    print(f"\nModified file saved to '{dst}'")


if __name__ == "__main__":
    main()