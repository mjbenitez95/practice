# Given the head of a linked list with an odd number of 
# nodes head, return the value of the node in the middle.

# For example, given a linked list that represents 1 -> 2
#  -> 3 -> 4 -> 5, return 3.

import collections

TEST_CASES = [
    [[1,2,3,4,5], 3],
    [[1,2,7,4,5], 7],
    [[5,1,6,2,8,9,2,3], 2],
    [[5,1,6,2,8,9,2,3,10], 8],
    [[], None],
    [[-1,0,1], 0]
]

def generate_linked_list(arr):
    linked_list = collections.deque()
    for num in arr:
        linked_list.append(num)

    return linked_list

def middle_value(linked_list):
    if len(linked_list) < 1:
        return None

    fast = 0
    slow = 0
    
    while fast + 2 < len(linked_list):
        fast += 2
        slow += 1

    return linked_list[slow]


if __name__ == "__main__":
    for case in TEST_CASES:
        print(middle_value(generate_linked_list(case[0])) == case[1])