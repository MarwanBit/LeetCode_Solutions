from typing import Optional

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.right = right 
        self.left = left 

class Solution():
    def __init__(self):
        '''
        '''
        self.count = 0
        self.cache = {0:1}
    
    def dfs(self, root: Optional[TreeNode], target_sum: int) -> None:
        '''
        '''
        if root is None:
            return 
        self.dfs(root.left, target_sum)
        self.findPaths(root, target_sum)
        self.dfs(root.right, target_sum)

    def findPaths(self, root: Optional[TreeNode], target_sum: int) -> None:
        '''
        '''
        if root is None:
            return 
        if root.val == target_sum:
            self.count += 1
            self.findPaths(root .left, target_sum - root.val)
            self.findPaths(root.right, target_sum - root.val)

    def sumPaths(self, root: Optional[TreeNode], target_sum: int) -> int:
        '''
        '''
        self.dfs(root, target_sum)
        return self.count
    
    def dfsOpt(self, root: Optional[TreeNode], target_sum: int, current: int) -> int:
        '''
        '''
        if root == None:
            return 
        current += root.val
        oldPathSumQuery = current - target_sum
        self.count += self.cache.get(oldPathSumQuery, 0)
        self.cache[current] = self.cache.get(current, 0) + 1
        self.dfsOpt(root.left, target_sum, current)
        self.dfsOpt(root.left, target_sum, current)
        self.cache[current] -= 1

        

    
    def sumPathsOpt(self, root: Optional[TreeNode], target_sum: int, current: int) -> int:
        '''
        '''
        self.count = 0 
        self.cache = {0:1}
        self.dfsOpt(root, target_sum, 0)
        return self.count
    


if __name__ == "__main__":
    sol = Solution()
    '''
    Test case: 

                    3 
                    / \ 
                    1   3
                     \
                     2
    '''
    root = TreeNode(3)
    left_parent = TreeNode(1)
    left_right_child = TreeNode(2)
    right_parent = TreeNode(3)
    root.left = left_parent 
    root.right = right_parent
    left_parent.right = left_right_child
    print(sol.sumPaths(root, 3))
