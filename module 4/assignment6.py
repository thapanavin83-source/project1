import random

n = int(input("Enter number of random points: "))
inside = 0
count = 0

while count < n:
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    if x*x + y*y < 1:
        inside += 1
    count += 1

print("Approximation of pi:", 4*inside/n)