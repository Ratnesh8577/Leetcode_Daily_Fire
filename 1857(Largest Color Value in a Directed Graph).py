from collections import deque, defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # Step 1: Build the graph and in-degree array
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Step 2: Initialize DP table for color counts
        dp = [[0] * 26 for _ in range(n)]
        queue = deque()

        # Step 3: Add nodes with in-degree 0 to queue
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
            dp[i][ord(colors[i]) - ord('a')] = 1  # Initial color count for the node

        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                for c in range(26):
                    add = 1 if c == ord(colors[neighbor]) - ord('a') else 0
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + add)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            max_color_value = max(max_color_value, max(dp[node]))

        # If not all nodes were visited, there's a cycle
        return -1 if visited < n else max_color_value
    
    
# copy code chatgpt