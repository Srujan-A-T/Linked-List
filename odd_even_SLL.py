class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def traveseLL(head):
    while head !=None:
        print(head.data,end="")
        if(head.next!=None):
            print("->",end="")
        head=head.next
        

def Odd_even(head):
    odd=head
    even=head.next
    evenhead=head.next

    while(even!=None and even.next!=None):
        odd.next=odd.next.next
        even.next=even.next.next
        odd=odd.next
        even=even.next

    odd.next=evenhead

    return head



head=Node(1)
head.next=Node(3)
head.next.next=Node(4)
head.next.next.next=Node(5)
head.next.next.next.next=Node(2)
head.next.next.next.next.next=Node(6)


oddeven=Odd_even(head)

traveseLL(oddeven)

