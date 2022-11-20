#8. Write a python script to calculate sum of digits of a given number
num=int(input("Enter any number ....:"))
sum=0
count=0
while(num!=0):
    sum=sum+num%10
    num=num//10

print(sum)    
   