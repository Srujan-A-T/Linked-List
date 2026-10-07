class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def travesalSLL(head):
    while head is not None:
        print(head.data,end="")
        if head.next is not None:
            print('->',end="")
        head=head.next
    print()

def palindrome(head): # brute force approach 
    if(head==None):
        return False

    curr=head
    prev=None
    while(curr!=None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next

    temp=head


    while(temp!=None):
        if(temp.data==prev.data):
            temp=temp.next
            prev=prev.next
        else:
            return False

    return True


def reverseLinkedList(head):
    if(head==None):
        return head

    curr=head
    prev=None
    while(curr!=None):
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode

    return prev

def optimalPalindrome(head):

    if(head==None or head.next==None):
        return True

    fast=head
    slow=head

    while(fast.next!=None and fast.next.next!=None):
        fast=fast.next.next
        slow=slow.next

    
    newhead=reverseLinkedList(slow.next)

    first=head
    second=newhead

    while(second!=None):
        if(first.data!=second.data):
            reverseLinkedList(newhead)
            return False
        first=first.next
        second=second.next

    reverseLinkedList(newhead)
    return True

head=Node(1)
head.next=Node(2)
head.next.next=Node(2)
head.next.next.next=Node(1)


print(optimalPalindrome(head))
