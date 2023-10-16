'''
실전 문제: 부품 찾기
'''
def solution(n, n_list, m, m_list):
    origin_list = n_list
    size_origin = n


    start = 0
    end = n - 1
    query_list = m_list
    size_target = m

    origin_list.sort()

    for i in query_list:
        result = bin_search(origin_list, i, 0, n - 1)
        if result != None:
            print('yes', end=' ')
        else:
            print('no', end=' ')

def bin_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

    answer = []

    return answer

if __name__ == '__main__':
    # 매장 부품 개수
    n = 5   # 1 <= n <= 10^6
    # 매장 부품 번호
    # 1 < n_list[i] <= 10^6
    n_list = [8, 3, 7, 9, 2]
    
    # 손님 요청 부품 개수
    m = 3
    # 손님 요청 부품 번호
    m_list = [5, 7, 9]
    
    solve = solution(n, n_list, m, m_list)

    print(solve)