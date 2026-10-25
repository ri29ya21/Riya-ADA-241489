# Implement lengthOfLIS(nums: List[int]) -> int, accepting an integer array and returning the
#  length of the longest strictly increasing subsequence.
def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = list(map(int, input("Enter array elements: ").split()))

print("Length of LIS:", lengthOfLIS(nums))