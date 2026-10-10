class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def traverse(head):
    # Traverse the doubly linked list and print its elements
    current = head
    while current:
      # Print current node's data
        print(current.data, end=" <-> ")
        # Move to the next node
        current = current.next
    print("None")

def inserthead(head,data):
    new_node=Node(data)
    new_node.next=head
    if head:
        head.prev=new_node
    return new_node

def deleteoccurance(head,key):
    temp=head
    while(temp!=None):
        if(temp.data==key):
            if(temp==head):
                head=head.next
            nextnode=temp.next
            prevnode=temp.prev
            if(nextnode):nextnode.prev=prevnode
            if(prevnode):prevnode.next=nextnode
            temp=nextnode
        else:
            temp=temp.next
    return head

head = None

head = inserthead(head, 10)
head = inserthead(head, 6)
head = inserthead(head, 10)
head = inserthead(head, 10)
head = inserthead(head,4)
head = inserthead(head, 10)

new=deleteoccurance(head,10)

traverse(new)