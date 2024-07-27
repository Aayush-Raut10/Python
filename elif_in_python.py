#python program demostrating elif conditional statement 
#Getting maks input from user

marks = int(input("Enter the marks = "))

if(marks>=90):
    print(" you got grade A+")

elif(marks>=80 and marks<90):
    print("You got grade A")

elif(marks>=70 and marks<80):
    print("You got grade B+")

elif(marks>=60 and marks<70):
    print("You got grade B")

else:
    print("You should study hard")
