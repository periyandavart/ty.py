n = input();
num = int(n);
tot = 0;
temp = num;
while temp > 0:
        dig = temp % 10;
        tot += dig ** 3;
        temp //= 10;
if num == tot:
    print("yes");
else:
    print("no");
