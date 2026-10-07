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

def sort_012(head): #brute force
    curr=head
    sorthead=head

    if curr==None or curr.next==None:
        return head

    count0=0
    count1=0
    count2=0

    while curr!=None:
        if(curr.data==0):
            count0+=1
            curr=curr.next
        elif(curr.data==1):
            count1+=1
            curr=curr.next
        else:
            count2+=1
            curr=curr.next

    for _ in range(count0):
        sorthead.data=0
        sorthead=sorthead.next

    for _ in range(count1):
            sorthead.data=1
            sorthead=sorthead.next

    for _ in range(count2):
            sorthead.data=2
            sorthead=sorthead.next

    return head
        
def sorts_012(head): # sort the zeros,ones,two,in LL
    curr=head
    if(curr==None or curr.next==None):
        return head
    
    l1=Node(-1)
    zero=l1
    l2=Node(-1)
    one=l2
    l3=Node(-1)
    two=l3

    while(curr!=None):
        if(curr.data==0):
            newNode=Node(curr.data)
            l1.next=newNode
            l1=l1.next
            curr=curr.next
        elif(curr.data==1):
            newNode=Node(curr.data)
            l2.next=newNode
            l2=l2.next
            curr=curr.next
        else:
            newNode=Node(curr.data)
            l3.next=newNode
            l3=l3.next
            curr=curr.next

    
    l1.next=one.next
    l2.next=two.next

    return zero.next

head=Node(1)
head.next=Node(2)
head.next.next=Node(0)
head.next.next.next=Node(1)
head.next.next.next.next=Node(2)
head.next.next.next.next.next=Node(0)



travesalSLL(sorts_012(head))