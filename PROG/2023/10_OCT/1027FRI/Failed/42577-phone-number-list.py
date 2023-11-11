import re

def solution(phone_book):
    '''
        어떤 번호가 다른 번호의 접두어인 경우 있을 시
        -> false
        없다면
        -> true
        
        즉, 접두어 만나는 경우 바로 return 종료!
        
        정렬해놓은 뒤에 비교하도록 하면
        최악의 경우에 가까운 케이스 더 줄이기 가능
    '''
    # 접두어이므로 표현식은 처음부터 시작 필요
    
    phone_book = sorted(phone_book)

    len_ph_book = len(phone_book)
    for i in range(len_ph_book):
        temp_pick_str = phone_book[i]
        # 정규식 적용
        regex = re.compile(f'^({temp_pick_str})')
        for j in range(0, len_ph_book):
            if i == j:
                continue
            temp_pick_comparee = phone_book[j]
            print(f"비교대상\n{temp_pick_str} // {temp_pick_comparee}")
            is_there_match = regex.match(temp_pick_comparee)
            print(is_there_match)
            if is_there_match is not None:
                return False
    return True

if __name__ == '__main__':
    # phone_book = ["123","3123"]
    phone_book = ["12346", "123", "1453", "1234", "31234", "12345"]

    solve = solution(phone_book)
    print(solve)