from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 Node 방문 처리
    visited[start] = True
    
    # Queue 빌 때까지 반복
    while queue:
        # Queue에서 원소 하나 뽑기
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된
        # 아직 미방문인 원소들을
        # Queue에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True