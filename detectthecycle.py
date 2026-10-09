class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def traverseNode(head):
    curr=head

    while(curr!=None):
        print(curr.data,end="")
        if(curr.next!=None):
            print("->",end="")
        curr=curr.next


def detectLoopLL(head):
    fast=head
    slow=head

    while(slow and fast and fast.next):
        fast=fast.next.next
        slow=slow.next

        if(fast==slow):
            return True

    return False


head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=head.next

print(detectLoopLL(head))