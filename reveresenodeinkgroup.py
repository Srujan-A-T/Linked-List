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

def reverseLL(head):
    temp=head
    prev=None
    while(temp!=None):
        nextNode=temp.next
        temp.next=prev
        prev=temp
        temp=nextNode

    return prev

def findkthNode(head,k):
    k-=1
    while(head!=None and k>0):
        k-=1
        head=head.next

    return head

def reversekthgroup(head,k):
    temp=head
    prevNode=None
    while(temp!=None):
        kthNode=findkthNode(temp,k)
        if(kthNode==None):
            if(prevNode):
                prevNode.next=temp
            break
        nextNode=kthNode.next
        kthNode.next=None
        reverseLL(temp)
        if(temp==head):
            head=kthNode
        else:
            prevNode.next=kthNode

        prevNode=temp
        temp=nextNode
    return head



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
head.next.next.next.next.next=Node(60)
head.next.next.next.next.next.next=Node(70)

rev=reversekthgroup(head,3)

traverseNode(rev)
