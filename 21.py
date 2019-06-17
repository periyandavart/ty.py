x,y,z=map(int,input().split())
if(x>1 and x<=100000):
  a=int((x/2)*(2*y+ (x-1)*z))
  print(a)
