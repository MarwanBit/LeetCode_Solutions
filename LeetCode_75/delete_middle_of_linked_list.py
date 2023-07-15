# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):         
        self.val = val
        self.next = next



def getLength(head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next == None:
        return 1 
    return 1 + getLength(head.next)

def printLinked(head: Optional[ListNode]) -> None:
    '''
    '''
    while head.next != None:
        print(head.val)
        head = head.next
    print(head.val)

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        '''
        length = getLength(head)
        if length % 2 == 1:
            target_index = int(((length - 1) / 2) - 1)
            targetNode = head
            for i in range(0, target_index):
                targetNode = targetNode.next
            temp = targetNode.next 
            targetNode.next = targetNode.next.next
            temp.next = None
        else: 
            target_index = int(((length) / 2) - 1)
            targetNode = head
            for i in range(0, target_index):
                targetNode = targetNode.next
            temp = targetNode.next 
            targetNode.next = targetNode.next.next
            temp.next = None

        return head


if __name__ == "__main__":
    #this creates the first example linked list
    head_0 = ListNode(1)
    node_1 = ListNode(3)
    node_2 = ListNode(4)
    node_3 = ListNode(7)
    node_4 = ListNode(1)
    node_5 = ListNode(2)
    node_6 = ListNode(6)
    head_0.next = node_1 
    node_1.next = node_2 
    node_2.next = node_3 
    node_3.next = node_4 
    node_4.next = node_5 
    node_5.next = node_6 
    #This is the next example linked list 
    head_0_1 = ListNode(1)
    node_1_1 = ListNode(2)
    node_2_1 = ListNode(3)
    node_3_1 = ListNode(4)
    head_0_1.next = node_1_1
    node_1_1.next = node_2_1
    node_2_1.next = node_3_1


    sol = Solution()
    print(sol.deleteMiddle(head_0))
    print(sol.deleteMiddle(head_0_1))
