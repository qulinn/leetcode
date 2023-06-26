from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 2: rotten
        # 1: fresh
        # 0: empty 

        queue = deque()

        # step1: build the initial set of rotten oranges
        fresh = 0
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # mark the round/level
        queue.append((-1, -1))

        # step2: start the rotting process via BFS
        minutes = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # we finish one round of processing
                minutes += 1
                # to avoid the endless loop
                if queue:
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contamnitate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROW > neighbor_row >= 0 and COL > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        return minutes if fresh == 0 else -1