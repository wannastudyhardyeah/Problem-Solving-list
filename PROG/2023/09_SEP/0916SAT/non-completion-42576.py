def solution(participant, completion):
    # (선수 이름, 명 수)의 딕셔너리
    filter_dict_parti = {}

    for i in range(len(participant)):
        temp = participant[i]
        try:
            refer = filter_dict_parti[temp]
        except:
            # 새로 추가하기 위함
            refer = None
        if (refer != None):
            filter_dict_parti[temp] += 1
        else:
            # 1로 초기화하면서 추가
            filter_dict_parti[temp] = 1
    print(filter_dict_parti)

    for i in range(len(completion)):
        temp = completion[i]
        refer = filter_dict_parti[temp]
        # 참조 없을 경우가 없는걸로 판단
        if (refer >= 1):
            filter_dict_parti[temp] -= 1
        else:
            pass

    answer = [k for k, v in filter_dict_parti.items() if v != 0][0]
    return answer

if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]

    solution(participant, completion)