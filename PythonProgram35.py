# List as input from user

n = input("Enter  text of numbers : ")
list = n.split()
sum = 0
for num in list:
    sum = sum + int (num)
    print(sum)
