class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


def traverseNode(head):
    curr=head

    while(curr!=None):
        print(curr.data,end="")
        if(curr.next!=None):
            print("->",end="")
        curr=curr.next


def deleteMiddleoftheLL(head):
    fast=head
    dummy=Node(0,head)
    slow=dummy

    while(fast and fast.next):
        fast=fast.next.next
        slow=slow.next

    slow.next=slow.next.next

    return dummy.next


head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)


new=deleteMiddleoftheLL(head)

traverseNode(new)