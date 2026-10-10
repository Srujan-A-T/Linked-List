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


def intersectionOfLL(head1,head2):
    temp=head1
    hashing=set()
    while(temp!=None):
        hashing.add(temp)
        temp=temp.next

    temp=head2
    
    while(temp!=None):
        if(temp in hashing):
            return temp

        temp=temp.next

    return -1 

def intersectoptimal(head1,head2):
    t1=head1
    t2=head2

    while(t1!=t2):

        t1=head2 if(t1 is None) else t1.next
        t2=head1 if(t2 is None) else t2.next

    return t1
    


head1=Node(1)
head1.next=Node(3)
head1.next.next=Node(4)
head1.next.next.next=Node(2)
head1.next.next.next.next=Node(5)


head2=Node(3)
head2.next=Node(8)
head2.next.next=head1.next.next
head2.next.next.next=Node(7)



new=intersectoptimal(head1,head2)

print(new.data)


