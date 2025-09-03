number = int(input("Enter an integer: "))
if number < 2:
    print(f"Number {number} is not a prime number")
else:
    isPrime = True
    for i in range(2, number):
        if number % i ==0:
            isPrime = False
    if isPrime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

