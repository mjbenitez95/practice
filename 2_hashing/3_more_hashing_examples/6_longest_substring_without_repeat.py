# Given a string s, find the length of the longest substring without repeating characters.

TEST_CASES = [
    ['aabbccddefg', 4],
    ['abcdefg', 7],
    ['abcdeefg', 5],
    ['abcddefg', 4],
    ['a', 1],
    ['', 0],
    ['aaa', 1],
]

def longest_substring_without_repeat(s):
    left = 0
    letters = {}
    ans = 0

    for right, letter in enumerate(s):
        if letter not in letters:
            letters[letter] = 0

        letters[letter] += 1

        while letters[letter] > 1:
            letters[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans

if __name__=="__main__":
    for case in TEST_CASES:
        print(longest_substring_without_repeat(case[0]) == case[1])



