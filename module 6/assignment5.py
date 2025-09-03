def filter_even_numbers(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:  # keep only even numbers
            new_list.append(n)
    return new_list


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter_even_numbers(original_list)

print("Original list:", original_list)
print("List with even numbers only:", even_list)