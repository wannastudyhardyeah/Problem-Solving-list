# def solution(record):
#     answer = []
#
#     return answer

class User:
    def __init__(self, user_id, user_name, status):
        self.user_id = user_id
        self.user_name = user_name
        self.status = status
        self.status_list = []

def define_message(user_name, status):
    output_msg = ""
    if status == "Enter":
        output_msg = user_name + "님이 들어왔습니다."
    elif status == "Leave":
        output_msg = user_name + "님이 나갔습니다."
    return output_msg

if __name__ == "__main__":
    input_strs_list = ["Enter uid1234 Muzi",
                       "Enter uid4567 Prodo",
                       "Leave uid1234",
                       "Enter uid1234 Prodo",
                       "Change uid4567 Ryan"]

    split_list = []

    for i in input_strs_list:
        split_list.append(i.split(' '))

    size = len(split_list)

    print(split_list)

    user_list = []
    # 유저 최초 들어올때 기록됨
    # (join_cnt, user_name)
    user_idx = {}
    # 유저가 최초로 들어올때마다 (+1)
    join_cnt = 0

    # 유저 status 발생 때마다 모두 기록
    # (user_id, user_status)
    # (user_id로 join해야됨)
    log = []
    log_cnt = 0
    for i in range(size):
        parsing = split_list[i]
        status_parsed = parsing[0]
        if (status_parsed == "Enter"):
            tmp_id = parsing[1]
            tmp_name = parsing[2]
            try:
                refer_user_join = user_idx[tmp_id][0]
            except:
                refer_user_join = False

            if (refer_user_join is False):
                user_list.append(User(tmp_id, tmp_name, status_parsed))
                user_idx[tmp_id] = (join_cnt, tmp_name)
                join_cnt += 1
                refer_user_join = user_idx[tmp_id][0]
            else:
                user_list[refer_user_join].user_name = tmp_name
            user_list[refer_user_join].status_list.append(status_parsed)
            # print(user_list[i].user_id, user_list[i].user_name)
        elif (status_parsed == "Leave"):
            tmp_id = parsing[1]
            refer_user_join = user_idx[tmp_id][0]
            user_list[refer_user_join].status = status_parsed
            user_list[refer_user_join].status_list.append(status_parsed)
        else:
            tmp_id = parsing[1]
            changed_name = parsing[2]
            refer_user_join = user_idx[tmp_id][0]
            user_list[refer_user_join].user_name = changed_name
        # 로그 기록
        log.append((parsing[1], status_parsed))
    #
    # for i in user_list:
    #     for j in i.status_list:
    #         print(define_message(i.user_name, j))
    result = []
    for uid, stts in log:
        result.append(
            define_message(user_list[user_idx[uid][0]].user_name,
                           stts)
        )
    print(list(filter(None, result)))