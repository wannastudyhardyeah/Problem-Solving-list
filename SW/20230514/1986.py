"""
20230514
1986 지그재그 숫자
"""
import sys

howmany = int(sys.stdin.readline().rstrip())
num_input = []
for _ in range(howmany):
    num_input.append(int(sys.stdin.readline().rstrip()))


for _ in range(howmany):
    sum = 1
    for i in range(2, num_input[_] + 1):
        if (num_input[_] == 1):
            print("#" + str(_ + 1) + " ", sum)
        else:
            # minus
            if (i % 2 == 0):
                sum -= i
            # plus
            else:
                sum += i
    print("#" + str(_ + 1) + " ", sum)
