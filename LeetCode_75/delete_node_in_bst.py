from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def BinarySearch(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        '''
        if root == None:
            return None
        if root.val == key:
            return root 
        elif key < root.val:
            self.BinarySearch(self, root.left, key)
        elif key > root.val:
            self.BinarySearch(self, root.right, key)

    def leftMostChild(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        '''
        if node != None and node.left != None:
            self.leftMostChild(node.left)
        elif node != None and node.left == None:
            return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        We will split this into two functions,
        the first finds the node findNode(root, key)
        and the second function handles the deletion and subsequent tree rotations
        which need to be done 
        '''
        root_delete = self.BinarySearch(root, key)
        #This step handles to check if the deletion needs to even be done
        if root_delete == None:
            return root 
        #Otherwise we must perform the deletion which is what we need to work
        #on through applying a bunch of tree rotations
        #This case corresponds to the deletion a leaf, in which we just make it none
        if root_delete.left == None and root_delete.right == None:
            root_delete = None 
        #Otherwise we need to deal with the more general case
        elif root_delete.left == None and root_delete.right:
            root_delete = root_delete.right
        elif root_delete.left and root_delete.right == None:
            root_delete = root_delete.left
        elif root_delete.left and root_delete.right:
            A = root_delete.left
            l_c = self.leftMostChild(root_delete.right)
            l_c.left = A
            root_delete = root_delete.right
        return root 