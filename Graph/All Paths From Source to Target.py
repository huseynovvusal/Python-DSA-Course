from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start_node = 0
        target_node = len(graph) - 1

        all_paths = []
        initial_path = [start_node]

        self.findPaths(graph, all_paths, initial_path, start_node, target_node)

        return all_paths

    def findPaths(self, graph: List[List[int]], all_paths: List[List[int]], current_path: List[int], current_node: int, target_node: int):
        if(current_node == target_node):
            all_paths.append(current_path.copy())
            return

        for neighbor in graph[current_node]:
            current_path.append(neighbor)
            self.findPaths(graph, all_paths, current_path, neighbor, target_node)
            current_path.pop()