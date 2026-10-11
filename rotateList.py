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

def findkthNode(head,k):
    k-=1
    while(head!=None and k>0):
        k-=1
        head=head.next

    return head

def rotateList(head,k):
    if(head==None or k==0):return head

    length=1
    tail=head
    while(tail.next!=None):
        length+=1
        tail=tail.next

    if(length%k==0):return head
    k=k%length

    tail.next=head

    lastNode=findkthNode(head,length-k)
    head=lastNode.next
    lastNode.next=None

    return head
    


head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
head.next.next.next.next.next=Node(60)
head.next.next.next.next.next.next=Node(70)

rotate=rotateList(head,3)
traverseNode(rotate)
