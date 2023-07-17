from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        This solution is O(n^2) because for each recursive call
        on a linked list of length N we must iterate our prev_end and end pointer
        n-1 and n times respectively
        so we number of computations is N*N + N-1(N-1) + ... + 1(1)

        It is O(N) space complexity because we create these prev_end, end pointers for the 
        N iterations/ recursive calls that we perform, so we can improve alot in both directions
        let's try to come up with some better solutions
        '''
        #Handle the base cases of length 0 and length 1 lists
        if head == None:
            return None
        elif head.next == None:
            return head 
        #Now we handle the case of all the other lists
        prev_end = head 
        end = head
        while prev_end.next.next != None:
            prev_end = prev_end.next
        end = prev_end.next 
        prev_end.next = None 
        end.next = self.reverseList(head)
        return end 
    
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        This solution is O(n^2) because for each recursive call
        on a linked list of length N we must iterate our prev_end and end pointer
        n-1 and n times respectively
        so we number of computations is N*N + N-1(N-1) + ... + 1(1)
        '''
        #Handle the base cases of length 0 and length 1 lists
        if head == None:
            return None
        elif head.next == None:
            return head 
        prev, curr = None, head 
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        return prev