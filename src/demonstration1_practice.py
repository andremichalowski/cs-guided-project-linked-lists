class LinkedListNode():
  def __init__(self, value):
      self.value = value
      self.next = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z


def delete_node(node_to_delete):
  next_node = node_to_delete.next
  node_to_delete.value = next_node.value
  node_to_delete.next = next_node.next

def print_ll(node):
  current = node
  while current is not None:
    print(current.value)
    current = current.next

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')


