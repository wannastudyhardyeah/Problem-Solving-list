'''
프로그래머스
12953 - N개의 최소공배수
'''
'''
2 = 1 * 2
6 = 2 * 3
8 = 2^3
14 = 2 * 7

'''

def is_prime(n):
    is_prime_flag = 1
    for i in range(2, int(pow(n, 0.5)) + 1):
        if (n % 2 == 0):
            is_prime_flag = 0
            break
    if (is_prime_flag == 0):
        return False
    return True

'''
각 수마다
sqrt(n) 이하의 약수들을 구하기

'''
def solution(arr):
    arr = sorted(arr)
    len_arr = len(arr)
    divisrs = [
                [0
                for __ in range(0, arr[_] + 1)
                ]
               for _ in range(len_arr)]

    # 약수들을 구하는 부분
    for i in range(len_arr):
        range_num = arr[i]
        if range_num == 2:
            divisrs[i][1] += 1
            continue
        print(f"range_num: {range_num}")
        for j in range(2, range_num + 1):
            divider_temp = range_num
            dividsr_iter = j
            while(True):
                if (dividsr_iter == range_num
                    and is_prime(dividsr_iter) == True):
                    divisrs[i][dividsr_iter - 1] += 1
                    divider_temp = divider_temp // dividsr_iter

                if (divider_temp % dividsr_iter == 0):
                    divisrs[i][dividsr_iter-1] += 1
                    divider_temp = divider_temp // dividsr_iter
                else:
                    break
    print(divisrs)
    # ----약수 구하기 끝----
    
    # 최소공배수 구하기 시작
    num_list = [0 for i in range(0, len(divisrs[-1]))]
    print(f"num_list-before\n: {num_list}")
    len_divisrs = len(divisrs)
    for i in range(len_divisrs):
        # 여기서 숫자 참조할려면
        # (j+1)로!!
        for j in range(len(divisrs[i])):
            cnt_pick = divisrs[i][j]
            if cnt_pick == 0:
                num_list[j] = -1
            if num_list[j] == 0:
                num_list[j] = cnt_pick
            else:
                if (num_list[j] > cnt_pick
                    and cnt_pick != 0
                    and num_list[j] != -1):
                    num_list[j] = cnt_pick

    answer = 1
    for idx, i in enumerate(num_list):
        if i != 0:
            answer *= (int(pow(idx+1, i)))

    print(f"num_list-after\n: {num_list}")
    print(f"answer: {answer}")
    # ----최소공배수 구하기 끝----

    return answer

if __name__ == '__main__':
    # arr = [2, 6, 8, 14]
    arr = [1, 2, 3]
    solve = solution(arr)
    print(solve)