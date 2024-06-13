# Standard Libraries
from typing import Optional, List

# Custom Modules
from core.binary_tree import BinaryTree


class TreeBuilder:
    def __init__(self):
        pass

    def build_tree(self, nodes: List[int]) -> Optional[BinaryTree]:
        if not nodes:
            return None

        val = nodes.pop(0)

        # root = None if val == 0 else TreeNode(val)
        if val == 0:
            root = None
        else:
            root = BinaryTree(val)

        if root:
            root.left = self.build_tree(nodes)
            root.right = self.build_tree(nodes)

        return root
