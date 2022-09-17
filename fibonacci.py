from array import array


n=int(input("Enter the position you want to see in fibonacci series : "))
f= [0,1] 
for i in range(2,n+2):
    f.append(f[i-1]+f[i-2])
print(f[n+1])
