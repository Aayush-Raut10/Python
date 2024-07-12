#Python program to find the no. of digits in given number using while loop

num = int(input("Enter positive number: "))
count = 0
original_num = num

while(num!=0):
    count = count + 1
   
    num = num//10


print("Total no. of digits in",original_num,"=",count)
