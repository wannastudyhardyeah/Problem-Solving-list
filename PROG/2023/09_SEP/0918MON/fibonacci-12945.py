def solution(n):
    fibo_list = [1, 1, 2]
    if (n <= 3):
        return (fibo_list[n-1] % 1234567)
    i = 3
    while(i < n):
    # for i in range(3, n):
        now_sum_1 = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(now_sum_1)
        i += 1
        if (i == n):
            break
        now_sum_2 = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(now_sum_2)
        i += 1
    answer = fibo_list[n-1] % 1234567
    return answer

'''
def solution(n):
    fibo_list = [1, 1, 2]
    if (n <= 3):
        return (fibo_list[n-1] % 1234567)
    for i in range(3, n):
        now_sum = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(now_sum)
    answer = fibo_list[n-1] % 1234567
    return answer
'''

if __name__ == '__main__':

    n = 100000

    print(solution(n))
