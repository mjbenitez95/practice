# Given a string s, return the first character to appear twice. 
# It is guaranteed that the input will have a duplicate character.

TEST_CASES = [
    ["matthew", "t"],
    ["jennifer", "n"],
    ["molybdenum", "m"],
    ["meemee", "e"],
    ["ememe", "e"],
    ["emanae", "a"],
]

def multiple_characters(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            return char
        char_dict[char] = 1

if __name__ == "__main__":
    for case in TEST_CASES:
        print(multiple_characters(case[0]) == case[1])