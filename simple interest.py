#python program to find simple interest

def calculate_si(principle,time,rate):
    return (principle * time * rate)/100

principle = int(input("Enter the principle amount: "))
time = int(input("Enter the time in year: "))
rate = float(input("Enter the rate of interest: "))



print("The simple interest = Rs.", calculate_si(principle,time,rate))




