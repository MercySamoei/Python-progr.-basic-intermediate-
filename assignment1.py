#Code that takes a list of numbers as input and returns the sum of all the even numbers as input.

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

numbers = [2, 7, 39, 6, 33, 87, 3, 8, 10,11,77,80]
print(sum_even_numbers(numbers))
