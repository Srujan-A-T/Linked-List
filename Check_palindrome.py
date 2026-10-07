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

def palindrome(head):
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
        


head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(3)
head.next.next.next.next=Node(2)
head.next.next.next.next.next=Node(1)

check=palindrome(head)

print(check)