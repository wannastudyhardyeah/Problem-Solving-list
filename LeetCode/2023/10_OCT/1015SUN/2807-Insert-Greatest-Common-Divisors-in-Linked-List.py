# Definition for singly-linked list.
from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        '''
        중간에 gcd를 삽입/연결하기 때문에
        다음 노드를 미리 저장해야 함
        '''
class Solution:
    def insertGreatestCommonDivisors(self,
                                     head: Optional[ListNode]) \
                                -> Optional[ListNode]:
        # 길이가 1인 경우를 고려
        if (head.next is None):
            return head

        # print(head)
        for_ref_head = head
        next_node = head.next
        while for_ref_head:
            front = for_ref_head.val
            post = for_ref_head.next.val
            print(f'front: {front}, post:{post}')
            temp_gcd_val = math.gcd(front, post)
            print(f'gcd: {temp_gcd_val}')

            new_gcd_node = ListNode(temp_gcd_val)
            new_gcd_node.next = for_ref_head.next
            for_ref_head.next = new_gcd_node

            #  (gcd를 제외한) 다음 노드로 진행
            # 이때, next_node의 다음 노드가 None이면
            # break 해야 함
            if (next_node.next is None):
                break
            for_ref_head = next_node
            next_node = next_node.next

        return head
    # def getGCD(self):


if __name__ == '__main__':
    # head_list = [18, 6, 10, 3]
    head_list = [18]

    head = ListNode(val=head_list[0])
    refer_head = head

    for idx in range(1, len(head_list)):
        refer_head.next = ListNode(val=head_list[idx])
        refer_head = refer_head.next

    node = head
    while node:
        print(node.val)
        node = node.next

    solve = Solution()
    res_head = solve.insertGreatestCommonDivisors(head)
    node = res_head
    while node:
        print(node.val)
        node = node.next
