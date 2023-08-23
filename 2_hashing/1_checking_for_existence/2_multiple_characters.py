# Given a string s, return the first character to appear twice. 
# It is guaranteed that the input will have a duplicate character.

TEST_CASES = [
    ["matthew", "t"],
    ["jennifer", "n"],
    ["molybdenum", "m"],
    ["meemee", "e"],
    ["ememe", "e"],
    ["emanae", "a"],
    ["abcdefghijkl", ""],
]

def multiple_characters(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            return char
        char_dict[char] = 1

    return ""

def multiple_characters_set(string):
    chars = set()
    for char in string:
        if char in chars:
            return char
        chars.add(char)

    return ""

if __name__ == "__main__":
    for case in TEST_CASES:
        print(multiple_characters(case[0]) == case[1], multiple_characters_set(case[0]) == case[1])