"""
20230513
BOJ 25304 영수증
"""
import sys


# 총 금액 X
sum_amount = int(sys.stdin.readline().rstrip())
# 구매한 물건 종류의 수 N
the_num_of_things = int(sys.stdin.readline().rstrip())

# 누적하여 총 금액을 더하기 위한 변수
sum_acc = 0


for _ in range(the_num_of_things):
    """
    종류 N개 만큼 반복해서 
        각각 가격 a와 개수 b를 입력 받기 

    temp_list : 임시로 각각의 a와 b를 저장하기 위한 리스트
    """
    temp_list = list(map(int, sys.stdin.readline().rsplit(' ')))

    sum_acc += (temp_list[0] * temp_list[1])


# 총 금액 X와 sum_acc가 동일한지 판단
if (sum_amount == sum_acc):
    print("Yes")
else:
    print("No")