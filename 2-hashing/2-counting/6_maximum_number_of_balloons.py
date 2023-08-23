# Given a string text, you want to use the characters of text to 
# form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the 
# maximum number of instances that can be formed.

TEST_CASES = [
    ["nlaebolko", 1],
    ["loonbalxballpoon", 2],
    ["leetcode", 0],
]

def maximum_number_of_balloons(string):
    chars = {}

    for char in string:
        if char in "balloon":
            if char not in chars:
                chars[char] = 0

            chars[char] += 1
    
    if len(chars) != 5 or chars['l'] < 2 or chars['o'] < 2:
        return 0

    min_char_count = chars['b']
    for char, count in chars.items():
        char_count = count
        if char == 'l' or char == 'o':
            char_count = count // 2
        
        min_char_count = min(min_char_count, char_count)

    return min_char_count

if __name__=="__main__":
    for case in TEST_CASES:
        print(maximum_number_of_balloons(case[0]) == case[1])


        
