""" 
20230801TUE
Goorm - 174805: 숫자 제거 배열


"""
import sys
"""

range

1 <= N      <= 100,000
1 <= K      <= 100
1 <= a_i    <= 200,000

in case which "K" is bigger than "a_i"
    it's okay to pass it
e.g. K = 99, a_i = 5 
    => no need to check!

"""
def thefunc(ex_criteria, seq_a):
    '''
    processing main iteration within entire_num
    
    return a list 
        it contains numbers that only is matched to 'criteria'  
    ''' 
    final_list = []

    for i in seq_a:
        result = comp_for_each_elmnt(ex_criteria, i)
        if (result == 0):
            final_list.append(i)
    return final_list

def comp_for_each_elmnt(ex_criteria, each_seq_a):
    '''
    a function 
        that processes comparison for each element of the lists
            (btw. ex_criteria and seq_a[i])
    '''
    len_crit = len(ex_criteria)
    len_seq_a = len(each_seq_a)

    if (len_crit > len_seq_a):
        return 0
    elif (len_crit == len_seq_a):
        if (ex_criteria == each_seq_a):
            return 1
        else:
            return 0
    else:
        i= 0
        # a variable for flagging 
        #   if a correct letter with 'crit[0]' is detected 
        is_consecu = 0
        while (i < len_crit):
            if (is_consecu == 0): j = 0
            while (j < len_seq_a):
                if (each_seq_a[j] == ex_criteria[i]):
                    is_consecu += 1
                    if (j < len_seq_a - 1):
                        j += 1
                    break
                else:
                    is_consecu = 0
                j += 1
            i += 1
        
        if (is_consecu == len_crit):
            return 1
        else:
            return 0


    
    '''
    len(crit) & len(e_seq_a)
    =A          =B
    
    1) A = B
    => if (crit == e_seq_a)

    2) A < B
      a) A = 1, B > 1
    => for i in range(B):
        if (e_seq_a[i] == crit)
    
      b) A > 1, B > 1
    => for i in range(A):
        for j in range(B):
            if 
    
    i= 0
    # a variable for flagging 
    #   if a correct letter with 'crit[0]' is detected 
    is_consecu = 0
    while (i < A):
      if (is_consecu == 0): j = 0
      while (j < B):
        if (e_seq_a[j] == crit[i]):
          is_consecu = 1
          j += 1
          break
        j += 1
      i += 1   

    '''


    


if __name__ == "__main__":
    while(1):
        input_data = [[] for _ in range(2)]
        first = 0; second = 1
        input_data[first] = sys.stdin.readline().rstrip().rsplit(' ')
        # N
        entire_num = input_data[first][0]
        # K (exclusion criteria)
        ex_criteria = input_data[first][1]

        input_data[second] = sys.stdin.readline().rstrip().rsplit(' ')

        res = thefunc(ex_criteria, input_data[second])
        print(len(res))

    # print(input_data)

""" if __name__ == "__main__":   
    crit = "ab"
    for_test = ["abcd", "abc", "aqab", "aqaqab", "aqaqaqaq", "ab", "aq"]

    for tst in for_test:
        comp_for_each_elmnt(crit, tst) """