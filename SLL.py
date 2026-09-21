class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# create a function called traverse a linked list


def travesalSLL(head):
    while head is not None:
        print(head.data,end="")
        if head.next is not None:
            print('->',end="")
        head=head.next
    print()

def insertFront(head,x):
    newnode=Node(x)
    newnode.next=head
    return newnode

def insertend(head,x):
    newnode=Node(x)
    last=head
    while last.next is not None:
        last=last.next
    last.next=newnode

    return head

def atpositon(head,pos,x):
    if pos <1:
        return head

    if pos==1:
        newnode=Node(x)
        newnode.next=head
        return newnode

    curr=head

    for i in range(1,pos-1):
        if curr is None:
            return head
        curr=curr.next

def removehead(head):
    if head is None:
        return None

    temp=head
    head=head.next

    temp=None

    return head

def removelast(head):
    if head==None or head.next==None:
        return None

    temp=head

    while temp.next.next!=None:
        temp=temp.next

    temp.next=None

    return head

def deleteKth(head,k):
    if(head==None):
        return head

    if(k==1):
        temp=head
        head=head.next
        temp=None
        return head

    count=0
    temp=head
    prev=None
    while(temp!=None):
        count+=1
        if(count==k):
            prev.next=prev.next.next
            temp=None
            break
        prev=temp
        temp=temp.next

    return head

def deleteel(head,el):
    if(head==None):
        return head

    if(head.data==el):
        temp=head
        head=head.next
        temp=None
        return head

    temp=head
    prev=None
    while(temp!=None):
        if(temp.data==el):
            prev.next=prev.next.next
            temp=None
            break
        prev=temp
        temp=temp.next

    return head

if __name__=="__main__":

    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head.next.next.next.next=Node(40)
    head.next.next.next.next.next=Node(50)
    head.next.next.next.next.next.next=Node(40)


    count=0
    val=40
    curr=head
    while curr!=None:
        if(curr.data==val):
            count+=1
            curr=curr.next
        else:
            curr=curr.next

    for i in range(count):
        head=deleteel(head,val)


    travesalSLL(head)