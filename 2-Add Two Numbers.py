# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result_list = ListNode(0)
        list_tail = result_list

        while l1 or l2 or carry:
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if carry == 1:
                carry = 0
            if value >= 10:
                value = value % 10
                carry = 1

            list_tail.next = ListNode(value)
            list_tail = list_tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result_list.next