# Standard Libraries
import sys
import traceback

# Custom Modules
from utils import file_utils
from core.tree_utils import TreeUtils


def stop():
    sys.exit(1)


def main():
    # Create necessary class objects
    tree_utils = TreeUtils()

    try:
        # Step #1: Load nodes from the file
        loaded_nodes = file_utils.load_nodes(file_path="files/input_1000a.txt")

        # Step #2: Building a binary tree using loaded nodes
        tree_root = tree_utils.build_tree(nodes=loaded_nodes)

        # Step #3: Converting to BST
        sorted_values = sorted(tree_utils.inorder_traversal(root=tree_root))
        tree_utils.convert_to_bst(root=tree_root, values=sorted_values)

        # Step #4: Get leaves
        tree_leaves = tree_utils.find_leaves(root=tree_root)
        first_three_leaves = ' '.join(map(str, tree_leaves[:3]))
        last_three_leaves = ' '.join(map(str, tree_leaves[-3:]))

        # Step #4: Print root and leaves
        print(f"[INFO] Value in root: {tree_root.val}")
        print(f"[INFO] First three leaves: {first_three_leaves}")
        print(f"[INFO] Last three leaves: {last_three_leaves}")
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed: unexpected exception: {e}")
        traceback.print_exc()  # traceback included


if __name__ == '__main__':
    main()
