class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def display_list(self):
        curr = self.head
        while curr:
            if curr.next is not None:
                print(curr.data, end='->')
                curr = curr.next
            else:
                print(curr.data)
                curr = curr.next


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(10)
    second = Node(11)
    third = Node(12)
    # print('Head Node Is:', linked_list.head.data)
    linked_list.head.next = second
    # print('2nd Node Is:', linked_list.head.get_next())
    linked_list.head.next.next = third
    # print('3rd Node Is:', linked_list.head.next.get_next())
    print('Complete List Is:')
    linked_list.display_list()
