n=input()
num=int(n)
orig=num
rev=0
while num>0:
        rev=(rev*10)+num%10
        num//=10
if orig==rev:
    print("yes")
else:
    print("no")
