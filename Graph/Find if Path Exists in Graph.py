from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [source]
        visited = [False] * n # visited[x] -> if x is visited
        visited[source] = True

        while(stack):
            node = stack.pop()

            if(node == destination): return True

            for neighbor in graph[node]:
                if(not visited[neighbor]):
                    visited[neighbor] = True
                    stack.append(neighbor)

        return False

    """
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited = set()):
            print(node, visited)

            if(node == destination): return True

            visited.add(node)

            for neighbor in graph[node]:
                if(neighbor not in visited):
                    if(dfs(neighbor, visited)): return True

            return False

        return dfs(source)
    """

# s = Solution()
# print(s.validPath(4, [[1,2], [2,4],[1,4]], 2, 3))