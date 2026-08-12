#implement search(nums: list[int], target: int) -> int and mypow(x: float, n: int) -> 
# float functions taking an integer array/target and base/exponent pairs, returning index 
# and computed value respectively.
def search(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def mypow(x: float, n: int) -> float:
    return x ** n


# Example
nums = [10, 20, 30, 40, 50]
target = 30

print("Index:", search(nums, target))

print("Power:", mypow(2, 5))
print("Power:", mypow(2.5, 3))