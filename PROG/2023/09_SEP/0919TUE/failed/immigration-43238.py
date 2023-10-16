def solution(n, times):
    '''
    심사관에 대한 배열
    times를 정렬하고 시작
    그 뒤에 큐 리스트처럼 쓰기

    각 심사관 원소에는
    [걸리는시간, 현재 남은시간].
    '현재 남은시간'은
    계속 업데이트 돼야 함
    특히,

    - init
      [0]번의 현재 남은시간만큼
    흐르게 한 뒤
    - progress
      [0]번과 [1]번의 차이만큼
    흐르게 하는 걸 반복
    
    +) 추가 조건
      특정 심사대가 비어도
    (해당 심사대 걸리는시간)이
    다른 진행중 심사대의 
    (남은시간)+(걸리는시간)보다
    크다면
    다른 진행중 심사대로 가도록 함
    ㄴ 이건 sort로 해결이 되었을까??
    '''
    times.sort()
    for_copy = times.copy()
    queue = [
                [for_copy[i], for_copy[i]]
             for i in range(len(times))
            ]
    # 시간 지날때마다
    # 여기에 누적 덧셈
    taken_times = 0

    # 첫 번째를 진행
    pop_elmnt = queue.pop(0)
    #   해당 심사대의
    # (걸리는시간)만큼 더함
    taken_times += pop_elmnt[0]
    #  다시 맨뒷열에 추가
    queue.append(pop_elmnt)
    
    
    '''
    위에처럼 하지말고
    그냥 각 심사대에 idx 매기고,
    해시 테이블 리스트 만들기
    이때, 각 맵핑은
    무식하게 1~10^9 범위가 아니라
    각 심사대 한번 순회해서
    그 시간만큼 하기
    아래처럼 돼야 함
    [7, 7, 7, 9, 9, 10, 10, 12, 12]는
    (분) 7  9 10  12
    (명)[3, 2, 2, 2]
    '''
    #  time_list
    # = {
    #   times[i]: len(times[i])
    #  }
    times_list = {}

    for i in range(len(times)):
        refer_times = times[i]
        try:
            # 각 시간별 명수 누적계산
            times_list[refer_times] += 1
        except:
            times_list[refer_times] = 1
    print(times_list)

    answer = n

    return answer

if __name__ == '__main__':
    n = 6
    times = [7, 10, 7, 8, 100, 90, 8]
    solve = solution(n, times)