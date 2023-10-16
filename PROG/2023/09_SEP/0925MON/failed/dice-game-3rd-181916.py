'''
프로그래머스
181916 - 주사위 게임 3
'''
'''
아마도 여기서 가장 중요해보이는 건
필터링의 단계의 순서를
어떻게 배치하느냐이다.
이것에 따라 코드 길이가 달라질 것 같다.

그런데,
이 주사위 4개에서
주사위의 순서는 상관이 없다.
즉, 주사위에 고유idx 매길 필요가 없다.
=> 그냥 누적 카운트 해도 된다.
'''
def cases(p, q, r, oh, idx):
    if oh != 0:
        return oh, p, q, r
    elif r != 0:
        oh = idx
    elif q != 0:
        r = idx
    else:
        if p != 0:
            q = idx
        else:
            p = idx
    return oh, p, q, r

def swap_if_big_post(p, q):
    if (p < q):
        temp = p
        p = q
        q = temp
    return p, q

def solution(a, b, c, d):
    answer = [a, b, c, d]
    # 숫자 범위가 [1, 6]이므로
    # idx도 1~6에 꼭 맞춤!!
    # idx == 0 사용금지!!
    all_cnt = [0 for _ in range(7)]

    for i in answer:
        all_cnt[i] += 1
    p = 0
    q = 0
    r = 0
    oh = 0
    not_two_num = []
    for idx, j in enumerate(all_cnt):
        if j == 4:
            s = str(idx)
            answer = int(f"{s}{s}{s}{s}"[:])
            return answer
        if j == 2:
            p, q, r, oh = cases(p, q, r, oh, idx)
            if (r != 0):
                answer = not_two_num[0] * not_two_num[1]
                return answer
            elif (q != 0):
                answer = ((p + q) * abs(p-q))
                return answer

        if j == 3:
            p, q, r, oh = cases(p, q, r, oh, idx)
            if q != 0:
                p, q = swap_if_big_post(p, q)
                answer = pow(int(f"{p}{q}"), 2)
                return answer

        if (j == 1):
            p, q, r, oh = cases(p, q, r, oh, idx)
            if oh != 0:
                answer = min(p, q, r, oh)
                return answer
            elif r != 0:
                if not(p != q and q != r and r != p):
                    answer = not_two_num[0] * idx
                    return answer
            elif q != 0:
                p, q = swap_if_big_post(p, q)
                answer = pow(int(f"{p}{q}"), 2)
                return answer
            elif p != 0:
                not_two_num.append(idx)

    calcul_list = [pow(int(f"{p}{q}"), 2),
                    ((p + q) * abs(p-q)),
                   q*r]
    return answer

if __name__ == '__main__':
    abcd_list = [[6, 3, 3, 6], [2, 5, 2, 6], [6, 4, 2, 5]]
    for abcd in abcd_list:
        solve = solution(abcd[0], abcd[1], abcd[2], abcd[3])
        print(f"solve: {solve}")
