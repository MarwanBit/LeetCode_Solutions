from typing import Optional
from collections import deque

class TreeNode():
    def __init__(self, val, left = None, right = None):
        '''
        '''
        self.val = val 
        self.left = left
        self.right = right 


class Solution():
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        '''
        '''
        #First we handle the base cases 
        if root == None:
            return 0 
        #Now we handle the recursive call 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    #Let's try thig using iterative DFS, recursive DFS, and BFS
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int: 
        '''
        Usually BFS involves a queue, where the BFS has the root in the queue

        ex:

        3, .....
        3?, 9, 20 

        Add the root to the node, afterward, continue popping the queue and adding
        the left and right nodes to the que until we "empty" it out

        Repeat this process until the queue is filled with only "None" items
        '''
        if not root:
            return 0 
        
        level = 0 
        q = deque([root])
        while q: 
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    
    def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        '''
        Implemented using a stack (particularly in-order DFS), there is also
        pre-order DFS/ traversal 
        '''
        
        stack = [[root, 1]]
        res = 0
        while stack: 
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, 1 + depth])
                stack.append([node.right, 1 + depth])
        return res



    

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    left_parent = TreeNode(9)
    right_parent = TreeNode(20)
    right_child = TreeNode(15)
    left_child = TreeNode(7)
    '''
    Visualize this tree as the following

                3
              /   \ 
            9       20 
                /      \ 
            15           7
    '''
    root.left = left_parent
    root.right = right_parent 
    right_parent.left = right_child 
    right_parent.right = left_child 
    print(sol.maxDepth(root))
    