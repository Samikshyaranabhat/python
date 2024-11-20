a=input("Enter the value of a:")
b=input("Enter the value of b:")
def num(a,b):
        if a > b:
                return(f'{a} is greater than {b}')
        elif a == b:
                return('Both are equal')
        return(f'{b} is greater than {a}')
print(num(a,b))
