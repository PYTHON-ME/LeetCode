# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_copy = ret = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                ret_copy.next = l1
                l1 = l1.next
            else:
                ret_copy.next = l2
                l2 = l2.next
            ret_copy = ret_copy.next
        if l1:
            ret_copy.next = l1
        if l2:
            ret_copy.next = l2       
        return ret.next
