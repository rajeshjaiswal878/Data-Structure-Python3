'''
Given a string, remove the punctuation from the string if
the given character is a punctuation character as classified by the current C locale.
The default C locale classifies these characters as punctuation:

!"#$%&'()*+,-./:;?@[\]^_`{|}~
Examples:

Input : %welcome' to @geeksforgeek<s
Output : welcome to geeksforgeeks

Input : Hello!!!, he said ---and went.
Output : Hello he said and went
'''

import string


def remove_punctuation_string(in_p):
    res = [ch for ch in in_p if ch not in string.punctuation]
    return ''.join(res)


res = remove_punctuation_string('''Hello!!!, he said ---and went''')
print('String With Out Punctuations:', res)
