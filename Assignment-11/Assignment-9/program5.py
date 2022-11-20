#5. Write a python script to print first N odd natural numbers in reverse order
num=int(input("Enter any number to print n odd number...:"))
while(num>=1):
    print(2*num-1,end=" ")
    num-=1