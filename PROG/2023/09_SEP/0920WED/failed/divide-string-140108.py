
def solution(s):

    first_chr = s[0]
    cnt_fir_chr = 1

    cnt_other_chr = 0

    # 분리된 문자열 개수 누적
    cumul_cnt = 0
    # 첫 글자는 참조했으므로
    # 1부터 시작
    i = 1
    if (i == len(s)):
        cumul_cnt += 1
        answer = cumul_cnt
        return answer
    while (i != len(s)):
        temp = s[i]
        if (temp == first_chr):
            cnt_fir_chr += 1
        else:
            cnt_other_chr += 1
        if (cnt_fir_chr != 0
            and cnt_other_chr != 0
            and cnt_fir_chr == cnt_other_chr):
            if (i+1 == len(s)):
                cumul_cnt += 1
                break
            print("len(s):", len(s))
            print("i:", i)
            s = s[-(len(s)-i-1):]
            print(s)

            cumul_cnt += 1
            first_chr = s[0]
            cnt_fir_chr = 1
            cnt_other_chr = 0
            i = 1
            if (i == len(s)):
                cumul_cnt += 1
                break
        else:
            i += 1
    print(cumul_cnt)



    answer = []

    return answer

if __name__ == '__main__':
    s = ["banana",
         "abracadabra",
         "aaabbaccccabba"]
    for i in range(len(s)):
        solve = solution(s[i])
        print(solve)