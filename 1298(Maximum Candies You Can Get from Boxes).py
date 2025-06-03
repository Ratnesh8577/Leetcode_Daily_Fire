from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visited = [False] * n
        haveKeys = set()
        haveBoxes = set(initialBoxes)
        queue = deque()

        # Add initially open boxes to the queue
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        totalCandies = 0

        while queue:
            box = queue.popleft()
            if visited[box]:
                continue

            visited[box] = True
            totalCandies += candies[box]

            # Collect keys and try to open new boxes
            for key in keys[box]:
                if key not in haveKeys:
                    haveKeys.add(key)
                    if key in haveBoxes and not visited[key]:
                        queue.append(key)

            # Discover and queue new boxes
            for newBox in containedBoxes[box]:
                if newBox not in haveBoxes:
                    haveBoxes.add(newBox)
                if (status[newBox] == 1 or newBox in haveKeys) and not visited[newBox]:
                    queue.append(newBox)

        return totalCandies

# Copy code chatgpt
