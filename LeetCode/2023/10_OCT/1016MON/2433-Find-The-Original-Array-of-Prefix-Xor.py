from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        len_pref = len(pref)

        res_list = []
        # 0번째는 초깃값처럼 처리
        init_first = pref[0]
        res_list.append(init_first)

        if len_pref == 1:
            return [init_first]

        init_second = init_first ^ pref[1]
        res_list.append(init_second)

        for i in range(2, len_pref):
            # print(f'{res_list[i - 1]}, {pref[i]}')
            xor_operated = pref[i - 1] ^ pref[i]
            res_list.append(xor_operated)
        return res_list

if __name__ == '__main__':
    pref = [13]
    solve = Solution()
    print(solve.findArray(pref))