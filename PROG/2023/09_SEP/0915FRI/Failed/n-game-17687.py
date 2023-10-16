'''
문제 이해하기


- 2진법인 경우
0    1      2       3       4           5
0, / 1, / 1, 0, / 1, 1, / 1, 0, 0, / 1, 0, 1, /

[[구해야 할 것]]

- n진법의 n이 몇이든 간에,
 본질적으로는 십진법 기준으로
 1, 2, 3, ...을 차례대로 말하는 게임.
 따라서 "n의 값에 따라 진법 변환"만 하면 됨.
    (여기서 n 범위: 2 <= n <= 16)
 
 - [for문 <- t(미리구할 숫자개수) 기준] {
        [for문 <- (10진법에서 변환된 n진법 숫자 배열)] {
            이 iteration 횟수는 
            해당 "숫자의 길이"만큼.
        }
    }

    Q. 첫 번째 for문의 기준을 뭘로 잡을까?
      i) t(미리 구할 숫자개수)
        [for문]
        n진법 숫자 배열에서 매 iter마다 [p+m] 참조 
      ii) m(참가인원)
        [while문]
        mod 연산으로 p(튜브순서) 비교
        => 생각해보니 결국 t에 대한 비교 필요

        i)을 해야될 걸로 판단.

'''
from PyQt5.QtCore.QByteArray import size

'''
10진법 숫자 -> N-진수
n: 변환 대상 숫자
q: N진법의 N 숫자
ex) 5를 2진수로 변환 => make~(5, 2)
'''
def make_n_base_num(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 



'''
N-진수 -> 10진법 숫자
n: 변환 대상 숫자
q: N진법의 N 숫자
ex) 2진수 111를 10진수로 변환 => make~(5, 2) = 7
'''
def calcul_to_decnum(n, base):
    sum = 0
    if type(n) == int:
        n = str(n)
    size = len(n)
    
    for i in range(size-1, -1, -1):
        # n[i] * base^(size-i)
        eachnum = int(n[i]) * (pow(base, i))
        sum += eachnum
    
    return sum





'''
해당 숫자까지의
그 숫자 자리수만 같은 수의 개수
ex) 12_(8) => (10 ~ 77) - (10 ~ 12) => 7*8 - 1*3 =56-3=53

abcd_(n)
맨앞자리 -> a개
(b+1)개 / (c+1)개
맨뒷자리 -> (d+1)개
---------------------
n을 str로 받을지, int로 받을지 결정
'''
def each_pos_number(n):
    if type(n) == int:
        to_str = str(n)
    else:
        to_str = n

    size = len(n)
    product_res = 1
    for i in range(size):
        if (i == 0):
            product_res *= int(to_str[i])
        else:
            product_res *= (int(to_str[i])+1)
    return product_res

'''
n 기준으로 해서 자리올림하는 게 나을듯
계속 1씩 더하긴 하는데,
(더한 후 숫자)가 (n-1)이면 
check_idx[] 리스트에 해당 idx 추가
(첫째 자리는 이게 의미없지만
    둘째 자리부터는 의미있음)
if문으로


    ex) 8진법
    0, / 1, / 2, / 3, / 4, / 5, / 6, / 7, / 1, 0 / 1, 1 
'''
def convert_to_n_base(decnum):
    pass


def solution(n, t, m, p):
    answer = ''
    return answer

if __name__ == "__main__":
    n = 2   # 진법
    t = 4   # 미리구할 숫자개수
    m = 2   # 참가 인원
    p = 1   # 튜브 순서(1부터임)
    # solution(n, t, m, p)
    
    dec_num = 0
    all_n_base_list = ""
    while (True):
        converted = make_n_base_num(dec_num, n)
        all_n_base_list += converted
        size_of_n_base_list = len(all_n_base_list)
        if (size_of_n_base_list)
        dec_num += 1
        

    # # fin_pos = p + (t-1)*m
    # fin_pos = 15
    # print("fin_pos:", fin_pos)
    # # 자리수 개수합 구간별로 fin_pos와 비교
    # now_numbers = n
    # iter = 1
    # temp = n-1
    # # fin_pos가 커지는 순간에
    # # now_numbers 그 값 최종값
    # while (fin_pos > now_numbers):
    #     if (iter == 1):
    #         temp += 1
    #     elif (iter == 2):
    #         temp = (n-1)*n*iter
    #     else:
    #         temp = n-1
    #         for j in range(iter-1):
    #             temp *= n
    #         temp *= iter
    #
    #     now_numbers += temp
    #     iter += 1
    # print("now:", now_numbers)

    print(calcul_to_decnum('222', 3))