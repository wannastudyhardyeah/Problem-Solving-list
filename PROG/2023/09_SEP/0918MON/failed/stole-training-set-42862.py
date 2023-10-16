'''

'''
'''
## reserve의 각 원소 참조해서
    양쪽 끝까지 참조하기

## lost 학생에는
    빌릴 수 있는 개수(속성) 기재
    (이건 최대 2개까지임)
    
## reserve도, lost도 아닌 학생들 존재함!!
'''


def solution(n, lost, reserve):
    stud_list = [Studs(i+1, n, get_train=2)
                    if i+1 in reserve
                    else Studs(i+1, n, get_train=0)
                 for i in range(n)]
    print(list(map(lambda x:stud_list[x].get_train,
                   range(n))
            )
          )

    '''
    # lost 학생들 iteration
     lost 기준에서 순회 돌면서
     양옆 학생 중 reserve인 학생의
     get_train 값이 2일 때만 -1 연산 가능
    '''
    size_lost = len(lost)
    lost_get_cnt = 0
    # stud_list에서의 idx 구하기 위함.
    # idx값 1 차이가 남
    # num = 1이면 stud_idx = 0임
    stud_idx = lost[0] - 1

    # 현재 가리키는 학생의 stud_idx(num-1)
    now_idx = stud_idx
    # 연결된 것 끝까지 순회
    while(True):
        temp_stud = stud_list[now_idx]

        # lost 아닌지 가려내기
        if not (temp_stud.num in lost):
            now_idx += 1
            if (temp_stud.right_frnd == None):
                break
            continue

        # 오른쪽 친구가 없는 건
        # 끝까지 갔다는 거임
        if (temp_stud.right_frnd == None):
            if (temp_stud.left_frnd != None
                and stud_list[temp_stud.left_frnd-1].get_train == 2):
                stud_list[temp_stud.left_frnd - 1].get_train -= 1
                lost_get_cnt += 1
            break

        # 오른쪽 X인 상황 필터링 했으므로
        # 최소한 이거 없는건 보장됨
        if (temp_stud.left_frnd == None):
            if (stud_list[temp_stud.right_frnd-1].get_train == 2):
                stud_list[temp_stud.right_frnd - 1].get_train -= 1
                lost_get_cnt += 1
        # 아래부터는
        # 왼쪽 친구 있는 거 보장됨
        elif (stud_list[temp_stud.left_frnd-1].get_train == 2):
            stud_list[temp_stud.left_frnd - 1].get_train -= 1
            lost_get_cnt += 1
        elif (stud_list[temp_stud.right_frnd-1].get_train == 2):
            stud_list[temp_stud.right_frnd - 1].get_train -= 1
            lost_get_cnt += 1

        now_idx += 1

    answer = n - size_lost + lost_get_cnt

    return answer

class Studs():
    def __init__(self, num: int, n: int, get_train: int):
        self.num = num
        self.n = n
        #   reserve 학생은 2
        # (1이 되면 나눠주기 불가)
        #   lost 학생은 0
        #   둘 다 아닌 학생도 0
        self.get_train = get_train

        if (self.num != 1):
            self.left_frnd = num - 1
        else:
            self.left_frnd = None
        if (self.num != n):
            self.right_frnd = num + 1
        else:
            self.right_frnd = None

    def got_train(self):
        self.get_train = self.get_train + 1

if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]

    solution(n, lost, reserve)