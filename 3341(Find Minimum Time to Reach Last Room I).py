import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        rows = len(moveTime)
        cols = len(moveTime[0])
        
        # Min-heap to store (time, row, col)
        pq = [(0, 0, 0)]  # (time, row, col)
        
        # Directions to move (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Set to keep track of visited rooms
        visited = set()
        
        while pq:
            time, row, col = heapq.heappop(pq)
            
            # If we reach the destination (bottom-right corner)
            if row == rows - 1 and col == cols - 1:
                return time
            
            # Explore all possible neighbors (up, down, left, right)
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within bounds and not visited
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                    # Calculate the time to move to the next room
                    new_time = max(time, moveTime[new_row][new_col]) + 1
                    heapq.heappush(pq, (new_time, new_row, new_col))
                    visited.add((new_row, new_col))
        
        return -1  # If no path is found (though the problem assumes it's always reachable)
