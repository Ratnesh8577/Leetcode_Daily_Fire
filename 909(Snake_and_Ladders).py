class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def get_coordinates(square):
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        visited = set()
        queue = [(1, 0)]  # (current square, number of moves)

        while queue:
            square, moves = queue.pop(0)  # Using list as queue (BFS)
            for i in range(1, 7):  # Simulate dice roll from 1 to 6
                next_square = square + i
                if next_square > n * n:
                    continue
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1  # Not reachable

#Copy code chatgpt
