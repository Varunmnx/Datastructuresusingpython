class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        
        ## a+b = b+a : to make the length of both the list nodes same
        ## it is obvious that end of both the lists will be same repeating x nodes. 
        while a != b:
            
            if a:
                a = a.next
            else:
                a = headB
                
            if b:
                b = b.next
            else:
                b = headA
        
        ## return the head address is a (or b) where the a.val == b.val
        ## this means repeating x nodes starts form that head only.
        return a