'''
Given a string check if it is Pangram or not.
A pangram is a sentence containing every letter in the English Alphabet.

Examples : The quick brown fox jumps over the lazy dog ”
is a Pangram [Contains all the characters from ‘a’ to ‘z’]
“The quick brown fox jumps over the dog”
is not a Pangram [Doesn’t contains all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing]
'''

import string


# Just By Check Size Of Unique Character if all character in String Without any symbol and digits
def check_pan_gram(in_p):
    res = set([ch for ch in in_p.lower() if ch in string.ascii_letters])
    return 'No Pangram' if len(res) < 26 else 'Pangram'


res = check_pan_gram('The quick brown fox jumps over the dog')
print(res)
