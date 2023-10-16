def solution(n, left, right):
    filled_arr = make_one_dim_arr(n, left, right)
    print("result=>", filled_arr)
    # sliced = filled_arr[left:(right+1)]
    # print(sliced)
    # merged_list = []
    # for i in range(n):
    #     merged_list += filled_arr[i]
    # print(merged_list)
    # # new_list = [filled_arr[i][j] for i in range(n) for j in range(n)]
    # # print(new_list)
    # sliced_arr = iter_by_L_and_R_val(n, merged_list, left, right)
    # print(sliced_arr)
    answer = []
    return answer

'''
    1 2 3 4 5
    2 2 3 4 5
    3 3 3 4 5
    4 4 4 4 5
    5 5 5 5 5
    
    [[1, 2], [2, 2]]
    [[1, 2, 3], [2, 2, 3], [3, 3, 3]]
    [[1, 2, 3, 4], [2, 2, 3, 4], [3, 3, 3, 4], [4, 4, 4, 4]]
    [[1, 2, 3, 4, 5], [2, 2, 3, 4, 5], [3, 3, 3, 4, 5],
        [4, 4, 4, 4, 5], [5, 5, 5, 5, 5]]
'''
def make_one_dim_arr(n, left, right):
    '''
    아니 그냥
    [1, 2, 3, 4]에서 1만 2로 바꾸고
    [2, 2, 3, 4]에서 2만 3으로 바꾸면 됨
    
    그리고 left, right로 미리 잘라야됨
    '''

    '''
    아예 처음부터
    [left, right+1] 범위에서만
    생성되도록 하면 효율적일텐데
    '''
    # size = n**2
    # iter 범위
    # => [left_cut, right_cut+1]로 좁힘
    left_cut = left // n
    minus_pad = (left_cut)*n
    left = left - minus_pad

    right_cut = right // n
    right = right - minus_pad
    print(left, right)
    '''
    입력이 10^7이므로
    2중 for문은 안될것같음
    
    이거의 핵심은 결국
    [1, 2, 3, 4]를 [4, 4, 4, 4]로
    차례대로 변경시키는 건데
    
    그럼 iter 범위를 (n/2)로 줄이고
    한 번 iter당 
    연산을 양쪽에서 두번은 안될까?
    '''
    init_list_front = [(_+1) for _ in range(n)]
    init_list_post = [n for _ in range(n)]
    sum_front = []
    sum_post = init_list_post.copy()
    # 범위를 절반으로 나눔
    # 홀수인 경우 고려해서 (+1)
    for i in range(int(n/2)+1):
        if (i < left_cut
            or i>= right_cut+1):
            continue
        # 짝수인 경우
        # 마지막은 양쪽 다 진행 필요 X
        if ((i == int(n/2))
            and (n % 2 == 0)):
            continue
        print("--------------")
        print(f"iter-\"{i}\"")
        # 앞쪽(front)
        for j in range(i):            ##
            init_list_front[j] = i+1
        print("front_init\n=>", init_list_front)
        sum_front += init_list_front
        if i == int(n/2):
            print("--------------")
            continue
        # 뒷쪽(post)
        for j in range(n-i-1, -1, -1):##
            init_list_post[j] = n-i
        # init_list_post.reverse()
        init_list_post.reverse()
        print("post_init\n=>", init_list_post)
        sum_post += init_list_post
        print("--------------")
    print("front\n=>", sum_front)
    sum_post.reverse()
    print("post\n=>", sum_post)
    print("--------------")
    print("--------------")
    temp_sum = sum_front+sum_post
    print(temp_sum)
    sum = temp_sum[left:right + 1]
    print(sum)
    return sum

if __name__ == '__main__':
    n = 5
    left = 7; right = 14

    solution(n, left, right)

    # for i in range(n):
    #     for j in range(i+1):
    #         two_d_arr[j][i] = i+1
    # for k in range(n-1, -1, -1):
    #     for j in range(k, -1, -1):
    #         temp = two_d_arr[k][j]
    #         if temp == 0:
    #             two_d_arr[k][j] = k+1