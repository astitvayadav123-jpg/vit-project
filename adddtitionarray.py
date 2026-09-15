def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

# Read array elements from the user
numbers = list(map(int, input("Enter array elements separated by spaces: ").split()))

# Call the function
result = calculate_sum(numbers)

# Display the result
print("Sum of array elements:", result)