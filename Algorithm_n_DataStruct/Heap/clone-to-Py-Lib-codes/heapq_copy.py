
def heapify_copy(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    # Transform bottom-up.
    #   The largest index there's any point to looking at
    # is the largest with a child index in-range,
    # so must have 2*i + 1 < n, or i < (n-1)/2.
    #   If n is even = 2*j,
    # this is (2*j-1)/2 = j-1/2 so j-1 is the largest,
    # which is n//2 - 1.  If n is odd = 2*j+1,
    # this is (2*j+1-1)/2 = j
    # so j-1 is the largest, and that's again (n//2-1.)
    for i in reversed(range(n//2)):
        _siftup_copy(x, i)

def _siftup_copy(heap, pos):
    # 마지막 위치: heap의 길이
    endpos = len(heap)
    # 시작 위치: 현재 위치(인자 pos)
    startpos = pos
    # 현재 위치(시작 위치)의 값을 저장
    newitem = heap[pos]
# Bubble up the smaller child until hitting a leaf.
# 단말 노드에 도달할 때까지,
# 가장 작은 자식 노드를 올린다
    # 왼쪽 자식 노드의 위치 저장
    childpos = 2*pos + 1
    while childpos < endpos:
        # 오른쪽 자식 노드는 왼쪽 idx + 1한 것
        rightpos = childpos + 1
        # 오른쪽 자식 노드 위치가
        # 마지막 위치보다 작고,
        # 왼쪽 자식 노드 값이 오른쪽 자식 노드 값보다
        # 크거나 같을 때
        if (rightpos < endpos
            and
            not (heap[childpos] < heap[rightpos])):
            # 왼쪽 자식 노드 위치를
            # 오른쪽 자식 노드 위치로 갱신
            childpos = rightpos
        # 자식 노드를 위로 올린다
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown_copy(heap, startpos, pos)

def _siftdown_copy(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, 
    # moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        # newitem 값보다
        # 부모 노드의 값이 크면
        if newitem < parent:
            # 현재 위치의 노드 값을
            # 부모 노드의 값으로 변경
            heap[pos] = parent
            # 위치 역시 변경
            pos = parentpos
            # 즉, break가 되지 않음
            # (다음 iterate 실행됨)
            continue
        break
    heap[pos] = newitem


if __name__ == '__main__':
    input_list = [ 9, 100, 2, 3, 1, 23, 43, 13, 12]
    heapify_copy(input_list)
    print(input_list)

'''
                1
            3       2
    9       100   23    43
13    12

'''