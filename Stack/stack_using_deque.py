from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def __str__(self):
        return str(self.stack)

    def push(self, val):
        return self.stack.append(val)

    def push_left(self, val):
        return self.stack.appendleft(val)

    def pop(self):
        return self.stack.pop()

    def pop_left(self):
        return self.stack.popleft()

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(11)
    stack.push(12)
    stack.push(13)
    stack.push_left(21)
    stack.push_left(22)
    stack.push_left(23)
    print('Complete Stack:', stack)
    stack.pop()
    print('After Pop:', stack)
    stack.pop_left()
    print('After Pop Left:', stack)
    print('Top Element:', stack.top())
    print('Stack Size:', stack.size())
    stack.push(15)
    print('Stack Size:', stack)

''' 
Output Sample:
Complete Stack: deque([23, 22, 21, 11, 12, 13])
After Pop: deque([23, 22, 21, 11, 12])
After Pop Left: deque([22, 21, 11, 12])
Top Element: 12
Stack Size: 4
Stack Size: deque([22, 21, 11, 12, 15])
'''
