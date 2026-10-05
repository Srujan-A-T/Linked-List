class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


def convertArr2DLL(arr):
    head=Node(arr[0])
    curr=head

    for val in arr[1:]:
        new_node=Node(val)
        new_node.prev=curr
        curr.next=new_node
        curr=new_node

    return head

def printf(head):
    curr=head
    nodes=[]
    while curr:
        nodes.append(str(curr.data))
        curr=curr.next
    print("<->".join(nodes))

def deletionheadDLL(head):
    if head is None:
        return head

    curr = head
    curr=curr.next
    curr.prev=None
    head = curr

    return head

def deletiontailDLL(head):
    if head is None:
        return head

    curr = head 
    while curr.next.next is not None:
        curr = curr.next
    curr.next=None

    return head 

def deletionKthDLL(head,k):
    if head is None:
        return head

    curr=head
    count=k

    if k==1:
        head=curr.next
        curr=None
        return head
    
    while(count!=1):
        curr=curr.next
        count-=1

    curr.prev.next=curr.next

    return head

def deletionValDLL(head,val):
    if head is None:
        return head

    curr=head
    if head.data==val:
        head=curr.next
        curr=None
        return head

    while(curr.data!=val):
        curr=curr.next

    curr.prev.next=curr.next

    return head
    

myarr=[1,2,3,4]
head=convertArr2DLL(myarr)
printf(head)


