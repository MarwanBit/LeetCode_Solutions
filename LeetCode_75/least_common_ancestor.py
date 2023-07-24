from copy import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        '''
        '''
        self.p_ancestors = []
        self.q_ancestors = []


    def getAncestors(self, root: 'TreeNode', dest: 'TreeNode', ancestorList, depth: int) -> list['TreeNode']:
        '''
        '''
        if root == None:
            ancestorList = []
            return ancestorList
        if root.val == dest.val:
            ancestorList.append((root, depth))
            return ancestorList
        ancestorList.append((root, depth))
        x = self.getAncestors(root.left, dest, copy(ancestorList), depth + 1)
        y = self.getAncestors(root.right, dest, copy(ancestorList), depth + 1)
        x.extend(y)
        return x
        

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        max_depth = 0 
        lowest_common_ancestor = None
        self.p_ancestors = set(self.getAncestors(root, p, [], 0))
        self.q_ancestors = set(self.getAncestors(root, q, [], 0))
        for tup in self.p_ancestors:
            if tup in self.q_ancestors and tup[1] >= max_depth:
                max_depth = tup[1]
                lowest_common_ancestor = tup[0] 
        return lowest_common_ancestor


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2)
    left_child = TreeNode(1)
    right_child = TreeNode(3)
    root.left = left_child
    root.right = right_child
    res = sol.getAncestors(root, left_child, [], 0)
    for x in res:
        print(x[0].val)
    res = sol.lowestCommonAncestor(root, left_child, right_child)
    print(res.val)