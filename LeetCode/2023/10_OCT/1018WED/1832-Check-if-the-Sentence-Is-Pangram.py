class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 알파벳의 갯수에 대한 상수
        LEN_a_TO_z = ord('z') - ord('a') + 1
        # 인덱싱을 위한 상수(빼기 위함)
        ASCII_VALUE_a_FOR_IDX = ord('a')

        # 각 알파벳의 갯수에 대한 해시 테이블
        hash_low_atoz = [0 for i in range(LEN_a_TO_z)]
        # 각 알파벳 갯수 cnt가 최초로 더해질 때에만 +1함
        cnt_only_if_zero = 0
        # print(hash_low_atoz)

        for idx, s in enumerate(sentence):
            s_to_idx = ord(s) - ASCII_VALUE_a_FOR_IDX
            if (hash_low_atoz[s_to_idx] > 0):
                continue
            hash_low_atoz[s_to_idx] += 1
            cnt_only_if_zero += 1
            # print(f'{s}: {s_to_idx}')
            # print(f'{hash_low_atoz}, {cnt_only_if_zero}')

            # 26개 도달한 경우 바로 True 후 종료
            if (cnt_only_if_zero == LEN_a_TO_z):
                return True
        if (cnt_only_if_zero < LEN_a_TO_z):
            return False

if __name__ == '__main__':
    sentence = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
    solve = Solution()
    print(solve.checkIfPangram(sentence))