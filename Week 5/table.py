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







