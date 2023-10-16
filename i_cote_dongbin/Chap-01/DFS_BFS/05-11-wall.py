from collections import deque


# n, m = map(int, input().split())
n = 5; m = 6

graph = []
graph = [[1, 0, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]
# for i in range(n):
#     graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현



def bfs(x, y):
    # Queue 구현 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # Queue 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0
                    or nx >= n or ny >= m):
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드가
            # 첫 방문인 경우만
            # 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0,0))