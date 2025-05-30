"""from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start: int) -> List[int]:
            n = len(edges)
            dist = [-1] * n
            visited = set()
            curr = start
            d = 0
            while curr != -1 and curr not in visited:
                dist[curr] = d
                visited.add(curr)
                curr = edges[curr]
                d += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        min_dist = float('inf')
        result = -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_d = max(dist1[i], dist2[i])
                if max_d < min_dist:
                    min_dist = max_d
                    result = i
                elif max_d == min_dist and i < result:
                    result = i
        
        return result
"""

from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def traverse(start: int) -> dict:
            dist = {}
            curr = start
            d = 0
            while curr != -1 and curr not in dist:
                dist[curr] = d
                curr = edges[curr]
                d += 1
            return dist

        dist1 = traverse(node1)
        dist2 = traverse(node2)

        min_dist = float('inf')
        result = -1

        for node in set(dist1.keys()).intersection(dist2.keys()):
            max_d = max(dist1[node], dist2[node])
            if max_d < min_dist or (max_d == min_dist and node < result):
                min_dist = max_d
                result = node

        return result
