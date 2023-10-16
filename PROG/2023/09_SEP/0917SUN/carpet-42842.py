def solution(brown, yellow):
    '''
    관찰 조건1
        n x m(세로)이라 할 때
        n+m = (4+b)/2 이다.
      파생 조건1-1
          세로 길이 m일 때
          brown의 최상/최하 제외 부분은
          2 x (m - 2)이다
          ex) m=3 => 2개
    관찰 조건2
        세로 길이(m)은
        무조건 3 이상이다.
        ( 2일 때는 노랑 영역 성립X )
    관찰 조건3
        [(전체칸수) - (노랑+갈색)]의 값은
        짝수여야 한다.
    제시 조건1
        n >= m이다.
    '''
    n_plus_m = int((4 + brown)/2)
    b_plus_y = brown + yellow

    # 현재 i는 세로길이
    # (n_plus_m - 3) + 1
    for i in range(3, n_plus_m - 2):
        width = n_plus_m - i
        if (width < i):
            continue
        # 노란색 가능한 최댓값
        # (n x m) - brown

        n_x_m = i * width
        if (n_x_m < b_plus_y):
            continue
        if ((n_x_m - b_plus_y) % 2 != 0):
            continue
        else:
            answer = [n_plus_m - i, i]
            break

    return answer

if __name__ == '__main__':
    brown = 104
    yellow = 2
    solution(brown, yellow)