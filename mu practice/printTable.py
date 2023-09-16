# Table printer - prints a table with items right justified


def printTable(table):
    justifyList = [] #this list holds the length of the word with the greatest length in each subtable
    for subTable in table: #iterates through each of the subtables in the table
        justifyAmount = 0  #keeps track of the length of the word of the greatest length
        for item in subTable: #iterates through the items in each subtable
            if len(item) > justifyAmount:
                justifyAmount = len(item) #as loop iterates through items, make justifyAmount = the item length if it's bigger
        justifyList.append(justifyAmount) #adds the greatest length to justifyList
    #print(justifyList) #this is just to check I have the right lengths

    for number in range(len(table[0])): #assuming subtable length is same
        tableString = ""  #variable that will be printed total string concatenation
        for justify in range(len(justifyList)): #iterates through length of justify list so each concatenated item has right number
            tableString = tableString + table[justify][number].rjust(justifyList[justify]) + "  "
            #adds justification for each item and a margin
        print(tableString)


tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

printTable(tableData)
