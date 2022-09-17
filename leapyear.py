a=int(input("Enter a Year => "))
if(a%4==0 and (a%100!=0 or a%400==0)):
    print("This year is a leap year")
else:
    print("Not a leap year")