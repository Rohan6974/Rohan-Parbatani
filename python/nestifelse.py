num = int((input("enter the number: ")))

if(num > 0):
    if(num % 2 == 0):
        print("num is positive even number")
    else:
        print("num is positive odd number")
elif(num < 0):
    if(num % 2 == 0):
        print("num is negative even number")
    else:
        print("num is negative odd number")
else:
    print("num is zero")