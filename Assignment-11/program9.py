"""9. Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)"""
# num=int(input("Enter any number...:"))
# def decimalToBinary(num):
#     if(num>1):
#         decimalToBinary(num//2)
        
#     print(num&2,end=' ') 
    
# if __name__=='__main__' :
#     decimalToBinary(num)  


n= int(input("Enter any number :"))     
s=''
while n:
    s=str(n%2)+s
    n=n//2
print("convert deci to bin without using bin function :",s)  
print()  
    
