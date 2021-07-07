import gc
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

    def deletion(self,dele):
        if self.head==None:
            return 
        #head ko delete
        if self.head==dele:
            self.head=self.head.next
            return

      

        if dele.next!=None:
            dele.next.prev=dele.prev

        if dele.prev!=None:
            dele.prev.next=dele.next

        gc.collect()



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

l=DoublyLL()
l.insert_front(3)
l.insert_front(2)
l.insert_front(1)
l.insert_front(0)
l.printDLL()

l.deletion(l.head)
l.printDLL()

l.deletion(l.head.next.next)
l.printDLL()