# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in 
# the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Constraints:
#   m == s.length
#   n == t.length
#   1 <= m, n <= 105
#   s and t consist of uppercase and lowercase English letters.
 
# Follow up: Could you find an algorithm that runs in O(m + n) time?

from collections import Counter

TEST_CASES = [
  ["ADOBECODEBANC", "ABC", "BANC"],
  ["a", "a", "a"],
  ["a", "aa", ""],
]

def all_letters_used(substr, target):
    # could be improved with uniqueness
    for char in target:
        if substr.count(char) < target.count(char):
            return False

    return True

def minimum_window_substring(s, t):
    ans = ""
    
    if len(s) < len(t):    
        return ans

    left = 0
    right = len(t)

    # build first window
    substr = s[left:right]

    # check if all letters present
    if all_letters_used(substr, t):
        # case where t is the leftmost substr of s
        return substr
    
    right += 1
    while right <= len(s):
        substr = s[left:right]
        while all_letters_used(substr, t):
            if len(substr) <= len(ans) or ans == "":
                ans = substr
            
            left += 1
            substr = s[left:right]

        right += 1

    # return answer
    return ans

def minimum_window_substring_optimized(s, t):
    # print("Start:", s, t)
    ans = ""
    
    if len(s) < len(t):    
        return ans

    # m
    characters_needed = Counter(t)
    # print('A:', characters_needed)

    left = 0
    right = 0
    while right < len(s):
        # expand window right until all characters are accounted for
        while not all(count <= 0 for count in characters_needed.values()):
            char = s[right]
            if char in characters_needed:
                characters_needed[char] -= 1
            
            right += 1
    
        # shrink window from the left until we need more characters
        while all(count <= 0 for count in characters_needed.values()):
            substr = s[left:right]

            # check if shortest valid substr so far
            if len(substr) < len(ans) or ans == "":
                # if so, replace ans
                ans = substr

            char = s[left]
            if char in characters_needed:
                characters_needed[char] += 1
            left += 1

    return ans

# def minimum_window_substring_best(s, t):
#     tDict = defaultdict(int)
#     for c in t:
#         tDict[c]+=1
#     print(tDict)
#     m,n=len(s),len(t)
#     need=len(tDict)
#     have=0
#     l,r=0,0
#     mS=""
#     ma=float('inf')
#     sDict=defaultdict(int)
#     for r in range(m):
#         # print(sDict)
#         sDict[s[r]]+=1
#         if tDict.get(s[r],-1) == sDict[s[r]]:
#             have+=1
#             # print(have)
#         while have==need and l<=r:
#             if r-l+1<ma:
#                 ma=r-l+1
#                 mS=s[l:r+1]
#             if sDict[s[l]]==tDict.get(s[l],-1):
#                 have-=1
#             sDict[s[l]]-=1
#             l+=1
#     return mS
    


def minimum_window_substring_best(s, t):
    # count letters in t; this is O(n)
    t_counts = Counter(t)
    
    n = len(s)
    # how many character counts have to match, or, how many unique characters in t
    need = len(t_counts)
    
    # how many character counts we currently have that do match
    have = 0

    # initialize left and right pointers
    left, right = 0,0
    
    ans = ""
    len_ans = float('inf')
    s_counts = Counter()

    # for character in s; this is O(m)
    for right in range(n):
        # expand the window to the right
        right_char = s[right]
        s_counts[right_char] += 1

        # if adding that character makes our count for that character match the target
        if t_counts.get(right_char, -1) == s_counts[right_char]:
            # increment the number of matching character counts
            have += 1

        # whenever we have as many matching character counts as we need,
        # we have a valid substring solution
        while have == need and left <= right:
            # check if current substr len is better than ans len
            substring_len = right - left + 1
            if substring_len < len_ans:
                # if so, update the answer
                len_ans = substring_len 
                ans = s[left:right+1]

            left_char = s[left]
            
            # if the character we're removing is one in the target,
            if s_counts[left_char] == t_counts.get(left_char,-1):
                # decrement the number of matching character counts
                have -= 1

            # shorten the window from the left
            s_counts[left_char] -= 1
            left += 1

    return ans
        
if __name__ == "__main__":
    for case in TEST_CASES:
        print(minimum_window_substring_best(case[0], case[1]) == case[2])