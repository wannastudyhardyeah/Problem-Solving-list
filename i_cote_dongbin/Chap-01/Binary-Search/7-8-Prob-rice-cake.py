'''
떡 자르기

'''

def solution(n, m, array):
    start = 0
    end = max(array)

    result = 0
    while (start <= end):
        total = 0
        mid = (start + end)
        for x in array:
            # 잘랐을 때의 떡의 총 길이 계산
            if x > mid:
                total += x - mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)
    answer = []

    return answer


if __name__ == '__main__':
    # 떡의 개수
    n = 4
    # 요청한 떡의 길이
    m = 6
    # 떡의 길이
    rices = [19, 15, 10, 17]

    solve = solution(n, m, rices)