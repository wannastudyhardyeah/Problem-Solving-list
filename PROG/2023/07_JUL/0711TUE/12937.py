import sys

def solution(n, arr1, arr2):
    
    res_arr1 = []
    res_arr2 = []
    for i in range(n):
        bin_arr1 = loop_divide_by_2(arr1[i], n)
        bin_arr2 = loop_divide_by_2(arr2[i], n)
        # print("bin_arr1\n==>", bin_arr1)
        # print("bin_arr2\n==>", bin_arr2)

        bin_to_sharp(bin_arr1)
        bin_to_sharp(bin_arr2)
        res_arr1.append(bin_arr1)
        res_arr2.append(bin_arr2)
    # print("this is arr1\n==>", res_arr1)
    # print("this is arr2\n==>", res_arr2)

    answer = merge_two_arrs(res_arr1, res_arr2)
    print(answer)
    return answer

""" 
인자 값을 2진수로 변환
"""
def loop_divide_by_2(n, length):
    
    temp_arr = [-1 for _ in range(length)]
    quot = n
    cnt = length - 1

    """ 
    정지조건
     : quot <= 1이 될때
    """
    while (True):
        mod = quot % 2
        quot = int(quot / 2)
        
        """         
        mod(0 또는 1) 값을 
        cnt번째에 갱신 입력
        """
        temp_arr[cnt] = mod
        cnt -= 1
        
        if (quot == 0 or quot == 1):
            temp_arr[cnt] = quot
            break
        
    # print("current quot value is\n=>", quot)
    # print("converted binary number is\n=>", temp_arr)
    return temp_arr

""" 
2진수 배열 --> "#"과 " "의 문자열로
"""
def bin_to_sharp(bin_arr):
    convert = ""
    for i in range(len(bin_arr)):
        temp_val = bin_arr[i]
        if (temp_val == 0):
            convert += chr(32)
        elif (temp_val == 1):
            convert += '#'
        else:
            pass
    # print("converted string is\n=>" + ' ' + '[' + convert + ']')

def merge_two_arrs(arr1, arr2):
    sharp_char = '#'
    blank_char = chr(32)
    size = len(arr1)
    merged = ['' for _ in range(size)]
    for i in range(size):
        str_temp_mrg = ""
        for j in range(size):
            temp_1 = arr1[i][j]
            temp_2 = arr2[i][j]
            if (temp_1 == 1 or temp_2 == 1):
                str_temp_mrg += sharp_char
            elif ((temp_1 == -1 or temp_1 == 0) and (temp_2 == -1 or temp_2 == 0)):
                str_temp_mrg += blank_char
        merged[i] = str_temp_mrg

    # print("merged arr is\n==>", merged)

    # for a in range(size):
    #     for b in range(size):
    #         print(merged[a][b], end='')
    #     print('', end='\n')
    # print(merged)
    return merged

if __name__ == "__main__":
    # int_num = int(sys.stdin.readline().rstrip())
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    solution(n, arr1, arr2)

