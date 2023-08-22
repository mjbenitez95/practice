TEST_CASES = [
    [[1,1,1,0,0,0,1,1,1,1,0], 2, 6],
    [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10],
]

def max_consecutive_ones(nums, k):
    left = 0
    num_zeroes = 0
    ans = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            num_zeroes += 1
        
        while num_zeroes > k:
            if nums[left] == 0:
                num_zeroes -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(max_consecutive_ones(case[0], case[1]) == case[2])

