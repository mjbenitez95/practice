# Example 1: You are given a string s and an integer k. 
# Find the length of the longest substring that contains
# at most k distinct characters.

# For example, given s = "eceba" and k = 2, return 3. The
# longest substring with at most 2 distinct characters is "ece".

TEST_CASES = [
    ["eceba", 2, 3],
    ["ecebaaaa", 1, 4],
    ["abcdefg", 3, 3],
    ["abcdefg", 2, 2],
    ["aabbbccccdefg", 2, 7],
    ["aabbbccccdefg", 3, 9],
    ["aabbbccccdefg", 0, 0],
    ["aabbbccccdefg", 1, 4],
]

def longest_substring(string, num_chars):
    chars = {}
    ans = 0
    left = 0

    if num_chars == 0:
        return 0

    for right in range(len(string)):
        if string[right] not in chars:
            chars[string[right]] = 0

        chars[string[right]] += 1

        while len(chars) > num_chars:
            chars[string[left]] -= 1
            if chars[string[left]] == 0:
                chars.pop(string[left])
            left += 1

        ans = max(ans, right - left + 1)
    
    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(longest_substring(case[0], case[1]) == case[2])