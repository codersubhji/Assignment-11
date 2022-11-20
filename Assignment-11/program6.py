#6. Write a python script to calculate factorial of a given number
num=int(input("Enter any number ...:"))
fact=1
for n in range(1,num+1):
    fact=fact*n
print("Factorial of n number is ...:",fact)    
    
    