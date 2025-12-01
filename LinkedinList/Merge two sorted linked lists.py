"""
Merge two sorted linkedin list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedMerge(self, head1, head2):
        # Create a dummy node to start the merged list
        dummy = Node(0)
        curr = dummy

        # Traverse both lists
        while head1 and head2:
            if head1.data <= head2.data:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next   # move curr forward

        # Attach the remaining nodes
        if head1:
            curr.next = head1
        else:
            curr.next = head2

        # Return the merged list (skip dummy)
        return dummy.next
