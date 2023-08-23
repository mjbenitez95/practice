# A pangram is a sentence where every letter of the English alphabet 
# appears at least once.

# Given a string `sentence` containing only lowercase English letters, 
# return true if `sentence` is a pangram, or false otherwise.


TEST_CASES = [
    ["myveryexcellentmotherjustsentusninepizzas", False],
    ["supercalifragilizticexpialidocious", False],
    ["thequickbrownfoxjumpsoverthelazydog", True],
    ["thequickbrownfoxjumpoverthelazydog", False],
    ["waltzbadnymphforquickjigsvex", True],
    ["altzbadnymphforquickjigsvex", False]
    ["leetcode", False]
]

def pangram(sentence):
    chars = set()
    for char in sentence:
        if char not in chars:
            chars.add(char)

    return len(chars) == 26

if __name__ == "__main__":
    for case in TEST_CASES:
        print(pangram(case[0]) == case[1])