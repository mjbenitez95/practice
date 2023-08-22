TEST_CASES = [
    [[1, 2, 3, 4, 5],  [1, 3, 6, 10, 15]],
    [[5, 4, 3, 2, 1],  [5, 9, 12, 14, 15]],
    [[-5, -3, -1, 1, 3, 5],  [-5, -8, -9, -8, -5, 0]],
    [[100],  [100]],
    [[-100, 50, 50, 50],  [-100, -50, 0, 50]],
]

def build_prefix_sum(nums):
    ans = [nums[0]]

    for i in range(1, len(nums)):
        ans.append(nums[i] + ans[i-1])

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(build_prefix_sum(case[0]) == case[1])