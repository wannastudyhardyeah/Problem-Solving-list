'''
프로그래머스 - 최솟값 만들기
'''
def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    print(A, B)
    print(sum([i*j for i, j in zip(A,B)]))
    answer = sum([i*j for i, j in zip(A,B)])

    return answer

if __name__ == '__main__':
    A = [1, 4, 2]; B = [5, 4, 4]

    solution(A, B)