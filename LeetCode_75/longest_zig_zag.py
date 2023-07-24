from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxLength = 0
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
        0 maps to left, 1 maps to right
        '''
        self.dfs(root)
        return self.maxLength
        
        
    def dfs(self, root:Optional[TreeNode]) -> None:
        '''
        '''
        if root == None:
            return 
        self.rootDFS(root, 0, 0)
        self.rootDFS(root, 1, 0)
        #Recursive step
        self.dfs(root.left)
        self.dfs(root.right)
        
    def rootDFS(self, root:Optional[TreeNode], direction: int, length: int) -> None:
        if root == None:
            return 
        #Handles the logic for zig-zagging and keeping track of the things
        if direction == 1 and root.right:
            length += 1 
            self.maxLength = max(self.maxLength, length)
            self.rootDFS(root.right, 0, length)
        elif direction == 0 and root.left:
            length += 1 
            self.maxLength = max(self.maxLength, length)
            self.rootDFS(root.left, 1, length)
        else:
            return