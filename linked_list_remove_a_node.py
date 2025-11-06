class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create dummy node before head
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy

        # Step 2: Move fast ahead by n steps
        for _ in range(n):
            fast = fast.next

        # Step 3: Move both fast and slow until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Step 4: Delete the nth node from end
        slow.next = slow.next.next

        # Step 5: Return the new head
        return dummy.next
