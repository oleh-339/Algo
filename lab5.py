from collections import deque

def bfs(matrix, start_row, start_col, visited):
    rows = len(matrix)
    cols = len(matrix[0])
    
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if matrix[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

def count_islands(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    islands_count = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                bfs(matrix, r, c, visited)
                islands_count += 1

    return islands_count
