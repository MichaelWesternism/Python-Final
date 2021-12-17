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
def foodMenu():
    itemNumber = 1
    for i in food:
        print (f'{itemNumber:2}.{i[0]:20}${i[1]:.2f}')
        itemNumber = itemNumber+1
    print (f"{itemNumber:2}Exit")
    list = int(input())
    if list == itemNumber:
        print ("Exit")
    else:
        itemNumber = 1
        for i in food:
            if list == itemNumber:
                list = i
                return list
        itemNumber = itemNumber+1

def tableMenu():
    print ("1.Select Table")
    print ("2.Add Table")
    print ("3.Remove Table")
    print ("4.Exit")

def itemMenu():
    print ("1.Add Menu Item")
    print ("2.Remove Menu Item")
    print ("3.Exit")
