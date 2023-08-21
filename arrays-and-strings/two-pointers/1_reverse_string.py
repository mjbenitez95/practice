TEST_CASES = [
    [["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]],
    [["H", "E", "l", "L", "O"], ["O", "L", "l", "E", "H"]],
    [["M", "a", "t", "t", "h", "e", "w"], ["w", "e", "h", "t", "t", "a", "M"]],
    [["G", "i", "t", "H", "u", "b"], ["b", "u", "H", "t", "i", "G"]]
]

def reverse_string(s: list[str]) -> None:
    left = 0
    right = len(s) - 1
    
    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1

if __name__=="__main__":
    for case in TEST_CASES:
        reverse_string(case[0])
        print(case[0] == case[1])