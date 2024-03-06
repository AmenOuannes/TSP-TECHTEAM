from typing import Tuple, List, Union
from generate_data.py import *
import numpy as np


class TSP:
    def __init__(
            self,
            adjacency_matrix: np.ndarray,
    ):
        self.adjacency_matrix = adjacency_matrix

    def get_solution(self) -> Union[Tuple, List[int], np.ndarray]:
        path = np.random.permutation(self.adjacency_matrix.shape[0])
        cycle = np.concatenate((path, [path[0]]))
        return cycle

    def get_path_cost(self, cycle: Union[Tuple, List[int], np.ndarray]) -> float:
        cost = 0
        for i in range(len(cycle) - 1):
            cost += self.adjacency_matrix[cycle[i], cycle[i + 1]]
        cost += self.adjacency_matrix[cycle[-1], cycle[0]]
        return cost

