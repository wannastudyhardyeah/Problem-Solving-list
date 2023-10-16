def solution(n, m, k, data):

    data = list(map(int, data.split()))

    data.sort()

    first = data[n-1]
    second = data[n-2]

    result = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1
    answer = result

    return answer

if __name__ == '__main__':
    N = 5
    M = 7
    K = 2
    num_list = "3 4 3 4 3"
    solve = solution(N, M, K, num_list)
    print(solve)