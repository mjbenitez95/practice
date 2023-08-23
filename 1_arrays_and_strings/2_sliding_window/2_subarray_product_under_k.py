TEST_CASES = [
    [[10, 5, 2, 6], 100, 8],
]

def subarray_product_under_k(nums, k):
    left = 0
    product = 1
    num_subarrays = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product /= nums[left]
            left += 1

        num_subarrays += (right - left + 1)

    return num_subarrays

if __name__ == "__main__":
    for case in TEST_CASES:
        print(subarray_product_under_k(case[0], case[1]) == case[2])

