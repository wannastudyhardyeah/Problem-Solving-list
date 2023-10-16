import sys

class cal_sum:
    def __init__(self, num_of_N, num_line):
        self.num_of_N = num_of_N
        self.num_line = num_line
        # accumulate nums' sum to this var

    def iter_sum(self):
        self.sum = 0
        iter_num = self.num_of_N
        obj_nums = self.num_line
        for i in range(self.num_of_N):
            temp_num = int(obj_nums[i])
            if temp_num == 0:
                pass
            self.sum += temp_num

    def print_sum(self):
        # print("the sum of " + str(self.num_of_N) + " numbers is: " + str(self.sum))
        print(self.sum)

if __name__ == "__main__":
    num_of_N = int(sys.stdin.readline().rstrip())
    num_line = sys.stdin.readline().rstrip()
    # print("the number of N: ", num_of_N)
    # print("nums without blank: ", num_line)

    new_put = cal_sum(num_of_N, num_line)
    new_put.iter_sum()
    new_put.print_sum()