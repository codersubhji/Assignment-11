#1. Write a python script to calculate sum of first N natural numbers
num=int(input("Enter first number..:"))
sum=0
for n in range(1,num+1):
    sum=sum+n
print("sum of n natural is ..:",sum)

