# Given an array of strings strs, group the anagrams together.
# For example, given strs = ["eat","tea","tan","ate","nat","bat"], 
# return [["bat"],["nat","tan"],["ate","eat","tea"]].

TEST_CASES = [
    [["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]],
    [["jef", "erg", "bot", "awr", "reh"], [["jef"], ["erg"], ["bot"], ["awr"], ["reh"]]],
    [["jef", "fej", "ejf", "efj", "jfe"], [["jef", "fej", "ejf", "efj", "jfe"]]],
    [["jef", "fej", "ejf", "efj", "jfe"], [["jef", "fej", "ejf", "efj", "jfe"]]],
    [["word", "drow", "bat", "cat", "tab", "of", "foe"], [["word", "drow"], ["bat", "tab"], ["cat"], ["of"], ["foe"]]],
]

def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        key = str(sorted(word))

        if key not in anagrams:
            anagrams[key] = []
        
        anagrams[key].append(word)

    return list(anagrams.values())

if __name__ == "__main__":
    for case in TEST_CASES:
        print(group_anagrams(case[0]) == case[1])