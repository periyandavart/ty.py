print("Enter the year")
year=input()
if ((year%4==0)and(year%100!=0)):
    print("The year is a leap year")
elif((year%100==0)and(year%400==0)):
    print("The year is a leap year")
elif(year%400==0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")
