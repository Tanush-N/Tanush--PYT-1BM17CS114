def search(a,key,n):
    s=0
    l=n-1
    flag=False
    while(l>=s):
        mid=int((s+l)/2)
        if(a[mid]==key):
            flag=True
            return flag
        elif a[mid]>key:
            l=mid-1
        elif a[mid]<key:
            s=mid+1
    return flag
a=[]
n=int(input("enter no. of elements"))
for i in range(0,n):
    ele=int(input())
    a.append(ele)
key=int(input("enter the key"))
print(search(a,key,n))
