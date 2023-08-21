TEST_CASES = [
    [[-4, -3, 0, 1, 10], [0, 1, 9, 16, 100]],
    [[-10, -4, 7, 9], [16, 49, 81, 100]],
    [[-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], [1, 1, 4, 4, 9, 9, 16, 16, 25, 25]],
    [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [0, 1, 1, 4, 4, 9, 9, 16, 16, 25, 25]],
]

def sortedSquares(nums: list[int]) -> list[int]:
    negs = []
    poss = []
    result = []
    
    for num in nums:
        if num < 0:
            negs.append(num)
        elif num > 0: 
            poss.append(num)
        else: 
            result.append(num)
    
    left = len(negs) - 1
    right = 0
    
    while left > -1 and right < len(poss):
        if(abs(negs[left]) < abs(poss[right])):
            result.append(negs[left] * negs[left])
            left -= 1
        else:
            result.append(poss[right] * poss[right])
            right += 1
            
    while left > -1:
        result.append(negs[left] * negs[left])
        left -= 1
        
    while right < len(poss):
        result.append(poss[right] * poss[right])
        right += 1

    return result

# place result values in reverse order, so that negatives
# can be iterated left to right (highest abs() to lowest abs())
def sortedSquaresTwo(nums):
    result = [0] * len(nums)
    left = 0
    right = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            num = nums[left]
            left += 1
        else:
            num = nums[right]
            right -= 1
        result[i] = num * num
    
    return result

if __name__=="__main__":
    for case in TEST_CASES:
        print(sortedSquares(case[0]) == case[1], sortedSquaresTwo(case[0]) == case[1])