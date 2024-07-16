#Python program to find the factorial using funtion


num = int(input("Enter any positive integer: "))

def fact(n):
    if(n == 0):
        return 1
    else:
        return n * fact(n-1)

print("The factorial of", num ,"=",fact(num))