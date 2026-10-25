#Implement strStr(haystack: str, needle: str) -> int using the KMP algorithm and a Randomizer
#  class with getRandom() -> int for stream sampling, accepting text/pattern strings or 
# stream data and returning matching indices or sampled elements.
import random

# Part A: KMP String Matching
def strStr(haystack, needle):
    if needle == "":
        return 0

    m = len(needle)
    n = len(haystack)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            i += 1

    i = j = 0

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == m:
                return i - j
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


# Part B: Randomizer
class Randomizer:
    def __init__(self, stream):
        self.stream = stream

    def getRandom(self):
        selected = None

        for count, item in enumerate(self.stream, start=1):
            if random.randrange(count) == 0:
                selected = item

        return selected


# Main program
print("PART A: KMP String Matching")
haystack = input("Enter text: ")
needle = input("Enter pattern: ")

print("Pattern index:", strStr(haystack, needle))

print("\nPART B: Randomizer")
stream = list(map(int, input("Enter stream elements: ").split()))

randomizer = Randomizer(stream)
print("Randomly selected element:", randomizer.getRandom())