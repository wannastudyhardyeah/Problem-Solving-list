"""
문제: 음료수 얼려 먹기

예시)
    4 * 5 얼음 틀

    0 0 1 1 0
    0 0 0 1 1
    1 1 1 1 1
    0 0 0 0 0
    => 총 3개의 아이스크림 생성
"""
# from reference import BFS, DFS


def solution():
    # n: 세로 N // m: 가로 M
    # n, m = map(int, input().split())
    n, m = 3, 3
    # 2차원 리스트
    graph = []
    # for i in range(n):
    #     graph.append(list(map(int, input())))
    # graph = [[0, 0, 1, 1, 0],
    #          [0, 0, 0, 1, 1],
    #          [1, 1, 1, 1, 1],
    #          [0, 0, 0, 0, 0]]
    graph = [[0, 0, 1],
             [0, 1, 0],
             [1, 0, 1]]

    def dfs(x, y):
        # 주어진 범위 벗어나면 바로 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        # 미방문 Node는
        if graph[x][y] == 0:
            # 방문 체크
            graph[x][y] = 1
            # 상, 하, 좌, 우
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                print(i, j)
                result += 1
    print(result)

if __name__ == '__main__':
    solution()

