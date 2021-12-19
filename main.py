import pickle
import os.path
import bill
import menu
table = {}  #{1: bill object, 5: bill object}

#imports file to dict
try:
    if os.path.exists('tableConfig.dictionary'):
        with open('tableConfig.dictionary', 'rb') as tableConfig:
            table = pickle.load(tableConfig)
    else: print ("tableConfig.dictionary does not exist.")
except EOFError:
    print ("Exception, nothing written in file.")

menu.tableMenu()
bool = 0
while bool == 0: #repeats try and except until number value is entered
    try:
        selection = int(input("Enter Selection: "))
        bool = 1
    except ValueError:
        print("Exception, number value must be entered.")

while selection != 4:

    while selection not in range(1, 5): #catches selection out of range
        bool = 0
        while bool == 0: #repeats try and except until number value is entered
            try:
                selection = int(input("Enter Selection in range: "))
                bool = 1
            except ValueError:
                print("Exception, number value must be entered.")


    if selection == 1: #table selection
        if table:
            #prints tables
            print ("Enter Table Number You Want To Select.")
            for i in table.keys():
                print (f"Table  {i}")
            try:
                key = int(input("Table Number: "))

                #utilizing bill class
                menu.itemMenu() #menu items 1-4
                item = int(input("Enter Selection: "))
                while selection not in range(1, 5):
                    selection = int(input("Enter selection in range: "))
                while item != 4:
                    if item == 1:   #add item
                        table[key].add()

                    elif item == 2: #remove item
                        table[key].removeItem()
                    elif item == 3: #printbill
                        table[key].printBill()

                    menu.itemMenu()
                    item = int(input("Enter Selection: "))
                    #exit bill class
            except ValueError:
                print("Exception, number value must be entered.")
            except KeyError:
                print("Exception, table does not exist.")
        else: print("There are no tables.")



    elif selection == 2: #add new table
        try:
            key = int(input("\nEnter table number to add: "))

            name = input("Enter name on table: ")
            seats = input("Enter number of diners: ")
            bool = 0
            for i in table.keys():
                if i == key:
                    print ("\nTable Already Exists.")
                    bool = 1
            if bool == 0:
                table[key] = bill.Bill(name, seats)
                print (f"\nTable {key} has been added.")
        except:
            print ("Exception, Enter number for table.")



    elif selection == 3: #remove existing table
        #prints tables
        print ("Enter Table Number You Want To Select.")
        for i in table.keys():
            print (f"Table  {i}")
        try:
            key = int(input("Table Number: "))
            del table[key]
        except ValueError:
            print("Exception, number value must be entered.")
        except KeyError:
            print ("Exception, Key does not exist.")

    menu.tableMenu()
    bool = 0
    while bool == 0: #repeats try and except until number value is entered
        try:
            selection = int(input("Enter Selection: "))
            bool = 1
        except ValueError:
            print("Exception, number value must be entered.")


#exports dict to file
if os.path.exists('tableConfig.dictionary'):
    with open('tableConfig.dictionary', 'wb') as tableConfig:
        pickle.dump(table, tableConfig)
else: print ("tableConfig.dictionary does not exist.")
