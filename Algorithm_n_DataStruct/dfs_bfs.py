from reference import DFS, BFS

if __name__ == "__main__":
  # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
  graph = [
    [],       # 0번
    [2, 3, 8],# 1번
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
  ]
  graph_dfs = graph
  graph_bfs = graph

  # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
  visited_dfs, visited_bfs = [False] * 9, [False] * 9

  print("BFS 실행")
  BFS.bfs(graph_bfs, 1, visited_bfs)
  print("\n")
  print("DFS 실행")
  DFS.dfs(graph_dfs, 1, visited_dfs)

