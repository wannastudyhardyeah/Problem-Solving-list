def solution(phone_book):
    len_ph_book = len(phone_book)

    phone_book.sort()


    for j in range(1, len_ph_book):
        end_idx = len(phone_book[j - 1])
        if phone_book[j - 1] == phone_book[j][:end_idx]:
            return False
    return True

if __name__ == '__main__':
    phone_book = ["12346", "123", "1453", "1234", "31234", "12345"]

    solve = solution(phone_book)
    print(solve)