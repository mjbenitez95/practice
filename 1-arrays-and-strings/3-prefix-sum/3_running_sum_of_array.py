TEST_CASES = [
    [[1, 2, 3, 4],  [1, 3, 6, 10]],
    [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5]],
    [[3, 1, 2, 10, 1], [3, 4, 6, 16, 17]],
]

def running_sum_of_array(nums):
    ans = [nums[0]]

    for i in range(1, len(nums)):
        ans.append(nums[i] + ans[i - 1])

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(running_sum_of_array(case[0]) == case[1])