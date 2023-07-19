from typing import Optional

class TreeNode():
    def __init__(self, val=0, left = None, right = None):
        '''
        '''
        self.val = val 
        self.left = left 
        self.right = right


class Solution():
    def isLeaf(self, node: Optional[TreeNode]) -> bool:
        '''
        '''
        if node and (not node.left) and (not node.right):
            return True 
        return False

    def leafSequence(self, root: Optional[TreeNode]) -> list[int]:
        '''
        '''
        if not root:
            return []
        elif self.isLeaf(root):
            return [root.val]
        res = self.leafSequence(root.left)
        res.extend(self.leafSequence(root.right))
        return res
        

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        '''
        leaf_sequence_1 = self.leafSequence(root1)
        leaf_sequence_2 = self.leafSequence(root2)
        return leaf_sequence_1 == leaf_sequence_2
    


if __name__ == "__main__":
    sol = Solution()
    #None Case
    none_node = None
    #leaf case
    leaf = TreeNode(4)
    '''
    Test Case:
                1
                / \ 
                2  3

    '''
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left 
    root.right = right
    print(sol.leafSequence(none_node))
    print(sol.leafSequence(leaf))
    print(sol.leafSequence(root))
    