# This is Simple List Queue Implementation

class ListQueue:
    def __init__(self, limit):
        self.front = self.rear = 0
        self.size = 0
        self.capacity = limit
        self.LQ = [] * self.capacity

    def is_full(self):
        return self.capacity == self.rear

    def is_empty(self):
        return self.rear == 0

    def en_queue(self, val):
        if self.is_full():
            return f'Full Queue'
        else:
            self.LQ.append(val)
            self.rear += 1
            self.size += 1

    def de_queue(self):
        if self.is_empty():
            return f'Empty Queue'
        else:
            x = self.LQ.pop(0)
            self.rear -= 1
            self.size -= 1
            return x

    def get_front(self):
        if self.is_empty():
            return f'Empty Queue'
        else:
            return self.LQ[self.front]

    def get_rear(self):
        if self.is_empty():
            return f'Empty Queue'
        else:
            return self.LQ[self.rear]

    def display(self):
        if self.is_empty():
            return f'Empty Queue'
        else:
            return self.LQ


if __name__ == '__main__':
    queue = ListQueue(5)
    queue.en_queue(10)
    queue.en_queue(20)
    queue.en_queue(30)
    queue.en_queue(40)
    queue.en_queue(50)
    print('Current Queue:', queue.display())
    print('Queue Size:', queue.size)
    print('Queue Front:', queue.front, f'[{queue.LQ[queue.front]}]')
    print('Queue Rear:', queue.rear, f'[{queue.LQ[queue.rear - 1]}]')
    print('-' * 50)
    queue.de_queue()
    print('Current Queue:', queue.display())
    print('Queue Size:', queue.size)
    print('Queue Front:', queue.front, f'[{queue.LQ[queue.front]}]')
    print('Queue Rear:', queue.rear, f'[{queue.LQ[queue.rear - 1]}]')
    queue.en_queue(60)
    print('Current Queue:', queue.display())
    queue.en_queue(80)
    print('Current Queue:', queue.display())
