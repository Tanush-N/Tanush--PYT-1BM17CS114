n=int(input("enter a number"))
for i in range(1,int(n/2)+1):
    if(n%i==0):
        print(i)
print(n)
