'''
프로그래머스
140108 - 문자열 나누기
'''
'''
문자열 s = "banana"
==> x = "b"
'''
'''
그냥 읽는 족족
하나씩 계속 slice 하자!
'''

def solution(s):
    sum_cnt = 0
    seperated = s[:]

    # 종료조건
    # : 빈 문자열일 때
    while(seperated != ""):
        # 같을 때 카운트
        same_x = 0
        # 다를 때 카운트
        not_same_x = 0

        # 첫 번째 문자 저장
        first = seperated[0]
        i = 0
        #   두 개의 카운트가 같을 때는
        #  => break
        #   서로 다를 때는
        #  AND 마지막 문자 참조한 경우에
        #  => return (sum_cnt+1)
        #  이므로 loop 종료는 꼭 보장됨
        while(True):
            temp_pick_chr = seperated[i]
            if (temp_pick_chr == first):
                same_x += 1
            else:
                not_same_x += 1
            
            # 두 카운트가 동일해진 순간에
            if (same_x == not_same_x):
                sum_cnt += 1
                # 지금까지 참조한 문자열을
                # 그 이후 문자열과 분리시킴
                seperated = seperated[i+1:]
                # loop 종료
                break
            else:
                if (i + 1 == len(seperated)):
                    sum_cnt += 1
                    answer = sum_cnt
                    print(sum_cnt)
                    # 여기서 break는 
                    # 두 번 필요하기 때문에
                    # 바로 return을 함
                    return answer
            i += 1

    print(sum_cnt)
    answer = sum_cnt

    return answer

if __name__ == '__main__':
    s = "aaabbaccccabba"
    solve = solution(s)
    print(solve)
