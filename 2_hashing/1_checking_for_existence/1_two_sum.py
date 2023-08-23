TEST_CASES = [
    [[1,7,2,9,3,5,4], 13, True],
    [[-4,7,2,9,10,3,1], 6, True],
    [[-4,7,2,9,10,3,1], 14, False],
    [[1,7,2,9,3,5,4], 0, False],
    [[1,7,2,-2,9,3,5,4], 0, True],
]

def two_sum(nums, target):
    num_dict = {}
    for num in nums:
        num_dict[num] = num

    for num in nums:
        if ((target-num) in num_dict) and (num != target / 2):
            return True

    return False

if __name__ == "__main__":
    for case in TEST_CASES:
        print(two_sum(case[0], case[1]) == case[2])