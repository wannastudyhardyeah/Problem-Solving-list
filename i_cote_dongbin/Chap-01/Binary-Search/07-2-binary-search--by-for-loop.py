'''''''''
이진탐색(반복문 이용)

위치 나타내는 변수 3개 사용
=> 시작점, 끝점, 중간점

'''''''''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점 값보다
        # 찾고자 하는 값 작은 경우
        # 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
    
    # n: 원소의 개수
    # targe: 찾고자 하는 문자열

import random as rd

if __name__ == '__main__':
    # array = list(map(int, input().split()))
    array = [rd.randint(1, 100) for _ in range(50)]
    target = 5
    array.sort()
    print(array)
    n = len(array)
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("there is not elmnt you wanna find")
    else:
        print(result + 1)


