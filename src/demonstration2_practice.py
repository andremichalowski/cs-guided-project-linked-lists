class LinkedListNode():
  def __init__(self, value):
    self.value = self
    self.next = None

def reverse(head_of_list):
  current = head_of_list
  prev = None

  while current is not None:
    next = current.next
    current.next = prev

    prev = current
    current = next

  return prev


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z


def print_ll(node):
  current = node
  while current is not None:
    print(current.value)
    current = current.next

print_ll(x)
print('====')
new_head = reverse(x)
print_ll(new_head)