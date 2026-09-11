def twoSum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution found

# Take input from the user
nums_input = input("Enter nums (comma-separated, e.g. 2,7,11,15): ")
nums = [int(x.strip()) for x in nums_input.split(",")]

target = int(input("Enter target: "))

result = twoSum(nums, target)
print("Output:", result)