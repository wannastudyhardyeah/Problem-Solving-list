def solution(n, left, right):
    result = []
    for i in range(left, right+1):
        x = i % n
        y = i // n
        which_max = max(x, y)
        result.append(which_max + 1)
    answer = result
    return answer

if __name__ == '__main__':
    n = 4
    left = 7; right = 14
    solution(n, left, right)