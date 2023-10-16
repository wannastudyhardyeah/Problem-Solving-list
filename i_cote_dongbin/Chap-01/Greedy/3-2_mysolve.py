
    
def solution(N, M, K, num_list):

    num_list = [int(num_list.split(' ')[i])
                for i in range(len(num_list.split(' ')))]
    print(num_list)
    size_nums = len(num_list)
    
    # ({숫자값, 인덱스}, 사용카운트)를 넣음
    # 개별 딕셔너리는 당연히 중복 가능

    a = [(num_list[i], i) for i in range(size_nums)]
    a = sorted(a, reverse=True)
    val_idx_cnt = [[{a[i][0] : a[i][1]}, 0] for i in range(size_nums)]
    print(val_idx_cnt)

    total_cnt = 0
    total_sum = 0
    # val_idx_cnt의 각 원소를
    # 내림차순으로 사용
    # 단, K번 초과 불가
    iter = 0
    
    # 큰값 위주로 더해야 해서
    # iter의 값을 순서대로 넣음
    queue_list = []
    while (total_cnt < M):
        for j in range(len(queue_list)):
            val_idx_cnt[queue_list[0]][1] -= 1
        if (queue_list != []
            and val_idx_cnt[queue_list[0]][1] < K):
            iter = queue_list.pop(0)
            val_idx_cnt[iter][1] = 0

        temp_val = [_ for _ in val_idx_cnt[iter][0]][0]
        total_sum += temp_val
        print("---------------------------------------")
        print(f"더한 값: {temp_val}\n누적합: {total_sum}\n"
              f"현재카운트: {total_cnt}")
        print("---------------------------------------")
        val_idx_cnt[iter][1] += 1
        if val_idx_cnt[iter][1] >= K:
            # 현재 iter값 큐에 올리기
            queue_list.append(iter)
            val_idx_cnt[iter][1] += 1
            iter += 1
            total_cnt += 1
            continue
        total_cnt += 1
    print(total_sum)



    answer = 0

    return answer

if __name__ == '__main__':
    N = 5
    M = 7
    K = 2
    num_list = "3 4 3 4 3"
    solve = solution(N, M, K, num_list)