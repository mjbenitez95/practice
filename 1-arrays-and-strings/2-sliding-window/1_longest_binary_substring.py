TEST_CASES = [
    ["1101100111", 5],
    ["10101001101", 4],
    ["111101111", 9],
    ["001000001000", 2],
]

def longest_binary_substring(binary_string):
    left = 0
    num_zeroes = 0
    max_length = 0

    for right in range(0, len(binary_string)):
        if binary_string[right] == "0":
            num_zeroes += 1

        while num_zeroes > 1:
            if binary_string[left] == "0":
                num_zeroes -= 1
            left += 1


        cur_length = right - left + 1
        max_length = max(max_length, cur_length)

    return max_length

if __name__ == "__main__":
    for case in TEST_CASES:
        print(longest_binary_substring(case[0]) == case[1])

