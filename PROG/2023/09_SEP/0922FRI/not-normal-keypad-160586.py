'''
프로그래머스
160586 - 대충 만든 자판
'''
'''
전략

A-Z 각각에 대하여
n개의 키보드 중 그 idx값이 가장 작은것을 매핑하기

But, 최악의 경우는???
키보드가 100개 있을 때
+
모든 keymap[i]의 원소가 100개 있을 때.
    & 어떤 문자의 최초가 99(=100)번째에 위치.
그리고
최초 위치가 99번째인 문자가 속한 keymap[i]의 i가 99.

==> 그래도 2초는 넘지 않을거임!!! 
'''
A_chr_to_num = ord("A")
def solution(keymap, target):
    # 일단 keymap의 길이부터 저장
    len_kymap = len(keymap)
    # A~Z 딕셔너리
    atoz_map = [-1 for _ in range(ord("Z")-ord("A")+1)]
    for i in range(len_kymap):
        temp_range = len(keymap[i])
        for j in range(temp_range):
            temp_chr = keymap[i][j]
            # keymap에서 참조한
            # 특정 알파벳의 인덱스
            temp_idx = ord(temp_chr) - A_chr_to_num
            # temp_map
            # : atoz_map에서
            #  각 알파벳 매핑 idx값임
            temp_map = atoz_map[temp_idx]
            print(f"temp_map: {temp_map}")

            if (temp_map == -1
                    or temp_map > j):
                atoz_map[temp_idx] = j
            print(f"atoz_map\n=>{atoz_map}")
    #-----------------------------------
    #----target 파트-------
    target_range = len(target)
    # 총 눌러야하는 횟수 누적 합
    # target의 원소 개수만큼 생성
    cnt_sum = [0 for _ in range(target_range)]
    for i in range(target_range):
        len_target = len(target[i])
        for j in range(len_target):
            temp_target = target[i][j]
            target_idx = ord(temp_target) - A_chr_to_num
            
            # target_idx로 참조했을 때
            # 하나라도 -1이 있다는 건
            # 그건 불가능하다는 얘기임
            # 이 값은 더해지면 안됨!!!
            if (atoz_map[target_idx] == -1):
                cnt_sum[i] = 0
                break
            # target의 각 알파벳으로 조회한
            # 최초 idx값을 각 합계에 누적
            cnt_sum[i] += atoz_map[target_idx] + 1
        # cnt_sum[i] == 0인 경우 처리
        if (cnt_sum[i] == 0):
            cnt_sum[i] = -1
    print(f"cnt_sum: {cnt_sum}")
    answer = cnt_sum

    return answer

if __name__ == '__main__':
    keymap = ["ABACD", "BCEFD"]
    target = ["ABCD","AABB"]
    solve = solution(keymap, target)
