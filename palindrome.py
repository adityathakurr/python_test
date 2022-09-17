num = int(input("Enter num no. to check : "))
num=int(num)

sum_1=0
temp=num

while(num>0):

    b = num % 10
    sum_1=(sum_1*10)+b
    num= num//10
    

if(temp==sum_1):
    print("This is a palindrome no.")
else:
    print("Not a palindrome no.")
