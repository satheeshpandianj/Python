#Write your code below this line 👇
def prime_checker(number):
    # count = 3
    # for num in range(3,number):
    #     if(number % num) == 0:
    #         print(f"It's not a prime number.")
    #         break
    #     else:
    #         count += 1
    # if (count == number):
    #     print(f"It's a prime number.")
    isPrime = True
    for num in range(3,int(number / 2)):
        if(number % num) == 0:
            isPrime = False
    if isPrime:
        print(f"It's a prime number.")
    else:
        print(f"It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
