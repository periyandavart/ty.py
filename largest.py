print("Enter the three numbers");
n1=input();
n2=input();
n3=input();
largest = n1
if largest < n2:
        if n2 > n3:
            print(n2,"is largest")
        else:
            print(n3,"is largest")
elif largest < n3:
        if n3 > n2:
            print(n3,"is largest")
        else:
            print(n2,"is largest")
else:
        print(n1,"is largest")
    
