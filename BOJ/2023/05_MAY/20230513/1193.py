'''
20230513
BOJ 1193 분수찾기
'''
'''
    (1, 1) -> (1, 2) -> (2, 1) -> (3, 1) 
->  (2, 2) -> (1, 3) -> (1, 4) -> (2, 3) -> (3, 2) -> (4, 1) -> (5, 1) -> (4, 2)
->  (3, 3) -> (2, 4) -> (1, 5) -> (1, 6) -> (2, 5) -> (3, 4) -> (4, 3) -> (5, 2) -> 
    (6, 1) -> (7, 1) -> (6, 2) -> (5, 3) 
->  (4, 4)
'''
import sys

'''
iter_list의 원소의 개수가
    even     =>  분모가 1
        해당 방향 분수들은
        (즉, 기준에서 이전 분수들로 갈려면) 
            '분자' minus
            '분모' plus
    odd      =>  분자가 1
        해당 방향 분수들은
        (즉, 기준에서 이전 분수들로 갈려면)
            '분자' plus
            '분모' minus
'''

def progress(now_pos, now_id, e_or_o, goal, ):
    """
    now_pos:    현재 좌표
    now_id:     현재 인덱스
    e_or_o:     0 if even, 1 elses
    goal:       도착 목표로 하는 인덱스
    """
    if (e_or_o == 0):
        for i in range(now_id - goal):
            now_pos[0] -= 1
            now_pos[1] += 1
    else:
        for i in range(now_id - goal):
            now_pos[0] += 1
            now_pos[1] -= 1
    return now_pos

num_put = int(sys.stdin.readline().rstrip())
sum = 0
iter = 1
iter_list = []
while (sum < num_put):
    sum += iter
    iter_list.append(iter)
    iter += 1
    # print(sum)

len_iter_list = len(iter_list)

# 현재 위치 2-D 좌표값
#   0번째: 분자     /   1번째:  분모
now_pos = [-1, -1]
e_or_o = -1
if (len_iter_list % 2 == 0):
    now_pos[0] = iter_list[len_iter_list - 1]
    now_pos[1] = 1
    e_or_o = 0
else:
    now_pos[0] = 1
    now_pos[1] = iter_list[len_iter_list - 1]
    e_or_o = 1

# print("%d, %d" % (now_pos[0], now_pos[1]))

output = progress(now_pos, sum, e_or_o, num_put)
print (str(output[0]) + "/" + str(output[1]))