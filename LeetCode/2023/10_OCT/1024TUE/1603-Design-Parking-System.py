class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # self.big = big
        # self.medium = medium
        # self.small = small
        self.list_by_size = [big, medium, small]


    def addCar(self, carType: int) -> bool:
        index_by_minus_one = carType - 1
        self.list_by_size[index_by_minus_one] -= 1
        return self.list_by_size[index_by_minus_one] >= 0
        # if carType == 1:
        #     if self.big > 0:
        #         self.big -= 1
        #         return True
        #     else:
        #         return False
        # elif carType == 2:
        #     if self.medium > 0:
        #         self.medium -= 1
        #         return True
        #     else:
        #         return False
        # else:
        #     if self.small > 0:
        #         self.small -= 1
        #         return True
        #     else:
        #         return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

if __name__ == '__main__':
    solve = ParkingSystem(1, 1, 0)
    print(solve.list_by_size)
    input_list = [1, 2, 3, 1]
    for i in input_list:
        solve.addCar(i)
    print(solve.list_by_size)
