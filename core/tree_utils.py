# Standard Libraries
from typing import Optional, List

# Custom Modules
from core.binary_tree import BinaryTree


class TreeUtils:
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

    def inorder_traversal(self, root: BinaryTree, result=None):
        """
        Обхід дерева внутрішнім порядком.

        :param root:
        :param result:
        :return:
        """
        if result is None:
            result = []

        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.val)
            self.inorder_traversal(root.right, result)

        return result

    def convert_to_bst(self, root: BinaryTree, values):
        """
        Вставка значень у дерево згідно внутрішньому обходу.

        :param root:
        :param values:
        :return:
        """
        if root:
            self.convert_to_bst(root.left, values)
            root.val = values.pop(0)
            self.convert_to_bst(root.right, values)

    def find_leaves(self, root: BinaryTree) -> List[int]:
        """
        Знаходження листків дерева.

        :param root:
        :return:
        """

        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        leaves = self.find_leaves(root.left) + self.find_leaves(root.right)
        return leaves

