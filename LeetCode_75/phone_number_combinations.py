from collections import deque

class TreeNode():
    def __init__(self, val, children : list[TreeNode]):
        self.val = val
        self.children = children

    def addChildren(self, child : TreeNode):
        if self.children == None:
            self.children = [child]
        else:
            self.children.append(child)


class Solution:
    def treeDFS(self, curr_val, root):
        '''
        '''
        if root == None:
            self.combinations.append(curr_val)
            return 
        elif root.children == None:
            self.combinations.append(curr_val + root.val)
            return
        else:
            for children in root.children:
                self.treeDFS(curr_val + root.val, children)

    def letterCombinations(self, digits: str) -> list[str]:
        self.combinations = []

        letter_map = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        #Our approach is to generate a decision tree and to use
        # this decision tree by applying DFS to it, to generate
        # all of the combinations! 

        q = deque()
        #First we create our root node
        level = -1 
        root = TreeNode("", None)
        top = root
        q.append((root, level))
        if len(digits) == 1:
            next_digit = digits[0]
            for letter in letter_map[int(next_digit)]:
                child = TreeNode(letter, None)
                root.addChildren(child)
        else:
            # We must use a sort of BFS traversal to construct the tree
            while level < len(digits) - 2:
                for i in range(len(q)):
                    root, level = q.popleft()
                    next_digit = digits[level + 1]
                    for letter in letter_map[int(next_digit)]:
                        child = TreeNode(letter, None)
                        q.append((child, level + 1))
                        root.addChildren(child)
        self.treeDFS("", top)
        return [] if self.combinations == [""] else self.combinations


        