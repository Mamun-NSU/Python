# Checking Leap Year

year=int(input("Input year: "))

if year%400==0 and year%100==0:
    print("This is Leap Uear")
elif year%4==0 and year%100!=0:
    print("This is Leap Uear")
else:
    print("NOT Leap Uear")    
        