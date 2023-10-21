import sys
import heapq as hq

def solution():
    heap_queue = []
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 입력 별도로 받으면 메모리 초과
        one_line_input = map(int, sys.stdin.readline().split())
        for one_input_val in one_line_input:
            # Queue에 들어가는 원소를 n개로 한정
            if len(heap_queue) < n:
                hq.heappush(heap_queue, one_input_val)
            else:
                # 가장 작은 값 참조
                # heappush() 시점에 정렬된 상태
                top_val = heap_queue[0]
                # input값 하나가 이 값보다 크면
                if (top_val < one_input_val):
                    # 해당 가장 작은 값 빼고
                    hq.heappop(heap_queue)
                    # input값 하나를 넣음
                    hq.heappush(heap_queue, one_input_val)

    print(heap_queue[0])

    return;

if __name__ == '__main__':
    # N = int(sys.stdin.readline().strip())
    # list_input = [list(map(int, sys.stdin.readline().split()))
    #             for _ in range(N)]
    #
    # print(list_input)
    solve = solution()
