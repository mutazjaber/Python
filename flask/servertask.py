class Node:
    def __init__(self, data = None):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None



    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.value, end=" ------>" )
            curr = curr.next 

    def addAtPosition(self, data ,postion):
        new_node = Node(data)
        current= self.head
        
        if postion == 1 :
            new_node.next = self.head
            self.head = new_node
        
        else :
            while postion > 1 :
                
            
        

    

# headData = linkedList()
# headData.head = node('one')
# node2 = node ('two')
# node3= node ('three')
# node4 = node('four')
# headData.head.next = node2
# node2.next = node3
# node3.next = node4