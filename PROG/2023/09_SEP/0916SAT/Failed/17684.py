def solution(msg):
    answer = []
    return answer

if __name__ == "__main__":
    upper_dict = {(i+1):(chr(ord('A')+ i))
                  for i in range(ord('Z')-ord('A')+1)}
    upper_dict_key_chr = {(chr(ord('A')+ i)):(i+1)
                          for i in range(ord('Z')-ord('A')+1)}
    print(upper_dict)
    print(upper_dict_key_chr)

    # 출력 색인 담을 리스트
    for_result_list = []

    # 사전 인덱스 27부터 시작
    dict_idx = 27
    input_msg = "ABABABABABABABAB"
    size = len(input_msg)

    left_pad_msg = " " + input_msg

    now_pos = 1
    now_chunk = input_msg[0]
    # 원본 문자열에 대해 iteration
    i = 0
    while(i < size):
        if (i == size - 1):
            #           기존 색인 출력!
            for_result_list.append(upper_dict_key_chr[now_chunk])
            break
        is_i_plused = 0
        print("---------------")
        print("iter - \"i\":", i)
        now_chunk = input_msg[i]
        print("now_chunk:", now_chunk)
        print("---------------")
        # 매칭되는 가장 긴 문자열 찾기
        iter_chunk = now_chunk
        for j in range(i+1, size):
            print("now iter-\"j\":", j)
            iter_chunk += input_msg[j]
            print("현재 참조:", iter_chunk)
            # 현재 chunk에 해당되는 것 참조
            try:
                refer_idx =  upper_dict_key_chr[iter_chunk]
            except:
                # 없으면 None
                refer_idx = None
            print("refer_idx =", refer_idx)
            # 해당되는 게 있다면
            if (refer_idx != None):
                # 현재 chunk를 now_chunk에
                now_chunk = iter_chunk
                continue
            else:
                upper_dict[dict_idx] = iter_chunk
                upper_dict_key_chr[iter_chunk] = dict_idx
                print("색인 추가!\n=>", iter_chunk, dict_idx)
    #           기존 색인 출력!
                for_result_list.append(upper_dict_key_chr[iter_chunk[:(-1)]])
                len_iter_chunk = len(iter_chunk)
                if (len_iter_chunk >= 2):
                    i += len_iter_chunk - 1
                    is_i_plused = 1
                dict_idx += 1
                break
        if (is_i_plused == 1):
            continue
        else:
            i += 1
    print(for_result_list)
