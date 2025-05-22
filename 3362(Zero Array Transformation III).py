import heapq

class Solution:
    def maxRemoval(self, nums, queries):
        n = len(nums)
        queries.sort(key=lambda x: x[0])  # sort by l

        query_index = 0
        available = []  # max-heap for available r's (use negative values)
        running = []    # min-heap for running r's

        for i in range(n):
            # Add all queries starting at or before i to available (as max-heap)
            while query_index < len(queries) and queries[query_index][0] <= i:
                r = queries[query_index][1]
                # Python heapq is min-heap, so push negative for max-heap behavior
                heapq.heappush(available, -r)
                query_index += 1

            # Remove expired queries from running (those with r < i)
            while running and running[0] < i:
                heapq.heappop(running)

            # Ensure nums[i] is covered by enough running queries
            while nums[i] > len(running):
                if not available or -available[0] < i:
                    return -1
                r = -heapq.heappop(available)
                heapq.heappush(running, r)

        # Remaining in available are removable queries
        return len(available)
