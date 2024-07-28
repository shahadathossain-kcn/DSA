def get_squared_numbers(numbers):
    square_numbers = []
    for i in numbers:
        square_numbers.append(i * i)
    return square_numbers

numbers = [1, 2, 3, 4, 5]
p = get_squared_numbers(numbers)
print(p)