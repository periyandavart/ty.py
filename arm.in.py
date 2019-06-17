a,b=map(int,input().split())
for x in range(a+1,b):
 sum=0
 temp=x
 while(temp>0):
  digit=temp%10
  sum+=digit**3
  temp=temp//10
 if(x==sum):
  print(x,end=" ")
