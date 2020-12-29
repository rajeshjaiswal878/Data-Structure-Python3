# Array Implementation of Queue In Python

class Queue:
    def __init__(self, limit):
        self.front = self.size = 0
        self.capacity = limit
        self.rear = self.capacity - 1
        self.Q = [None] * self.capacity

    # Define Full Check On Queue
    def is_full(self):
        return self.size == self.capacity

    # Define Empty Check On Queue
    def is_empty(self):
        return self.size == 0

    # Define EnQueue[Insert Operations At Rear: item]
    def en_queue(self, item):
        if self.is_full():
            return f'Full Queue'
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size += 1

    # Define DeQueue[Deletions from front End]
    def de_queue(self):
        if self.is_empty():
            return f'Empty Queue'
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    # Define Front Pointer Position Check
    def get_front(self):
        if self.is_empty():
            return f'Empty Queue'
        return self.Q[self.front]

    # Define Rear Pointer Check
    def get_rear(self):
        if self.is_empty():
            return f'Empty Queue'
        return self.Q[self.rear]

    # Define Display Queue
    def __str__(self):
        return str(self.Q)


if __name__ == '__main__':
    queue = Queue(5)
    queue.en_queue(10)
    queue.en_queue(20)
    queue.en_queue(30)
    queue.en_queue(40)
    queue.en_queue(50)
    print('Current Queue:', queue)
    print('Queue Size:', queue.size)
    print('Queue Front:', queue.front, f'[{queue.Q[queue.front]}]')
    print('Queue Rear:', queue.rear, f'[{queue.Q[queue.rear]}]')
    print('-' * 50)
    queue.de_queue()
    print('Current Queue:', queue)
    print('Queue Size:', queue.size)
    print('Queue Front:', queue.front, f'[{queue.Q[queue.front]}]')
    print('Queue Rear:', queue.rear, f'[{queue.Q[queue.rear]}]')
