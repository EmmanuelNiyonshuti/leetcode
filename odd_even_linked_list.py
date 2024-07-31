#!/usr/bin/python3

from typing import Optional, List
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the list is empty or has only one node no change is needed
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

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
        [2,1,3,5,6,4,7]
    ]
    for i, case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        head = list_to_linked_list(case)
        print("Original list:")
        print_linked_list(head)

        odd_even_list = sln.oddEvenList(head)

        print("output: ")
        print_linked_list(odd_even_list)

    print("\nAll test cases completed")