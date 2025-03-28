from typing import Optional, List

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if(not root): return 0

        level = 0
        queue = [root]

        while(queue):
            size = len(queue)

            for i in range(size):
                curr_node = queue.pop(0)

                for child in curr_node.children:
                    queue.append(child)

            level += 1

        return level
