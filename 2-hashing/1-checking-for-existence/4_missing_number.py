# Given an array nums containing n distinct numbers in the range [0, n]
# return the only number in the range that is missing from the array.

TEST_CASES = [
    [[0,1,2,3,4,5,6,7,8,9,11], 10],
    [[0,1,2,3,4,5,7,8], 6],
    [[0,2,3,4,5,7,8], 1],
    [[1,2,3,4,5,7,8], 0],
    [[0,1,2,3,4,5], 6],
    [[0,1], 2],
    [[0], 1],
    [[1], 0],
    [[-1], 0],
    [[10,9,8,7,6,5,4,3,2,1,0], 11],
    [[5,4,3,1,0], 2],
    [[5,1,2,4,0], 3],
    [[5,1,2,4,3], 0],
]

def missing_number(nums):
    present_numbers = set()
    for num in nums:
        present_numbers.add(num)

    for i in range(len(nums)):
        if i not in present_numbers:
            return i

    return len(nums)

if __name__ == "__main__":
    for case in TEST_CASES:
        print(missing_number(case[0]) == case[1])