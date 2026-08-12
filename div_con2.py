#design a sort class containing merge_sort(arr:list[int]) -> list[int] and 
# quick_sort(arr:list[int]) ->list[int] methods that accept an unsorted integer array
#  and return the sorted array.
class Sort:

    # Merge Sort
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # Quick Sort
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)


# Example
obj = Sort()

arr = [8, 3, 5, 1, 9, 2, 7]

print("Original Array:", arr)
print("Merge Sort:", obj.merge_sort(arr))
print("Quick Sort:", obj.quick_sort(arr))