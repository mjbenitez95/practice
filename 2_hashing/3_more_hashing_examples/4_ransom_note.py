# Given two strings ransomNote and magazine, return true if 
# ransomNote can be constructed by using the letters from 
# magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

TEST_CASES = [
    ['a', 'b', False],
    ['aa', 'ab', False],
    ['aa', 'aab', True],
    [
        'franklymydearidontgiveadamn', 
        'thereareagreatmanythingswhichidonotknoworconsidermyselftobeverymuchanexpertatbutchiefamongthemisdeath', 
        True
    ],
    [
        'iamlordvoldemort', 
        'tommarvoloriddle', 
        True
    ],
    [
        'theboywholived', 
        'tommarvoloriddle', 
        False
    ],
]

def ransom_note(note, magazine):
    note_letters = {}
    for letter in note:
        if letter not in note_letters:
            note_letters[letter] = 0
        
        note_letters[letter] += 1

    for letter in magazine:
        if letter in note_letters:
            note_letters[letter] -= 1
            if note_letters[letter] == 0:
                note_letters.pop(letter)

    return len(note_letters) == 0

def ransom_note_pythonic(note, magazine):
    for letter in note:
        if magazine.count(letter) < note.count(letter):
            return False

    return True


if __name__=="__main__":
    for case in TEST_CASES:
        print(ransom_note(case[0], case[1]) == case[2], ransom_note_pythonic(case[0], case[1]) == case[2])