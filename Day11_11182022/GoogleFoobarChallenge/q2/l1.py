def find_sublist_with_sum(nums, key):
    left, right = 0, 0
    current_sum = 0

    while right < len(nums):
        current_sum += nums[right]

        while current_sum > key:
            current_sum -= nums[left]
            left += 1

        if current_sum == key:
            return [left, right]

        right += 1

    return [-1, -1]

# Example usage:
nums = [4, 3, 10, 2, 8]
key = 12
result = find_sublist_with_sum(nums, key)
print(result)  # Output: [2, 3]