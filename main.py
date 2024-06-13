# Standard Libraries
import sys
import traceback

# Custom Modules
from utils import file_utils
from core.tree_builder import TreeBuilder
from core.binary_tree import BinaryTree


def stop():
    sys.exit(1)


def main():
    # Create necessary class objects
    tree_builder = TreeBuilder()

    try:
        # Step #1: Load nodes from the file
        loaded_nodes = file_utils.load_nodes(file_path="files/input_1000a.txt")

        # Step #2: Create a binary tree using loaded nodes
        tree_root = tree_builder.build_tree(nodes=loaded_nodes)

        ...
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed: unexpected exception: {e}")
        traceback.print_exc()  # traceback included


if __name__ == '__main__':
    main()
