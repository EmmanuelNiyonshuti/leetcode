#!/usr/bin/python3

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def count_nodes(head: Optional[ListNode]) -> int:
            count = 0
            while head:
                head = head.next
                count += 1
            return count
        if head is None:
            return None
        if head.next is None:
            del head
            return None
        nodes_num = count_nodes(head)
        mid = nodes_num // 2
        new_head = head
        while mid > 1:
            mid -= 1
            head = head.next
        head.next = head.next.next
        return new_head


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
        [2, 1],
        [1,2,3,4],
        [1,3,4,7,1,2,6]
    ]
    for i, case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        head = list_to_linked_list(case)
        print("Original linked list:")
        print_linked_list(head)

        modified_list = sln.deleteMiddle(head)

        print("new linked list: ")
        print_linked_list(modified_list)

    print("\nAll test cases completed")

