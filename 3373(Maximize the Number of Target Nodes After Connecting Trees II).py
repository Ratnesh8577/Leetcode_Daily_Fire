from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def bfs_parity_count(n: int, edges: List[List[int]]) -> tuple:
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            depth = [0] * n
            visited = [False] * n
            queue = [(0, 0)]  # manual queue: list of (node, depth)
            visited[0] = True

            even_count = 0
            odd_count = 0
            head = 0  # simulate queue

            while head < len(queue):
                node, d = queue[head]
                head += 1
                depth[node] = d
                if d % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, d + 1))

            return depth, even_count, odd_count

        n = len(edges1) + 1
        m = len(edges2) + 1

        depth1, even1, odd1 = bfs_parity_count(n, edges1)
        depth2, even2, odd2 = bfs_parity_count(m, edges2)

        result = []
        for i in range(n):
            parity_i = depth1[i] % 2

            # Case 1: connect to even node in tree2
            case1 = (even2 if parity_i == 0 else odd2) + (even1 if parity_i == 0 else odd1)

            # Case 2: connect to odd node in tree2
            case2 = (odd2 if parity_i == 0 else even2) + (even1 if parity_i == 0 else odd1)

            result.append(max(case1, case2))

        return result

# Copy code in chatgpt