# Standard Libraries
from typing import Optional, List

# Custom Modules
from core.binary_tree import BinaryTree


class TreeUtils:
    def build_tree(self, nodes: List[int]) -> Optional[BinaryTree]:
        """
        Побудова дерева.

        :param nodes:
        :return:
        """
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

    def find_paths_with_sum_from_node(self, node, target_sum, current_path, all_paths) -> None:
        if not node:
            return

        # Step #1: Додаємо поточний вузол до шляху
        current_path.append(node.val)

        # Step #2: Перевіряємо, чи поточний шлях відповідає цільовій сумі
        if sum(current_path) == target_sum:
            all_paths.append(list(current_path))

        # Step #3: Продовжуємо пошук по лівому та правому піддеревам
        self.find_paths_with_sum_from_node(node.left, target_sum, current_path, all_paths)
        self.find_paths_with_sum_from_node(node.right, target_sum, current_path, all_paths)

        # Step #4: Видаляємо поточний вузол з шляху перед поверненням до попереднього вузла
        current_path.pop()

    def find_all_paths_with_sum(self, root, target_sum) -> list:
        all_paths = []

        # Step #1: Запускаємо функцію для кожного вузла як початкової точки шляху
        def find_from_each_node(node):
            if not node:
                return
            self.find_paths_with_sum_from_node(node, target_sum, [], all_paths)
            find_from_each_node(node.left)
            find_from_each_node(node.right)

        find_from_each_node(root)
        return all_paths
