'''
We are given a binary string containing 1’s and 0’s.
Find maximum length of consecutive 1’s in it.

Examples:
Input : str = '11000111101010111'
Output : 4
'''


def maximum_ones_length(input_str):
    return max(map(len, input_str.split('0')))


input_str = '11000111101010111'
res = maximum_ones_length(input_str)
print(f'Maximum Ones Length Is :{res}')
