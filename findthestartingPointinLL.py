class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def startingPointofLL(head):
    hash_set=set()
    temp=head

    while(temp!=None):
        if(temp in hash_set):
            return temp

        hash_set.add(temp)
        temp=temp.next

    return None

def optimalstart(head):
    fast=head
    slow=head

    while(fast and fast.next):
        fast=fast.next.next
        slow=slow.next

        if(slow==fast):
            slow=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next

            return slow

    return None
head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = head.next

print(optimalstart(head).data)