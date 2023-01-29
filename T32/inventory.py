from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    #constructor method for the Shoe class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #method to get the cost of the shoe
    def get_cost(self):
        return self.cost

    #method to get the quantity of the shoe in stock
    def get_quantity(self):
        return self.quantity

    #method to return a representation of the shoe object
    def __str__(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]


#=============Shoe list===========
#The list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data(shoe_list):
    try:
        #open the file "inventory.txt" in read mode
        with open ("inventory.txt", 'r') as file:
            #skip first line
            next(file)
            #iterate through each line in the file
                #split the line by comma and assign variables to the values
            for line in file:
                country, code, product, cost, quantity = line.strip().split(',')
                shoe_list.append(Shoe(country, code, product, cost, quantity))
    #print error message if file is not found
    except FileNotFoundError:
        print("Inventory.txt does not exist")
    #print error message if any other exception occurs    
    except Exception as e:
        print(f"An error occurred: {e}")
    #return the updated shoe_list   
    return shoe_list


def capture_shoes(shoe_list):
    #ask for user-input to create new shoe for list
    country = input("Enter Country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = input("Enter shoe cost: ")
    quantity = input("Enter shoe quantity: ")

    #create a new Shoe object with inputted values
        #append new shoe object to passed in shoe_list
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    print("Shoe added to invetory list")


def view_all(shoe_list):
    #defining headers for the table
        #list comprehension to convert each shoe object to a string representation
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    table = [shoe.__str__() for shoe in shoe_list]
    print(tabulate(table, headers, tablefmt="pretty"))


def re_stock(shoe_list):
    print("Function will display lowest quantity shoe.")

    #find the shoe with the lowest quantity using the min() function and the lambda function as an argument
    min_quantity = min(shoe_list, key=lambda x: x.quantity)
    response = input(f"Do you want to restock {min_quantity.product}? (Y/N): ").upper()

    if response == 'Y':
        quantity = input("Enter the quantity to add: ")
        min_quantity.quantity += quantity
        print(f"{quantity} {min_quantity.product} successfully added to the inventory.")

        #try to write the updated inventory to a text file
            #if an error occurs, display the error message to the user
        try:
            with open('inventory.txt', 'w') as file:
                for shoe in shoe_list:
                    file.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Re-stocking cancelled.")

def search_shoe(shoe_list):
    #enter shoe code search through the shoes in shoe_list
        #compare the shoe.code to user entered code
    code = int(input("Enter the shoe code: "))
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return None


def value_per_item(shoe_list):
    #2D list of product names and total value for each shoe in the shoe_list
        #define table headers
            #print using tabulate format
    table = [[shoe.product, float(shoe.cost) * int(shoe.quantity)] for shoe in shoe_list]
    headers = ["Product", "Total Value"]
    print(tabulate(table, headers, tablefmt="pretty"))


def highest_qty(shoe_list):
    #max function with lambda argument to find the shoe with the highest quantity
    highest_qty_shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f"{highest_qty_shoe.product} is the product with the higest quantity ({highest_qty_shoe.quantity}), and is for sale")

#==========Main Menu=============
    #user menu
def main_menu(shoes_list):
    while True:
        print("""\n=========================================
Shoe Inventory System Main Menu
1. Capture shoe data
2. View all shoes
3. Re-stock a shoe
4. Search for a shoe
5. Calculate value per item
6. Display highest quantity item for sale
7. Exit
=========================================\n""")
        choice = input("Enter your choice: ")
        if choice == "1":
            capture_shoes(shoes_list)
        elif choice == "2":
            view_all(shoes_list)
        elif choice == "3":
            re_stock(shoes_list)
        elif choice == "4":
            shoe = search_shoe(shoes_list)
            if shoe:
                print(shoe)
            else:
                print("Shoe not found.")
        elif choice == "5":
            value_per_item(shoes_list)
        elif choice == "6":
            highest_qty(shoes_list)
        elif choice == "7":
            print(".")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#program running, 
    #first reading all shoe data 
        #then running the menu
read_shoes_data(shoe_list)
main_menu(shoe_list)