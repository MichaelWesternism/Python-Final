class Bill:


    def __init__(self, name, seats):
        self.items = []   #[ ["beer",7] , ["wine",10] ]
        self.total = 0  #bill total
        self.name = name
        self.seats = seats

    def __str__(self):
        return f"{self.name} owes ${self.total}"


    def add(self):
        #food list with price
        food = [
            ['NY Strip', 39],
            ['Duck Breast', 28],
            ['Pork Chop', 28],
            ['Short Ribs', 27],
            ['Salmon', 26],
            ['Chicken Statler', 25],
            ['Lobster Mac', 24],
            ['Butternut Squash', 22],
            ['Beer', 7],
            ['Wine', 10],
            ['Martini', 15]
        ]

        #prints food list
        itemNumber = 1  #keeps track of food index
        for i in food:
            print (f'{itemNumber:2}.{i[0]:20}${i[1]:.2f}')
            itemNumber = itemNumber+1
        print (f"{itemNumber:2}.Exit")

        try:
            #add selected item to item list
            list = int(input("Add Menu Item:"))
            if list == itemNumber:
                print ("Exit")
            else:
                self.items.append(food[list-1])
                self.total = self.total + food[list-1][1]  #adds to bill total
        except IndexError:
            print ("Exception, index out of range.")
        except ValueError:
            print("Exception, number value must be entered.")


    #removes item from table
    def removeItem(self):
        itemNumber = 1
        for i in self.items:  #prints current items on table
            print (f"{itemNumber:2}.{i[0]:20}${i[1]:.2f}")
            itemNumber = itemNumber + 1
        try:
            list = int(input("Remove Menu Item:"))
            remove = self.items.pop(list-1)
            print (f"{remove[0]} was removed.")
            self.total = self.total - remove[1] #subtracts bill total
        except IndexError:
            print ("Exception, index out of range.")
        except ValueError:
            print("Exception, number value must be entered.")



    #prints bill items and total
    def printBill(self):
        print (f"\n{self.seats} diners under {self.name}")
        for i in self.items:
            print (f"{i[0]:20}${i[1]:.2f}")
        print (f"Total Bill: ${self.total:.2f}")
