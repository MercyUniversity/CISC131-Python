def two_sum(nums, target):
    indices = {}  # Dictionary to store numbers and their indices
    for i, num in enumerate(nums):
        difference = target - num
        if difference in indices:
            return [indices[difference], i]  # Found the solution
        indices[num] = i  # Store the index of the current number
    return None  # If no solution is found
# Test
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
