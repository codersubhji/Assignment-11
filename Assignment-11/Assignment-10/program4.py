#4. Write a python script to print first N odd natural numbers
num=int(input("Enter any number ..."))
for n in range(1,num+1):
    print(2*n-1,end=" ")