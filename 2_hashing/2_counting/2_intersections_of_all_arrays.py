# Given a 2D array nums that contains n arrays of distinct integers,
# return a sorted array containing all the numbers that appear in all n arrays.

# For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return 
# [3, 4]. 3 and 4 are the only numbers that are in all arrays.

TEST_CASES = [
    [[[3,1,2,4,5], [1,2,3,4], [3,4,5,6]], [3,4]],
    [[[1,7,2,5,3], [1,7,2,5,3], [3,4,5,6]], [3,5]],
    [[[1,2,3,4,5], [6,7,8,9,10], [1,2,3]], []],
]

def numbers_in_all_arrays(arrays):
    ans = []
    nums = {}

    for array in arrays:
        for num in array:
            if num not in nums:
                nums[num] = 0
            
            nums[num] += 1

    for num, count in nums.items():
        if count == len(arrays):
            ans.append(num)

    return sorted(ans)

if __name__=="__main__":
    for case in TEST_CASES:
        print(numbers_in_all_arrays(case[0]) == case[1])