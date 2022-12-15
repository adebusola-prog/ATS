def import_and_create_bank(filename):
    bank = {}
     #open file in read mode and read all lines into a list
    f = open("lineno.txt", "r")
    lines = f.readlines()

    for line in lines:

        #strip whitespace from beginning and end of line
        #split into a list based on comma separator
        lst = line.strip().split(":")

        #skip line if missing value (expense amount)
        if len(lst) <= 1:
            continue

        #get key (name) and value (expense amount) from list
        key = lst[0].strip()
        value = lst[1].strip()

        try:
            #cast value to float
            value = float(value)

            #add new expense amount to current total expense amount
            #associated with key (name), or 0
            #associate the new total expense amount with key (name)
            bank[key] = bank.get(key, 0) + value

        except:
            #otherwise go to top of for loop, to next line in list of lines
            continue

    f.close()

    return bank

print(import_and_create_bank("lineno.txt"))