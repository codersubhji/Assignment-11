#4. Write a python script to calculate sum of first N odd natural numbers
num=int(input("Enter any number..:"))
sum=0
for n in range(1,num+1):
    odd=2*n-1
    sum=sum+odd
print(sum)    
    