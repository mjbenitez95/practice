# Given the head of a linked list, swap every pair of nodes. For 
# example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6, return
# a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.

import collections


TEST_CASES = [
    [[1,2,3,4,5,6], [2,1,4,3,6,5]],
    [[1,2,3,4,5], [2,1,4,3,5]],
    [[1], [1]],
    [[1,2], [2,1]],
    [[], []],
]

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, num):
        node = ListNode(num)
        if self.head == None:
            self.head = node

        if self.tail == None:
            self.tail = node
        else:
            self.tail.next = node

        self.tail = node

    def pop(self):
        if self.head == None:
            return None

        second_to_last_node = self.head
        last_node = self.tail

        while second_to_last_node.next.next:
            second_to_last_node = second_to_last_node.next

        self.tail = second_to_last_node
        second_to_last_node.next = None

        return last_node.val

def generate_linked_list(arr):
    linked_list = LinkedList()
    for num in arr:
        linked_list.push(num)

    return linked_list

def arrayize(linked_list):
    arr = []
    cur = linked_list.head
    
    while cur:
        arr.append(cur.val)
        cur = cur.next

    return arr


def swap_in_pairs(linked_list):
    ans = []

    if linked_list.head == None:
        return ans

    fast = linked_list.head
    slow = linked_list.head

    cur_tail = None

    while slow and slow.next:
        fast = slow.next
        tmp = fast.next
        
        if slow == linked_list.head:
            linked_list.head = fast
        if cur_tail:
            cur_tail.next = fast

        fast.next = slow
        slow.next = tmp
        cur_tail = slow
        slow = tmp

    return arrayize(linked_list)

if __name__ == "__main__":
    for case in TEST_CASES:
        print(swap_in_pairs(generate_linked_list(case[0])) == case[1])