'''
프로그래머스
161990 - 바탕화면 정리
'''

'''
". # . . .", 
". . # . .", 
". . . # ."

(칼럼 idx 가장 높은 거) - (칼럼 idx 가장 낮은 거)
(로우 idx 가장 높은 거) - (로우 idx 가장 낮은 거) 

'''

def solution(wallpaper):
    # 목적은 각각 최대, 최소인 값
    # 구하기 위함
    size_row = len(wallpaper)
    size_col = len(wallpaper[0])
    row_list = []
    col_list = []
    for i in range(size_row):
        for j in range(size_col):
            temp = wallpaper[i][j]
            if (temp == '#'):
                row_list.append(i)
                col_list.append(j)
    print("rows:", row_list)
    print("cols:", col_list)
    rows_dict = {row_list[_]:_ for _ in range(len(row_list))}
    cols_dict = {col_list[_]:_ for _ in range(len(col_list))}
    print("rows dict", rows_dict)
    print("cols dict", cols_dict)
    print("min-row-pos", min(row_list))
    print("max-row-pos", max(row_list))
    print("min-col-pos", min(col_list))
    print("max-col-pos", max(col_list))
    min_row = min(row_list)
    max_row = max(row_list)
    min_col = min(col_list)
    max_col = max(col_list)
    answer = [min_row, min_col, max_row+1, max_col+1]
    print(answer)

    return answer


if __name__ == '__main__':
    wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
    solve = solution(wallpaper)