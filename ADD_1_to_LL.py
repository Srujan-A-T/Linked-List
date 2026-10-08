class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
    curr=head
    prev=None

    while(curr!=None):
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode

    return prev

def traverseNode(head):
    curr=head

    while(curr!=None):
        print(curr.data,end="")
        if(curr.next!=None):
            print("->",end="")
        curr=curr.next

def bruteadd1(head):
    head=reverse(head)
    temp=head
    carry=1
    while(temp!=None):
        temp.data=temp.data+carry
        if temp.data <10:
            carry=0
            break
        else:
            temp.data=0
            carry=1

        temp=temp.next

    if(carry==1):
        newnode=Node(1)
        head=reverse(head)
        newnode.next=head
        return newnode

    head=reverse(head)
    return head

def helper(head):
    if head==None:
        return 1

    carry=helper(head.next)
    head.data=head.data+carry

    if(head.data<10):
        return 0

    head.data=0
    return 1

def optimal(head):

    carry=helper(head)
    if(carry==1):
        newnode=Node(1)
        newnode.next=head
        return newnode
    return head
    
head=Node(9)
head.next=Node(9)
head.next.next=Node(9)
head.next.next.next=Node(9)

new=optimal(head)
traverseNode(new)