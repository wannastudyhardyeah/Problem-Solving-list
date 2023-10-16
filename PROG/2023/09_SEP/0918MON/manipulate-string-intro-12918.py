import re
def solution(s):

    p = re.compile("^[0-9]{4,4}$|^[0-9]{6,6}$").match(s)
    try:
        res = p.group()
    except:
        res = None
    if (res == s):
        answer = True
    else:
        answer = False

    return answer

if __name__ == '__main__':
    s = "a3456"

    solve = solution(s)
    print(solve)