#5. Write a python script to calculate sum of first N even natural numbers
num=int(input("Enter any number..:"))
sum=0
for n in range(1,num+1):
    even=2*n
    sum=sum+even
print("sum of first n even number...",sum)    