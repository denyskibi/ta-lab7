# Standard Libraries
from typing import List


def load_nodes(file_path: str) -> List[int]:
    with open(file_path, 'r') as file:
        nodes_str = file.readline().strip().split()
        nodes_int = map(int, nodes_str)
        nodes_list = list(nodes_int)
        return nodes_list
