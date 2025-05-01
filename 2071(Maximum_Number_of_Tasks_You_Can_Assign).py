from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(k):
            # Take k hardest tasks and k strongest workers
            selected_tasks = tasks[:k]
            selected_workers = SortedList(workers[-k:])
            pills_left = pills

            for i in reversed(range(k)):
                task = selected_tasks[i]
                
                # Try to find a worker who can do it without a pill
                idx = selected_workers.bisect_left(task)
                if idx < len(selected_workers):
                    selected_workers.pop(idx)
                else:
                    # Try with pill
                    if pills_left == 0:
                        return False
                    idx = selected_workers.bisect_left(task - strength)
                    if idx == len(selected_workers):
                        return False
                    selected_workers.pop(idx)
                    pills_left -= 1
            return True

        low, high = 0, min(len(tasks), len(workers))
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result
