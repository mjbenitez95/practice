# You're given strings jewels representing the types of stones that are jewels, 
# and stones representing the stones you have. Each character in stones is a 
# type of stone you have. You want to know how many of the stones you have are 
# also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone 
# from "A".

TEST_CASES = [
    ["aA", "aAAbbbb", 3],
    ["z", "ZZ", 0],
    ["mathew", "abcdefghijklmnopqrstuvwxyz", 6],
]

def jewels_and_stones(jewels, stones):
    ans = 0
    counts = {}

    for stone in stones:
        if stone not in counts:
            counts[stone] = 0

        counts[stone] += 1

    for jewel in jewels:
        if jewel in counts:
            ans += counts[jewel]

    return ans

def jewels_and_stones_pythonic(jewels, stones):
    ans = 0
    for jewel in jewels:
        ans += stones.count(jewel)

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(jewels_and_stones(case[0], case[1]) == case[2], jewels_and_stones_pythonic(case[0], case[1]) == case[2])