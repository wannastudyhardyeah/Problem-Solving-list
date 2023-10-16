import re

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        self.address = address
        return self.regexp()

    def regexp(self):
        regexp_pat = re.compile(r'[.]{1,1}')
        substituted = regexp_pat.sub('[.]', self.address)
        return substituted

if __name__ == '__main__':
    address = "255.100.50.1"
    solve = Solution()
    print(solve.defangIPaddr(address))