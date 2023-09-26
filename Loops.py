import math

numbers = [4, 9, 16, 25, 36]

for num in numbers:
    square_root = math.sqrt(num)
    print(f"The square root of {num} is {square_root}")

numbers = [4, 9, 16, 25, 36]

index = 0

while index < len(numbers):
    cubed_value = numbers[index] ** 3

    print(f"The cubed value of {numbers[index]} is {cubed_value}")
    
    index += 1
