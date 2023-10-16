from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 출처: https://www.youtube.com/watch?v=xlotWQYY2aw
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        # 트리 노드 And 깊이(depth)
        # 두 개를 가져 간다
        queue.append((root, 0))
        max_depth = 0
        final_sum = 0

        while queue:
            curr_node, curr_depth = queue.popleft()
            
            #   현재의 depth가 max_depth보다
            # 큰 경우에는
            if (curr_depth > max_depth):
                # 합을 0으로 해야 함
                final_sum = 0
                max_depth = curr_depth
            # 두 depth가 서로 같다면
            elif (curr_depth == max_depth):
                # 이건 합을 더해야 하는 순간
                # (물론 더 깊이 내려갈 수 있음.
                #  그땐 바로 0으로 갱신해야 함.)
                final_sum += curr_node.val

            if (curr_node.left):
                queue.append((curr_node.left, curr_depth+1))
            if (curr_node.right):
                queue.append((curr_node.right, curr_depth+1))

        return final_sum


if __name__ == '__main__':
    n = 0
    solve = Solution()
    print(solve.deepestLeavesSum())