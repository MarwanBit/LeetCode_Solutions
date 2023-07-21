class TreeNode():
    def __init__(self, val, left = None, right = None):
        '''
        '''
        self.val = val 
        self.left = left
        self.right = right 


class Solution():
    def goodNodes(self, root: TreeNode) -> int:
        '''
        '''
        stack = [[root, root.val]]
        good_count = 0
        while stack:
            for s in stack:
                node, pre_max = stack.pop()
                if pre_max >= max(pre_max, node.val):
                    good_count += 1
                if node.left:
                    stack.append([node.left, max(pre_max, node.val)])
                if node.right:
                    stack.append([node.right, max(pre_max, node.val)])
        return good_count
    
    def goodNodesOpt(self, root: TreeNode) -> int:
        '''
        '''
        good_count = self.goodNodesRecursive(root, root.val)
        return good_count
    
    def goodNodesRecursive(self, root: TreeNode, pre_max: int) -> int:
        '''
        '''
        good_count = 0
        if root.val >= pre_max:
            good_count += 1 
        if root.left:
            good_count += self.goodNodesRecursive(root.left, max(pre_max, root.val))
        if root.right: 
            good_count += self.goodNodesRecursive(root.right, max(pre_max, root.val))
        return good_count



        

if __name__ == "__main__":
    sol = Solution()
    '''
    Test Case:
               3 
            / 
        3 
        / \ 
        4   2
    '''
    root1 = TreeNode(3)
    left_parent = TreeNode(3)
    left_child = TreeNode(4)
    right_child = TreeNode(2)
    root1.left = left_parent
    left_parent.left = left_child 
    left_parent.right = right_child
    #test case:  (1) 
    root2 = TreeNode(1)
    '''
    Test Case: 
                            3 
                            / \ 
                          1     4 
                        /     /    \ 
                      3     1       5
    '''
    root3 = TreeNode(3)
    left_parent = TreeNode(1)
    right_parent = TreeNode(4)
    left_left_child = TreeNode(3)
    right_left_child = TreeNode(1)
    right_right_child = TreeNode(5)
    root3.left = left_parent 
    root3.right = right_parent 
    left_parent.left = left_left_child 
    right_parent.left = right_left_child 
    right_parent.right = right_right_child
    print(sol.goodNodes(root1))
    print(sol.goodNodes(root2))
    print(sol.goodNodes(root3))
    print("attempt with the recursive implementation")
    print(sol.goodNodesRecursive(root1, -1))
    print(sol.goodNodesRecursive(root2, -1))
    print(sol.goodNodesRecursive(root3, -1))
