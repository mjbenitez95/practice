TEST_CASES = [
    ['abc', 'abcdefg', True],
    ['abc', 'adefbghic', True],
    ['abc', 'defg', False],
    ['abc', 'abdefg', False],
]

def is_subsequence(substr, main_str):
    left, right = 0, 0
    while left < len(substr) and right < len(main_str):
        if substr[left] == main_str[right]:
            left = left + 1
        right = right + 1
    return left == len(substr)


if __name__ == "__main__":
    for case in TEST_CASES:
        print(is_subsequence(case[0], case[1]) == case[2])

