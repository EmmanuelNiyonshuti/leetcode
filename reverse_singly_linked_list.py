#!/usr/bin/env python3

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head
            while curr is not None:
                next_tmp = curr.next
                curr.next = prev
                prev = curr
                curr = next_tmp
            return prev

if __name__ == "__main__":
    def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def print_linked_list(head: Optional[ListNode]):
        curr = head
        while curr:
            print(curr.val, end=" -> " if curr.next else "")
            curr = curr.next
        print()

    sln = Solution()
    # Test cases
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3, 4, 5],
        [-1, -5, 0, 2, -9],
        [100, 200, 300, 400, 500]
    ]
    for i, case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        head = list_to_linked_list(case)
        print("Original list:")
        print_linked_list(head)

        rev_head_iter = sln.reverseListIterative(head)

        print("Reversed list iteratively: ")
        print_linked_list(rev_head_iter)

    print("\nAll test cases completed")
