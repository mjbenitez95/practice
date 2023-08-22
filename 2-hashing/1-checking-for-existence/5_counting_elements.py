# Given an integer array arr, count how many elements x there are
# such that x + 1 is also in arr. If there are duplicates in arr, 
# count them separately.


TEST_CASES = [
    [[0,1,2,3,4], 4],
    [[0,1,2,3,4,3,2,1,0], 8],
    [[0,1,2,3,4,5,4,3,2,1,0], 10],
    [[0,2,4,2,0], 0],
    [[-1,0,2,0], 1],
    [[-1,0,-1,-1], 3],
    [[1,1,3,3,5,5,7,7], 0]
]

def counting_elements(arr):
    ans = 0
    nums = {}
    
    for num in arr:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1

    for num, count in nums.items():
        if num + 1 in nums:
            ans += count

    return ans

def counting_elements_optimized(arr):
    nums = set(arr)
    ans = 0
    for num in arr:
        if num + 1 in nums:
            ans += 1

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(counting_elements(case[0]) == case[1])