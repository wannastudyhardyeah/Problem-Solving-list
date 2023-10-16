from collections import Counter

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        hash_cnted =  self.compare_and_acc(word)
        cnt = dict(hash_cnted)
        nums_of_hash_cnted = self.count_nums_of_dict(cnt)
        len_nums_cnted = len(nums_of_hash_cnted)
        print(nums_of_hash_cnted)
        print(list(nums_of_hash_cnted.keys())[0])
        print(len_nums_cnted)

        '''
        len(nums_of_hash_cnted)가
        (i) 1이다
            1) 1개인 것만 있다
             => 이러면 True
            2) 2개 이상인 것만 있다
             => 다 개수 같다는 말이므로
                1개 제거 시, 달라짐
        (ii) 2이다
            1) 1개인 것이 있다
            => 이러면 True
            2) 1개인 것이 없다
             => 1개 제거 시, len은 2가 됨
             => False
        '''
        if (len_nums_cnted == 1):
            if (list(nums_of_hash_cnted.keys())[0] == 1):
                return True
            else:
                return False
        else:
            try:
                is_here_one = nums_of_hash_cnted[1]
            except:
                is_here_one = 0
            try:
                is_here_two = nums_of_hash_cnted[2]
            except:
                is_here_two = 0

            if is_here_one == 1:
                return True
            else:
                if is_here_one == 1:
                    return
                return False

    # 문자열 읽어서 해시맵에 카운트
    def compare_and_acc(self, word):
        # Counter로 해시맵
        hash = Counter(word)
        return hash
    
    # 해시맵에 나온 문자별 개수를
    # 서로 다른 개수가 몇 개인지 세기 위해
    def count_nums_of_dict(self, cnt_dict_hash):
        return Counter(dict(cnt_dict_hash).values())
    
if __name__ == '__main__':
    s = "abcc"
    solve = Solution()
    print(solve.equalFrequency(s))