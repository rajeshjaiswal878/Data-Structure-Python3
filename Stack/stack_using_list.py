class Stack:
    def __init__(self, limit):
        self.limit = limit
        self.stack = [] * self.limit

    def __str__(self):
        return str(self.stack)

    def push(self, val):
        if self.size() == self.limit:
            return f'Stack Full'
        else:
            return self.stack.append(val)

    def pop(self):
        if self.size() == 0:
            return f'Stack Empty'
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]


if __name__ == '__main__':
    stack = Stack(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)
    print('Complete Stack:', stack)
    stack.push(14)
    print('After Push:', stack)
    stack.pop()
    print('After Pop:', stack)
    print('Top Element:', stack.top())
    print('Stack Size:', stack.size())
    stack.push(15)
    print('Stack Size:', stack)


''' 
Output Sample:
Complete Stack: [11, 12, 13]
After Push: [11, 12, 13, 14]
After Pop: [11, 12, 13]
Top Element: 13
Stack Size: 3
Stack Size: [11, 12, 13, 15]
'''
