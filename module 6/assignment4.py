def sum_of_list(integers):
    sum = 0
    for number in integers:
        sum += number
    return sum

numbers = [4,5,6]
sum = sum_of_list(numbers)
print(f"The sum of the numbers in the list is: {sum}")