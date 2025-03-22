from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    l = r = head

    while(n > 0 and r):
        r = r.next
        n -= 1

    while(r and r.next):
        r = r.next
        l = l.next

    if(l == head and not r): return head.next

    # 1 -> 2, n = 2

    l.next = l.next.next

    return head