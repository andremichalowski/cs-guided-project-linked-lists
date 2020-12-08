# Let's represent a Node 
class LinkedListNode:
    # constructor 
    def __init__(self, value):
        self.value = value
        # the "arrow"
        self.next = None
​
# initialize a few LinkedListNodes
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
​
# connect the LinkedListNodes together 
x.next = y
y.next = z
​
# define a function that prints every node 
# in the linked list starting with the input node 
def print_ll(node):
    # init a new reference that will keep track 
    # of where we are in the traversal 
    current = node 
    # traverse the linked list until 
    # we get to the end 
    while current is not None:
        # print the value of each node along the way 
        print(current.value)
        # update current to refer to the next node
        # in the linked list 
        current = current.next
​
print_ll(y)