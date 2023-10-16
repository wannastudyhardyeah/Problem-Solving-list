import re
from collections import Counter

def solution(s):
    answer = []
    return answer


if __name__ == "__main__":
    in_str = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

    in_str = Counter(re.findall('\d+', in_str))
    print(in_str)

    # in_str = in_str[1:len(in_str)-1]
    #
    # split_str = in_str.split('},')
    # size_of_split_str = len(split_str)
    #
    #
    # new_tuple = [[] for _ in range(size_of_split_str)]
    # # ','로 스플릿 한 이후에
    # # 0~(n-2)번째만 '{'로 스플릿
    # # (n-1)번쨰는 '{', '}' 모두 스플릿
    # for i in range(size_of_split_str):
    #     if (i != size_of_split_str - 1):
    #         temp = split_str[i].split('{')[1].split(',')
    #         new_tuple[i] = [int(temp[j]) for j in range(len(temp))]
    #     else:
    #         temp = split_str[i].split('{')[1].split('}')[0].split(',')
    #         new_tuple[i] = [int(temp[j]) for j in range(len(temp))]
    #
    #
    # sorted_tuple = sorted({len(new_tuple[_]):new_tuple[_]
    #                        for _ in range(len(new_tuple))}.items())
    #
    # size_of_tuple = len(sorted_tuple)
    #
    # if len(sorted_tuple):
    #     print(list(sorted_tuple[0][1]))
    #
    # '''
    # [(1, [2]), (2, [2, 1]), (3, [1, 2, 3]), (4, [1, 2, 4, 3])]
    # print(sorted_tuple[0])          => (2, [2, 1])
    # print(sorted_tuple[0][1])       => [2, 1]
    # print(sorted_tuple[0][1][0])    => 2
    # '''
    # print(sorted_tuple[1][1])
    # stored_dict = {}
    # rank = 0
    # for i in range(size_of_tuple):
    #     val_list = sorted_tuple[i][1]
    #     for j in range(len(val_list)):
    #         try:
    #             check = stored_dict[val_list[j]]
    #         except:
    #             stored_dict[val_list[j]] = rank
    #             rank += 1
    # print(stored_dict)
    #
    # result = []
    # for key in stored_dict.items():
    #     result.append(key[0])
    # print(result)