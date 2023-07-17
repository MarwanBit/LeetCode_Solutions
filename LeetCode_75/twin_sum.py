from typing import Optional
from copy import copy, deepcopy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        '''
        '''
        if head == None:
            return None
        elif head.next == None:
            return head
        curr = head 
        prev = None 
        while curr != None:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev
    
    def printLinked(self, head: Optional[ListNode]) -> None:
        '''
        '''
        while head.next != None:
            print(head.val)
            head = head.next
        print(head.val)

    
    def getLength(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return 1 
        return 1 + self.getLength(head.next)

    def copylinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        '''
        copy_head = deepcopy(head)
        copy_curr = copy_head
        while head != None:
            copy_curr.next = deepcopy(head.next)
            copy_curr = copy_curr.next 
            head = head.next
        return copy_head



    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        '''
        if head == None:
            return 0
        elif head.next == None:
            return max(0, head.val)

        #first let's make a copy of the first let
        max_twin_sum = 0
        length = self.getLength(head)
        copy_head = self.copylinkedList(head)
        reversed_copy_head = self.reverseLinkedList(copy_head)
        i_pointer = head
        j_pointer = reversed_copy_head
        print("Initial values:")
        print("i pointer and next:" , i_pointer.val, i_pointer.next.val)
        print("j_pointer and next: ", j_pointer.val, j_pointer.next.val)
        for index in range((length // 2)):
            twin_sum = i_pointer.val + j_pointer.val
            print("current vals: ", i_pointer.val, j_pointer.val)
            print("current twin sum:", twin_sum)
            max_twin_sum = max(max_twin_sum, twin_sum)
            i_pointer = i_pointer.next
            j_pointer = j_pointer.next
        return max_twin_sum
    
    def pairSumOpt(self, head: Optional[ListNode]) -> int:
        '''
        O(N) time, O(1) extra space
        '''
        slow, fast = head, head 
        prev = None 
        while fast and fast.next:
            #This should put the slow at the
            fast = fast.next.next
            temp_slow = slow
            nxt = slow.next
            slow.next = prev
            prev = temp_slow
            slow = nxt 
        res = 0
        while slow:
            res = max(res, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return res
    
    def pairSumIntuitive(self, head: Optional[ListNode]) -> int:
        '''
        T O(n), S O(n)
        '''
        curr = head
        values = []
        while curr != None:
            values.append(curr.val)
            curr = curr.next 
        left, right = 0, len(values) - 1 
        max_sum = 0
        while left < right:
            left_val, right_val = values[left], values[right]
            max_sum = max(max_sum, left_val + right_val)
            left += 1 
            right -= 1 
        return max_sum

    def pairSumStack(self, head: Optional[ListNode]) -> int:
        '''
        T O(n), S O(n)
        '''
        curr = head
        stack = []
        count = 0
        max_sum = 0
        while curr != None:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        count = len(stack)
        i = 0
        while i <= count/2 :
            left_val, right_val = curr.val, stack.pop()
            max_sum = max(max_sum, left_val + right_val)
            curr = curr.next
            i += 1

        return max_sum



if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    node_1 = ListNode(2)
    node_2 = ListNode(3)
    node_3 = ListNode(4)
    head.next = node_1
    node_1.next = node_2 
    node_2.next = node_3 
    node_3.next = None
    copy = sol.copylinkedList(head)
    print("Printing the original list: ")
    sol.printLinked(head)
    print("Printing the copied linked list: ")
    sol.printLinked(copy)
    print("Pair sum!")
    print(sol.pairSum(head))