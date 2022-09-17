num=(int(input("Enter a no. to get the factorial : ")))
fact=1
while(num>0):
    fact=(fact*num)
    num=num-1
print('The factorial is : ', fact)