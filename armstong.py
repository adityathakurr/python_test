a=int(input("Enter a no. to check where it is an Armstong no. or not : "))
b=0
temp=a
while(a>0):
    i=a%10
    b=b+(i** 3)
    a=a//10
if(temp==b):
    print("This is an Armstrong No.")
else:
    print("This is not an Armstrong No.")
