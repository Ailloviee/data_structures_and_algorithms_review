class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size: return -1
        
        cur_node = self.head
        for _ in range(index): 
            cur_node = cur_node.next
        
        return cur_node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.size += 1
        if not self.head: self.head = self.tail = Node(val)
        else:
            node = self.head
            self.head = Node(val, next=node)
            node.prev = self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head: return self.addAtHead(val)
        else:
            self.size += 1
            self.tail.next = Node(val, self.tail)
            self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size: return
        if index == 0: return self.addAtHead(val)
        if index == self.size:  return self.addAtTail(val)

        self.size += 1
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        new_node = Node(val, prev, prev.next)
        prev.next = new_node
        new_node.next.prev = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size: return
        
        self.size -= 1
        
        # If the list will be empty, just set head and tail to None
        if self.size == 0: 
            self.head = self.tail = None
            return
        # If deleting head, just adjust self.head to its next and the prev to None
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        prev.next = prev.next.next
        
        if index == self.size: self.tail = prev
        else: prev.next.prev = prev


# Some driver code for testing
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(2)
assert obj.get(0) == 1
assert obj.get(1) == 2

obj.addAtIndex(1,3)
assert obj.get(1) == 3
obj.deleteAtIndex(2)
assert obj.get(2) == -1