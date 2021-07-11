class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def insert_start(self,data):
        new_node=Node(data)
     
        
        new_node.next=self.head
        self.head=new_node

    def printLL(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next

    def remove_duplicates(self):
       

        curr=self.head
        hash=set()
        hash.add(self.head.data)
        if self.head is None or self.head.next is None:
            return 
        while curr.next:
            if curr.next.data in hash:
                curr.next=curr.next.next

            else:
                hash.add(curr.next.data)
                curr=curr.next

        

K=LL()
K.insert_start(21)
K.insert_start(1)
K.insert_start(2)
K.insert_start(21)
K.insert_start(3)
K.insert_start(4)
K.insert_start(5)
K.insert_start(3)
K.insert_start(6)
print("Before removing duplicates")
K.printLL()
print()
print("After removing")
K.remove_duplicates()
K.printLL()