"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
class Solution:
    def GetNth(self, head, index):
        # Code Here
        curr = head
        count = 1
        while curr :
            if count ==  index :
                return curr.data
            curr = curr.next 
            count += 1
        return -1
