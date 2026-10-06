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

head1=Node(1)
head1.next=Node(2)
head1.next.next=Node(3)


head2=Node(9)
head2.next=Node(9)
head2.next.next=Node(9)

def Add2LL(head1,head2):
    t1=head1
    t2=head2

    dummyNode=Node(-1)
    curr=dummyNode
    carry=0

    while(t1!=None or t2!=None):
        sum=carry
        if(t1):sum+=t1.data
        if(t2):sum+=t2.data
        newNode=Node(sum%10)
        carry=sum//10

        curr.next=newNode
        curr=curr.next

        if(t1):t1=t1.next
        if(t2):t2=t2.next

    if(carry):
        newNode=Node(carry)
        curr.next=newNode

    return dummyNode.next

new1=reverse(head1)
new2=reverse(head2)

new3=Add2LL(new1,new2)
new4=reverse(new3)
traverseNode(new4)





