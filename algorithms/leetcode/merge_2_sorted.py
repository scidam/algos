# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        item1 = list1
        item2 = list2

        previousItem = None
        startList = None

        while item1 is not None or item2 is not None:
            if previousItem is None:
                if item1 and item2:
                    if item1.val <= item2.val:
                        previousItem = ListNode(val=item1.val)
                        item1 = item1.next if item1.next else None
                    elif item2.val <= item1.val:
                        previousItem = ListNode(val=item2.val)
                        item2 = item2.next if item2.next else None
                elif item1 and not item2:
                    previousItem = ListNode(val=item1.val)
                    item1 = item1.next if item1.next else None
                elif item2 and not item1:
                    previousItem = ListNode(val=item2.val)
                    item2 = item2.next if item2.next else None
                startList = previousItem
                continue

            if item1 and item2:
                if previousItem.val <= item1.val <= item2.val:
                    previousItem.next = ListNode(val=item1.val)
                    item1 = item1.next if item1.next else None
                    previousItem = previousItem.next
                elif previousItem.val <= item2.val <= item1.val:
                    previousItem.next = ListNode(val=item2.val)
                    item2 = item2.next if item2.next else None
                    previousItem = previousItem.next
            elif item1 and not item2:
                previousItem.next = ListNode(val=item1.val)
                item1 = item1.next if item1.next else None
                previousItem = previousItem.next
            elif item2 and not item1:
                previousItem.next = ListNode(val=item2.val)
                item2 = item2.next if item2.next else None
                previousItem = previousItem.next

        return startList
