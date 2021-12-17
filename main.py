import bill
import menu
table = {}

menu.tableMenu()
selection = int(input())

while selection != 4:
    if selection == 1:
        print ("Enter Table Number You Want To Select.")
        for i in table.keys():
            print (f"Table  {i}")
        key = int(input())

        #use class
        menu.itemMenu()
        item = int(input())
        while item != 3:
            if item == 1:
                list = bill.Bill.foodMenu()
                print (list)
            menu.itemMenu()
            item = int(input())




    if selection == 2:
        print ("Enter Table Number To Add.")
        key = int(input())
        bool = 0
        for i in table.keys():
            if i == key:
                print ("Table Already Exists.")
                bool = 1
        if bool == 0:
            table[key] = None
            print (f"Table {key} has been added.")



    if selection == 3:
        print ("Enter Table Number To Remove.")
    menu.tableMenu()
    selection = int(input())

print (table)
