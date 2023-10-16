import re

def size_of_bin_num(dec_num):
    str_bin_n = bin(dec_num)
    print(str_bin_n)
    p = re.compile("[1]")
    m = p.findall(str_bin_n)
    # print("regexp:", p.findall(str_bin_n))
    # list_parsed = list(map(lambda x: x.span(), m))
    # print("list_parsed:", list_parsed)
    # len_sum = sum([list_parsed[_][1] - list_parsed[_][0] for _ in range(len(list_parsed))])
    len_sum = len(m)
    print("len:", len_sum)
    return len_sum

def solution(n):
    ''''
    그냥 이진수에서 최초 1인 자리에 1(!=0b001)을 더한 뒤에
    1의 개수 차이만큼 0b__1~1 더해주면 됨
    '''
    p = re.compile('[1]+')
    bin_n = format(n, 'b')
    ones = p.findall(bin_n)[-1]
    zero = re.compile('[0]+').findall(bin_n)
    zero_str = zero[-1]
    print("zero", zero[-1])
    print("he", int('0b'+str(ones), 2))
    print(ones)
    size_bin_n = len(bin_n)
    print(bin_n)
    idx_first_zero = -1
    # 01001011100 + 00000000100 + 00000001100
    first = bin_n
    second = ones[-1] + zero_str
    third = ones[-1:] + zero_str
    print(second, third)
    for i in range(size_bin_n-1, -1, -1):
        if (bin_n[i] == '0'):
            idx_first_zero = i
            break
    idx_first_zero = size_bin_n - i
    print("idx", idx_first_zero)
    print(bin(0b1 << (idx_first_zero)))


if __name__ == '__main__':
    n = 8
    solve = solution(n)
    print(solve)