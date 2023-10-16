def solution(n):
    '''
    일단 가장 가능성 큰 부근은
    각 표현 숫자 개수 = M일 때
    int(n/M)의 부근임.
    ex) 10000을 3개로 => 3333의 부근
        (물론 이건 표현 불가임)
    '''
    # 숫자 몇 개로 표현할지
    howmany_nums = n
    # 표현 가능할 때마다 cnt += 1
    # 자기 자신이 있으므로 무조건 1부터
    repre_cnt = 1
    for i in range(2, howmany_nums+1):
        criteria = n // i

        init_val = criteria + i
        queue = [init_val - j for j in range(i)]
        last_val = queue[-1]
        all_sum = sum(queue)
        if (all_sum == n):
            print(queue)
            repre_cnt += 1
            break

        is_need_to_break = 0
        while (all_sum > n):
            queue.pop(0)
            queue.append(last_val - 1)
            init_val = queue[0]
            last_val = queue[-1]
            if (last_val <= 0):
                is_need_to_break = 1
                break
            all_sum = sum(queue)
            if (all_sum == n):
                print(queue)
                repre_cnt += 1
                break
        if (is_need_to_break == 1):
            break


    answer = repre_cnt

    return answer

if __name__ == '__main__':

    n = 15

    solve = solution(n)
    print(solve)