class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLL:
    def __init__(self):
        self.head=None

    def insert_front(self,data):
        new_node=Node(data)

        new_node.next=self.head
        if self.head!=None:
            self.head.prev=new_node

        self.head=new_node


    def insert_end(self,data):

        new_node=Node(data)

        if self.head==None:
            self.head=new_node
            return

        curr=self.head
        while curr.next!=None:
            
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
    def insert_after(self,prev_node,data):
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next:
            new_node.next.prev=new_node

    def insert_before(self,next_node,data) :
        new_node=Node(data)

        new_node.prev=next_node.prev
        next_node.prev=new_node
        new_node.next=next_node

        if new_node.prev.next!=None:
            new_node.prev.next=new_node


    def printDLL(self):

        if self.head==None:
            print("Empty")
            return 

        curr=self.head
        print("In forward:")
        last=None
        while curr!=None:
            
            print(curr.data)
            last=curr
            curr=curr.next

        print("Reverse:")

        while last!=None:
            print(last.data)
            last=last.prev


        


l1=DoublyLL()

l1.insert_end(1)
l1.insert_end(2)
l1.insert_end(4)
l1.insert_end((6))
l1.printDLL()
l1.insert_after(l1.head.next,3)
l1.printDLL()
l1.insert_before(l1.head.next.next.next.next,5)
l1.printDLL()
        