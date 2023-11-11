from Algorithm_n_DataStruct.Hash.Trie import trie as tr

def solution(phone_book):
    trie = tr.Trie()
    '''
        Trie에는 먼저 다 넣고 하면 효율 low
        비교할 때마다 하나씩 넣기!
    '''

    # 길이순으로 정렬하기
    phone_book.sort(key=len)
    print(phone_book)

    for str_for_ins in phone_book:
        trie.insert(str_for_ins)
    # print(trie.starts_with("123"))

    len_ph_book = len(phone_book)
    for i in range(len_ph_book):
        temp_pick_str = phone_book[i]
        # Trie에 기준 문자열 하나만 있는 경우는
        # 접두어인 경우가 아니므로 이 부분 처리
        find_in_trie = trie.starts_with(temp_pick_str)
        if (len(find_in_trie) == 1
            and find_in_trie[0] == temp_pick_str):
            continue

        if trie.search(temp_pick_str):
            return False
    return True

    # word_list = ["frodo", "front", "firefox", "fire"]
    # for word in word_list:
    #     trie.insert(word)
    # print(trie.search("friend"))
    # print(trie.search("frodod"))
    # print(trie.starts_with("fr"))
    # print(trie.starts_with("fi"))


if __name__ == '__main__':
    phone_book = ["12346", "123", "1453", "1234", "31234", "12345"]

    solve = solution(phone_book)
    print(solve)