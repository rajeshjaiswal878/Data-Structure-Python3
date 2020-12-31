class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 1
        self.tail = None

    def __str__(self):
        return str(self.head)

    def get_tail(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr

    def insert_at_start(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.length += 1
        else:
            node.next = self.head
            self.head = node
            self.tail = self.get_tail()
            self.length += 1

    def insert_at_position(self, pos, val):
        count = 0
        node = Node(val)
        if (pos < 0) or (pos > self.length):
            print('Out Of Range')
            return
        elif pos == 0:
            self.insert_at_start(val)
        elif pos == self.length:
            self.insert_at_end(val)
        else:
            curr = self.head
            while curr and count < pos - 1:
                curr = curr.next
                count += 1
            temp = curr.next
            curr.next = node
            node.next = temp
            self.tail = self.get_tail()
            self.length += 1

    def insert_at_end(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.length += 1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            self.tail = node
            self.length += 1

    # Display Current List
    def display_list(self):
        curr = self.head
        while curr:
            if curr.next is not None:
                print(curr.data, end="->")
                curr = curr.next
            else:
                print(curr.data)
                curr = curr.next


if __name__ == '__main__':
    lst = LinkedList()
    lst.head = Node(10)
    # print(lst.head)
    # print(lst.head.data)
    lst.insert_at_start(11)
    print('Complete List')
    lst.display_list()
    print('Tail Node:', lst.tail)
    print('--' * 30)
    lst.insert_at_end(12)
    print('Complete List')
    lst.display_list()
    print('List Size:', lst.length)
    print('Tail Node:', lst.tail)
    print('--' * 30)
    lst.insert_at_end(13)
    print('Complete List')
    lst.display_list()
    print('List Size:', lst.length)
    print('Tail Node:', lst.tail)
    print('--' * 30)
    lst.insert_at_position(0, 14)
    print('Complete List')
    lst.display_list()
    print('List Size:', lst.length)
    print('Tail Node:', lst.tail)
