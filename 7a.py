f1=open("prime.txt","r")
f2=open("happy.txt","r")
a=f1.read()
a.strip()
l1=a.split(",")
b=f2.read()
b.strip()
l2=b.split(",")
c=0
for i in l1:
    if i in l2:
        print(i)
        c+=1
print(c)
