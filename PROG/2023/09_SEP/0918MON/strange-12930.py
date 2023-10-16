def solution(s):
    splited_list = s.split(' ')
    size = len(splited_list)

    answer = ' '.join([''.join((
        map(
            (lambda x: splited_list[j][x].upper()
                            if x % 2 == 0
                            else splited_list[j][x].lower()),
                        range(len(splited_list[j]))
            )
                                ))
           for j in range(size)])

    # for i in range(size):
    #     each_size = len(splited_list[i])
    #     for j in range(each_size):
    #         temp = splited_list[i]
    #         if (j % 2 == 0):
    #             splited_list[i] = (temp[:j] +
    #                                temp[j].upper() +
    #                                temp[j+1:])
    #         else:
    #             splited_list[i] = (temp[:j] +
    #                                temp[j].lower() +
    #                                temp[j+1:])
    # print(splited_list)
    # print(True)

    return answer

if __name__ == '__main__':
    s = "try hello world"
    print(solution(s))