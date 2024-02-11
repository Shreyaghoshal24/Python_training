# Write a Python function that takes a list of integers and finds the list's longest increasing subsequence (LIS). The LIS is the longest subsequence of the list in which the elements are in increasing order.

def longest_increasing_sequence(nums):
    n = len(nums)
    
    # Initializing dynamic programming table
    dp = [1] * n

    # Iterating over each element of nums
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Initializing an empty list to hold the LIS
    lis = []
    max_len = max(dp)

    # Backtracking from the maximum value of dp to find the LIS
    i = dp.index(max_len)
    lis.append(nums[i])

    for j in range(i-1, -1, -1):
        if nums[j] < nums[i] and dp[j] == dp[i] - 1:
            lis.append(nums[j])
            i = j

    return lis[::-1]

# Example
nums = [10, 22, 9, 33, 21, 50, 41, 60,77,81, 77]
print(longest_increasing_sequence(nums))
