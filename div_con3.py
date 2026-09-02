#Implement findKthLargest(nums: List[int], k: int) -> int and findMinMax(nums: List[int]) ->
#  Tuple[int, int] functions accepting an unsorted array, returning the k-th element and 
# min-max pair.
def findKthLargest(nums, k):
    # Base case
    if len(nums) == 1:
        return nums[0]

    # Sort in descending order
    nums = sorted(nums, reverse=True)

    return nums[k - 1]


def findMinMax(nums):
    # Base case
    if len(nums) == 1:
        return nums[0], nums[0]

    # Divide the array
    mid = len(nums) // 2

    left_min, left_max = findMinMax(nums[:mid])
    right_min, right_max = findMinMax(nums[mid:])

    # Combine results
    minimum = min(left_min, right_min)
    maximum = max(left_max, right_max)

    return minimum, maximum


# Example
nums = [12, 5, 8, 20, 3, 15]

k = 3

print("Array:", nums)
print("3rd Largest Element:", findKthLargest(nums, k))

minimum, maximum = findMinMax(nums)
print("Minimum:", minimum)
print("Maximum:", maximum)