
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = deque()
        lvl_map = {1: root.val}
        level.append((root, 1))
        max_sum = root.val
        while level:
            s = 0
            stage = 0
            for i in range(len(level)):
                node, stage = level.popleft()
                s += node.val
                if node.left:
                    level.append((node.left, stage+1))
                if node.right:
                    level.append((node.right, stage+1))
            max_sum = max(max_sum, s) 
            lvl_map[stage] = s
        return min([x for x in lvl_map.keys() if  lvl_map[x] == max_sum])