#Python program to find the average of the list

marks = [10,20,85,96,78,89] #marks is a list

sum = 0

for i in marks:
    sum = sum + i


n = len(marks)

average = sum / n

print("Average = ",average)

