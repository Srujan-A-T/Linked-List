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


def removenthNode(head,n):

    
    fast=head
    for _ in range(n):
        fast=fast.next

    if(fast==None):
            return head.next

    slow=head
    
    while(fast.next!=None):
        slow=slow.next
        fast=fast.next
        

    
    slow.next=slow.next.next

    return head

head=Node(1)
head.next=Node(3)
head.next.next=Node(4)
head.next.next.next=Node(5)
head.next.next.next.next=Node(2)
head.next.next.next.next.next=Node(6)



travesalSLL(removenthNode(head,6))