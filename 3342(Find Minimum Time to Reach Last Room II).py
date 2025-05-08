import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        return self.dijkstra(moveTime, (0, 0), (len(moveTime) - 1, len(moveTime[0]) - 1))

    def dijkstra(self, moveTime, src, dst):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m)]

        dist[0][0] = 0
        heap = [(0, src)]  # (distance, (x, y))

        while heap:
            d, (i, j) = heapq.heappop(heap)

            if (i, j) == dst:
                return d
            if d > dist[i][j]:
                continue

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    move_cost = (i + j) % 2 + 1
                    new_dist = max(d, moveTime[x][y]) + move_cost
                    if new_dist < dist[x][y]:
                        dist[x][y] = new_dist
                        heapq.heappush(heap, (new_dist, (x, y)))

        return -1
