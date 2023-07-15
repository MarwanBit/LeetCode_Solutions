from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinked(head: Optional[ListNode]) -> None:
    '''
    '''
    while head.next != None:
        print(head.val)
        head = head.next
    print(head.val)


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        '''
        #Base case
        if head == None or head.next == None: 
            return head 
        #beginning of the odd and even sub lists (imagine we're partitioning)
        # the list into two other lists
        head_odd = head 
        head_even = head_odd.next 
        curr_odd = head_odd 
        curr_even = head_even
        while (curr_odd.next != None and curr_odd.next.next != None) or (curr_even.next != None and curr_even.next.next != None):
            #Update curr_odd if you can
            if curr_odd.next != None and curr_odd.next.next != None:
                curr_odd.next = curr_odd.next.next
                curr_odd = curr_odd.next
            else: 
                curr_odd.next = None
            #update cur_even if you can 
            if curr_even.next != None and curr_even.next.next != None:
                curr_even.next = curr_even.next.next
                curr_even = curr_even.next
            else: 
                curr_even.next = None
        #At the end we add the two together
        curr_odd.next = head_even 
        return head_odd

if __name__ == "__main__":
    sol = Solution()
    list_1 = [ListNode(1), ListNode(2)]
    len_1 = len(list_1)
    for index in range(len_1 - 1):
        list_1[index].next = list_1[index + 1]
    list_2 = [ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)]
    len_2 = len(list_2)
    for index in range(len_2 - 1):
        list_2[index].next = list_2[index + 1]
    print(sol.oddEvenList(None))
    printLinked(sol.oddEvenList(ListNode(1)))
    printLinked(sol.oddEvenList(list_1[0]))
    printLinked(sol.oddEvenList(list_2[0]))
    
