from collections import deque

def solution(maps):
    n_size = len(maps)
    m_size = len(maps[0])
    visited = [[False for _ in range(m_size)]
               for __ in range(n_size)]
    start = (0, 0)
    result = bfs(maps, start, visited)
    if result == 1:
        answer = -1
    else:
        answer = result
    return answer

# BFS 함수 정의
def bfs(graph, start, visited):
    '''
    # graph : 2차원 배열
    # start = (y, x) = (col, row)
    # visited : 2차원 배열
    '''
    # 큐(Queue) 구현 위해 deque 라이브러리 사용
    queue = deque()
    queue.append(start)
    col = start[1]
    row = start[0]
    # 현재 Node 방문 처리
    visited[col][row] = True
    n_size = len(graph)
    m_size = len(graph[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print("(y, x)")
    # Queue 빌 때까지 반복
    while queue:
        # Queue에서 원소 하나 뽑기
        y, x = queue.popleft()
        print(f"({y}, {x})")
        print()
        for i in range(4):
            ny = y + dx[i]
            nx = x + dy[i]
            print(f"({ny}, {nx})", end=' ')
            if (nx < 0 or nx >= m_size
                or ny < 0 or ny >= n_size):
                continue
            if graph[ny][nx] == 0:
                continue
            if (graph[ny][nx] != 1 and
                    visited[ny][nx] == True):
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                visited[ny][nx] = True
                queue.append((ny, nx))

            print()
            print("------------------------")
            print("result graph\n")
            print('\n'.join([' '.join([str(graph[i][j]) for j in range(m_size)]) for i in range(n_size)]))
            print("------------------------")

    print()
    print("------------------------")
    print("result graph\n")
    print('\n'.join([' '.join([str(graph[i][j]) for j in range(m_size)]) for i in range(n_size)]))
    print("------------------------")
    return graph[n_size - 1][m_size - 1]


if __name__ == '__main__':
    maps = [[1,0,1,1,1],
            [1,0,1,0,1],
            [1,0,1,1,1],
            [1,1,1,0,1],
            [0,0,0,0,1]]
    solution(maps)