def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    
    while fast:
        if fast.val != slow.val:
            slow.next = fast
            slow = slow.next
        
        fast = fast.next
        slow.next = None
        
    return head