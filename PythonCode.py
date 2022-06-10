import re
import string

# Function to open and read the input file
grocery_items = dict()
input_file = open("CS210_Project_Three_Input_File.txt", "r")
for line in input_file:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in grocery_items:
            grocery_items[word] = grocery_items[word] + 1
        else:
            grocery_items[word] = 1
input_file.close()

# Function that prints each item purchased along with its quantity
def printItemCount():
    print("\nQUANTITY OF EACH ITEM PURCHASED TODAY\n")
    for item in list(grocery_items.keys()):
        print(item, end = "")
        print(":", grocery_items[item])
    print()

# Function that prints the specific item the user wants to see
def printCount(userItem):
    userItem = userItem.capitalize()
    for item in list(grocery_items.keys()):
        if (userItem == item):
            return grocery_items[item]
    return 0

# Function that creates a file and writes the items and the quantities purchased to frequency.dat
def createFile(fileName):
    input_file = open(fileName, "w")
    for item in list(grocery_items.keys()):
        input_file.write("\n" + item + " " + str(grocery_items[item]))
    input_file.close()
    return 0