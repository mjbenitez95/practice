# Given an integer array nums, return the largest integer
# that only occurs once. If no integer occurs once, return -1.

TEST_CASES = [
    [[5,7,3,9,4,9,8,3,1], 8],
    [[9,9,8,8], -1],
]

def largest_unique_integer(nums):
    nums_present = {}

    for num in nums:
        if num not in nums_present:
            nums_present[num] = 0
        
        nums_present[num] += 1

    unique_integers = []
    for num, count in nums_present.items():
        if count == 1:
            unique_integers.append(num)

    if len(unique_integers) == 0:
        return -1

    return (sorted(unique_integers))[-1]


if __name__=="__main__":
    for case in TEST_CASES:
        print(largest_unique_integer(case[0]) == case[1])