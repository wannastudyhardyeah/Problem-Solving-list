from collections import deque

def solution(prices):
    '''
    [input]
    prices
        : 초 단위로 기록된 주식가격 담긴 배열
    ==
    [return]
    (list) : 각 가격마다
            그 가격 안 떨어진 시간 몇 초인지 기록
    '''
    '''
    각 가격을 큐에 하나씩 넣어두고
    1초 시간이 지난 시점의 가격이
    떨어졌는지 올랐는지를 체크
    (i) 떨어졌다
     => 이걸 위해서
     미리 "타이머 변수"로 카운트하기
     해당 타이머 변수의 값만큼 측정
     (해당 변수는 리스트로 
      각 가격 값에 하나씩 대응시키기!!)
      ㄴ 왜냐하면
      끝까지 유지되는 경우도 다 카운트해야해서.
    (ii) 올랐다
     => 계속 카운트
    '''
    answer = 0
    return answer



if __name__ == '__main__':
    prices = 0
    solve = solution(prices)
    print(solve)

