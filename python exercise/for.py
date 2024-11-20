# given the monthly expenses we will print the month number and expense and then in the end we will print total expense.

my_exp = [2300, 1800, 2000, 1000, 2200]
total = 0
for i in range(len(my_exp)):  
    print("Month:" , (i+1), "Expense:", my_exp[i])
    total += my_exp[i]
    print("Total expense is:", total)