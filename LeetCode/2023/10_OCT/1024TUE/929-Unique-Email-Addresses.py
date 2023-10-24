from typing import List
import re
import collections

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        '''
            '.'(쩜) 있으면
            -> 이것만 제거함
            '+' 있으면
            -> + 및 + 이후 문자들 모두 제거함
        '''
        # all_emails_list_for_hash = []
        # # local과 domain을 분리
        # for each_email in emails:
        #     local_split_by_at = each_email.split('@')[0]
        #     # domain은 마지막에 합치기 위해
        #     domian_split_by_at = '@' + each_email.split('@')[1]
        #     # print(local_split_by_at)
        #     split_by_plus = local_split_by_at.split('+')[0]
        #     # print(split_by_plus)
        #     subs_dot = re.sub('[.]', '', split_by_plus)
        #     # print(subs_dot)
        #     merged = subs_dot+domian_split_by_at
        #
        #     # 리스트에 하나씩 추가한 뒤에
        #     # Counter로 set 만들어서 len()으로 개수 구하기
        #     all_emails_list_for_hash.append(merged)
        # all_emails_hashed = collections.Counter(all_emails_list_for_hash)
        # return len(all_emails_hashed)
        
        # 아래는 풀이 이후 리트코드 solutions 참고한 거
        def parse(email: str):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            return f'{local}@{domain}'

        return len(set(map(parse, emails)))

if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    solve = Solution()
    print(solve.numUniqueEmails(emails))