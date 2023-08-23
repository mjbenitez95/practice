TEST_CASES = [
    [
        [1, 2, 3, 4, 5], 
        [[0,3], [0,4], [1,2], [1,4], [2,4]], 
        15, 
        [True, False, True, True, True],
    ],
    [
        [0, 2, 4, 1, 2, 1], 
        [[0,5], [1,4], [2,2], [2,3], [2,5]], 
        7, 
        [False, False, True, True, False],
    ],
]

def queries_by_sum(nums, queries, limit):
    prefix_sum = [nums[0]]
    ans = []

    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i-1])

    for x, y in queries:
        query_sum = prefix_sum[y] - prefix_sum[x] + nums[x]
        ans.append(query_sum < limit)
        
    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(queries_by_sum(case[0], case[1], case[2]) == case[3])