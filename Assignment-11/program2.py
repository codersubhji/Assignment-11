#2. Write a python script to calculate sum of squares of first N natural numbers
num=int(input("Enter any number..:"))
sum=0
for n in range(1,num+1):
    sum=sum+n*n
print(sum,end=" ")