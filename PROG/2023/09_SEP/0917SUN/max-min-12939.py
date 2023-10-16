def solution(s):
    print(s.split(' '))
    parsed = s.split(' ')
    print("parsed str-list\n=>", parsed)
    int_converted = [int(parsed[i]) for i in range(len(parsed))]
    be_sorted = sorted(int_converted)
    answer = str(f"{be_sorted[0]} {be_sorted[-1]}")
    return answer

if __name__ == '__main__':
    input_str = "5 -1 2 -3 4"
    solution(input_str)