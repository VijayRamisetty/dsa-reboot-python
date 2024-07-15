class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_node_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def find_mid_slow(self):
        current_node = self.head
        arr = []
        while current_node is not None:
            arr.append(current_node.data)
            current_node = current_node.next
        return arr[len(arr)//2]

    def find_mid_fast(self):
        """
        Floyd's Cycle Finding Algo (or) Hare & Tortoise
        :return: mid_val
        """
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def traverse(self):
        if self.head is None:
            print('list is empty')
            return

        current_node = self.head
        while current_node:
            print(current_node.data, end='->')
            current_node = current_node.next


if __name__ == '__main__':
    ll = LinkedList()

    for i in range(1, 10):
        ll.add_node(i)

    print('\n')
    ll.traverse()
    print('\n')
    ll.add_node_at_end(99)
    print('\n')
    ll.traverse()
    print('\n')
    print(ll.find_mid_slow())
    print('\n')
    print(ll.find_mid_fast())
