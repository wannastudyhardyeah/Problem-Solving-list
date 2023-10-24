from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        what_max_val = max(hours)
        if what_max_val < target:
            return 0
        else:
            cnt = 0
            for one_emp in hours:
                if one_emp >= target:
                    cnt += 1
            return cnt

if __name__ == '__main__':
    hours = [0,1,2,3,4]
    target = 2
    solve = Solution()
    print(solve.numberOfEmployeesWhoMetTarget(hours, target))