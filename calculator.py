print('''Enter :
1 => Addition
2 => Subtraction 
3 => Multiplication
4 => Division''')
a=int(input())
b=int(input("Enter 1st operand : "))
c=int(input("Enter 2nd operand : "))
if(a==1):
    print("Sum => ",b+c)
elif(a==2):
    print("Subtraction  => ",b-c)
elif(a==3):
    print("Multiplication => ",b*c)
else:
    print("Division ",b/c)