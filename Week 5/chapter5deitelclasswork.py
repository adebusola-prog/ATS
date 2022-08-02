#5.3 Use a list to solve the following problem: Read in 20 numbers. As each number is read, print
# it only if it is not a duplicate of a number already read
numbers = [1,2,3,4,5,61,2,3,6,7,8,9,4,3,10,45,47,18,19,20]
k = set()
for i in numbers:
    if i not in k:
        k.add(i)
print(k)

# 5.4 Cross-total each row to get the total sales of each product for lastmonth; cross-total each column to get the total sales by salesperson for last month. 
import collections
import tabulate
k = [{"prod1":300, "prod2":400, "prod3":500, "prod4":600, "prod5":700},
      {"prod1":200, "prod2":400, "prod3":600, "prod4":700, "prod5":900},
      {"prod1":100, "prod2":500, "prod3":500, "prod4":800, "prod5":1000},
      {"prod1":300, "prod2":200, "prod3":400, "prod4":900, "prod5":1100}]


cross_addition = collections.Counter()
for i in k:
       cross_addition.update(i)

n = dict(cross_addition)
print(n)
k = list(n.values())
print(k)

sales_person1 = {"prod1":300, "prod2":400, "prod3":500, "prod4":600, "prod5":700}
sales_person2 = {"prod1":200, "prod2":400, "prod3":600, "prod4":700, "prod5":900}
sales_person3 = {"prod1":100, "prod2":500, "prod3":500, "prod4":800, "prod5":1000}
sales_person4 = {"prod1":300, "prod2":200, "prod3":400, "prod4":900, "prod5":1100}


x = list(sales_person1.values()) 
print(sum(x))

y = list(sales_person2.values()) 
print(sum(y))

z = list(sales_person3.values())
print(sum(z))

a = list(sales_person4.values())
print(sum(a))


table_sales = [["", "Prod1", "Prod2", "Prod3", "Prod4", "Prod5", "Total Sales"],
               ["Sales_person1", 300, 400, 500, 600, 700, 2500],
               ["Sales_person2", 200, 400, 600, 700, 900, 2800],
               ["Sales_person3", 100, 500, 500, 800, 100, 2900],
               ["Sales_person4", 300, 200, 400, 900, 1100, 2900],
               ["Total product", 900, 1500, 2000, 3000, 3700]]
print(tabulate.tabulate(table_sales, headers="firstrow", tablefmt="fancy_grid", showindex=False))


#5.5 The Sieve of Eratosthenes) A prime integer is any integer greater than 1 that is evenly divisible only by itself and 1. The Sieve of Eratosthenes is a method of finding prime numbers. It operates

v = []
for i in range(2, 100):
    for j in range(2, i):
            if i % j == 0:
                i = 0
                v.append(i)
            
                break
    else:
        i = 1
        v.append(i)
print(v)



#5.6(Bubble Sort) Sorting data
def bubble_sort(list_a):
    indexing_length = len(list_a)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+ 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1],  list_a[i]


    return list_a
print(bubble_sort([2,3,1,4,5,2,3,7,8,9,12,6,67]))



# #5.7 Binary search
def binary_search(numbers, search_element, Low, High):
    if Low > High:
        return False
    else:
        Mid = (Low + High)//2
        
        if numbers[Mid] == search_element:
            return Mid
        else:
            if search_element < numbers[Mid]:
                return binary_search(numbers, search_element, Low, Mid-1)
            elif search_element > numbers[Mid]:
                return binary_search(numbers, search_element, Mid + 1, High)
            else:
                return -1


search_element = 16
numbers = [2,5,6,8,10,11,13,15,16]
result = binary_search(numbers, search_element, 0, len(numbers)-1)
if result != -1:
    print("Index", result)



# 5.8Create a dictionary of 20 random values in the range 1–99. Determine whether there are any
#duplicate values in the dictionary. (Hint: you may want to sort the list first.
import random
x = {}
for v in range(1,21):
    z = random.randint(1,100)
    x.update({str(z) : z})
# print(x)

val = [value for value in x.values()]
f = set(val)
if len(f) == len(val):
    print("no duplicates")
else:
    print("there are duplicates")


































