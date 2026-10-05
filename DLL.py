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
        

    

myarr=[1,2,3,4]
head=convertArr2DLL(myarr)
printf(head)


        