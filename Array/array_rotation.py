import array as arr

from icecream import ic

data = arr.array('i', [1, 2, 3, 4, 5, 7, 8, 9])
print(data)
ic(data)


def rotate_array_method_one(arr, n, d):
    temp = arr[:d]
    new_data = arr[d:]
    data = new_data + temp
    print(data)


def rotate_caller(arr, n, d):
    for i in range(d):
        rotate_array_by_one(arr, n)
    return arr


def rotate_array_by_one(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


n = len(data)
d = 3
res = rotate_caller(data, n, d)
print(res)
