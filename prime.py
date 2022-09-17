n=int(input("Enter a no. => "))
for i in range(2,n):
    b=n%i
    if(b==0):
        break
    i += 1
if(b==0):
    print("It's not a prime no.")
else:
    print("It is a prime no.")