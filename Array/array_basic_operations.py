import array as arr

from icecream import ic

data = arr.array('i', [1, 2, 3, 4, 5, 1])
print(data)
ic(data)
print('--------' * 5 + 'Operations' + '--------' * 5)
data.append(6)
print('After Addition of New Item To Array:', data)
data.insert(2, 11)
print('After Addition Of New Item At Specific Location:', data)
data.pop()
print('After Removal Of Last Item From Array:', data)
data.pop(3)
print('After Removal Of Item From Specific Location:', data)
data.remove(1)
print('After Removal Of First Occurrence Of Given Item:', data)
res = data.index(5)
print('1st Index Of Passed Item In Array:', res)
data.reverse()
print('After Reversal Array:', data)

''' 
Sample Output:
array('i', [1, 2, 3, 4, 5, 1])
ic| data: array('i', [1, 2, 3, 4, 5, 1])
----------------------------------------Operations----------------------------------------
After Addition of New Item To Array: array('i', [1, 2, 3, 4, 5, 1, 6])
After Addition Of New Item At Specific Location: array('i', [1, 2, 11, 3, 4, 5, 1, 6])
After Removal Of Last Item From Array: array('i', [1, 2, 11, 3, 4, 5, 1])
After Removal Of Item From Specific Location: array('i', [1, 2, 11, 4, 5, 1])
After Removal Of First Occurrence Of Given Item: array('i', [2, 11, 4, 5, 1])
1st Index Of Passed Item In Array: 3
After Reversal Array: array('i', [1, 5, 4, 11, 2])
'''
