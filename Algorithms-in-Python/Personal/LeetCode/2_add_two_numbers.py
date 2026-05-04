# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def addNode(self, l: ListNode, val: int):
        while l.next:
            l = l.next
        l.next = ListNode(val)
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        answer = ListNode("head")
        
        up = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum_val = x + y + up
            
            # 올림
            if sum_val > 9: up = sum_val // 10
            else: up = 0
                
            # 나머지
            sum_val %= 10
            
            self.addNode(answer, sum_val)
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        if up: self.addNode(answer, up)
                
        return answer.next   