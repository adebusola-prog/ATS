# x = "mango"
# y = x.islower()
# print(y)

def import_and_create_bank(bank):
    bank = {}
    with open("bank.txt", "r") as f:
        lines = f.readlines()
        # print(lines)
        #to strip line from whitespaces and to also split lines with(:)
        #use the following:
        for line in lines:
            # print(line)
            lst = line.strip().split(":")
            # print(lst)
            #skip line if missing value
            if len(lst) <= 1:
                continue
            # print(lst)
            #convert to a key: value pair
            key = lst[0].strip()
            value = lst[1].strip()
            
            # bank.update([(key,value)])
            # print(bank)
                
            try:
                #cast value to float
                value = float(value)
                bank[key] = bank.get(key, 0) + value

            except:
                continue

        print(bank)

import_and_create_bank("bank.txt")