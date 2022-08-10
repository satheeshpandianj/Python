year = int(input("Enter the year to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Leap Year")
        else:
            print(f"Not Leap Year")
    else:
        print(f"Leap Year")
else:
    print(f"Not Leap Year")
        
    