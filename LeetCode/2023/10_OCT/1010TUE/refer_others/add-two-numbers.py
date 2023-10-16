from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self,
                      l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        carry = 0

        while (l1 or l2 or carry):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # 자리수 올림
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)

            # 다음 노드(.next) 갱신
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1_sll = ListNode(l1[0])
    l2_sll = ListNode(l2[0])

    l1_cnt = 1
    l2_cnt = 1
    ref_l1_sll = l1_sll
    ref_l2_sll = l2_sll

    while l1_cnt <= len(l1) - 1:
        ref_l1_sll.next = ListNode(l1[l1_cnt]) if ref_l1_sll else None
        ref_l1_sll = ref_l1_sll.next
        l1_cnt += 1

    while l2_cnt <= len(l2) - 1:
        ref_l2_sll.next = ListNode(l2[l2_cnt]) if ref_l2_sll else None
        ref_l2_sll = ref_l2_sll.next
        l2_cnt += 1

    solve = Solution()
    result_sll = solve.addTwoNumbers(l1_sll, l2_sll)

    while result_sll:
        print(result_sll.val)
        result_sll = result_sll.next