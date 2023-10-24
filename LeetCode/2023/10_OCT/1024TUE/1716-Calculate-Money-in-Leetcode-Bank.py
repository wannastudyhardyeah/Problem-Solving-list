class Solution:
    def totalMoney(self, n: int) -> int:
        # 일주일 기준으로 1~7 값을 만들어서
        # 각각 iteration마다 1씩 더함
        # 이렇게 하면 1주일 뒤 월요일은
        # 이전 월요일 대비 +1로 시작함
        axis_vals_by_days = [1, 2, 3, 4, 5, 6, 7]

        sum = 0
        for i in range(n):
            # 인덱싱은 7 로 나눈 나머지로
            index = i % 7
            # 일단 먼저 합을 더해준 뒤
            sum += axis_vals_by_days[index]
            # 더해준 해당 인덱스의 값을 1 올림
            axis_vals_by_days[index] += 1
        return sum

if __name__ == '__main__':
    n = 10
    solve = Solution()
    print(solve.totalMoney(n))