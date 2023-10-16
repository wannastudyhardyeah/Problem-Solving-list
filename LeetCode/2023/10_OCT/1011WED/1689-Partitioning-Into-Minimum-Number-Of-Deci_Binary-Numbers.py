class Solution:
    def minPartitions(self, n: str) -> int:
        len_n_str = len(n)
        biggest_num = -1
        for i in range(len_n_str):
            char_pick_int = int(n[i])
            if (biggest_num < char_pick_int):
                biggest_num = char_pick_int
            # print(biggest_num)
        return biggest_num

if __name__ == '__main__':
    n_str = "27346209830709182346"
    solve = Solution()
    print(solve.minPartitions(n_str))