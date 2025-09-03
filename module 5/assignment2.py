numbers = []

while True:
    entry = input("Enter a number: ")
    if entry == "":
        break
    numbers.append(float(entry))


numbers.sort(reverse=True)


print("The greatest numbers in descending order:")
for num in numbers[:5]:
    print(num)