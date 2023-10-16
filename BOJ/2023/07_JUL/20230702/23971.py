import sys


class reserve_distancing:
    def __init__(self, H, W, N, M):
        # row
        self.H = H
        # column
        self.W = W
        self.N = N
        self.M = M

        self.empty = "E"
        self.able = "O"
        self.not_able = "X"

        # ( H * W ) size
        self.whole_room = [[self.empty for _ in range(W)] for __ in range(H)]
        
        # start by setting (0, 0) as "O"
        self.whole_room[0, 0] = self.able

    # marking "available" table
    def marking_O(self, pos_mark):
        r = pos_mark[0]
        c = pos_mark[1]

        self.whole_room[r][c] = self.able

    # marking "NOT-available" table
    def marking_X(self, pos_mark):
        r = pos_mark[0]
        c = pos_mark[1]

        self.whole_room[r][c] = self.not_able

    def calculate(self):
        temp_room = self.whole_room

        # it is compared with length of each column
        # start with "0-th Column"
        now_cnt_column = 0
        length_column = self.H

        while now_cnt_column < length_column:
            # it is compared with length of each row
            # start with "0-th Row"
            now_cnt_row = 0
            length_row = self.W

            if now_cnt_column == 0:
                while (now_cnt_row < length_row and
                       ):
                    if temp_room[now_cnt_row][now_cnt_column] == self.able:
                        temp_room[now_cnt_row][now_cnt_column] = 
            else:
                pass
        self.whole_room = temp_room
if __name__ == "__main__":
    num_put = int(sys.stdin.readline().rstrip())