# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head:Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return None
            prev = head
            curr = prev.next
            head.next = None
            while curr != None:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        def half(head: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        l2 = half(head)
        ans = 0
        l2 = reverse(l2)
        while l2:
            res = l2.val + head.val
            ans = max(ans, res)
            l2 = l2.next
            head = head.next
        return ans