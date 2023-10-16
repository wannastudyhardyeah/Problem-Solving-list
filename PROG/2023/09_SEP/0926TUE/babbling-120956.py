'''
프로그래머스
120956 - 옹알이 (1)
'''
import re
'''
정규식을 이용해서
일단 base[]를 토대로 다 sub 대체해보고
대체할 때의 변환 문자는 "_"(언더바)로 한다.
why? - "_" 없이 바로 붙여버리면 불상사 발생
 ex) "wyeoo"에서 "ye" 매칭 후 제거
        -> "woo"가 되어버리는데
          이러면 "woo" 매칭되어서 
          발음 가능한 걸로 판단됨.
          (원래는 "wyeoo"는 발음불가)
'''
def solution(babbling):
    # 매칭을 할 base 발음들
    base = ["aya", "ye", "woo", "ma"]
    for i in base:
        print("====start====")
        print(f"\"{i}\"")
        p = re.compile(f"({i})+")
        for idx, j in enumerate(babbling):
            # 길이 1은 비교 필요 X
            if (len(j) == 1):
                # 스킵함
                continue
            # 매칭되는 부분은 "_"로 변경
            m = p.sub('_', j)
            # "_"가 여러 개 있을 수 있으므로
            # 그 경우엔 "_" 한 개로 치환
            m = re.compile("[_]+").sub('_', m)
            # 그대로 원래 리스트에 복사
            babbling[idx]  = m[:]
            print(f"[{idx}]to {j}?\n==> {babbling[idx]}")
        print("=====end=====")

    cnt = 0
    answer = [True if _ == '_' else False
              for _ in babbling].count(True)


    return answer

if __name__ == '__main__':
    babbling = [["aya", "yee", "u", "maa", "wyeoo"],
                ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"],
                ]
    for i in babbling:
        solve = solution(i)
        print(solve)