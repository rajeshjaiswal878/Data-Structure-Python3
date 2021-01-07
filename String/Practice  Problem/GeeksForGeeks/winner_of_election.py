'''
Given an array of names of candidates in an election.
A candidate name in the array represents a vote cast to the candidate.
Print the name of candidates received Max vote.
If there is tie, print a lexicographically smaller name.
Examples:
Input :  votes = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]
Output : John
'''
from collections import Counter

from icecream import ic


def winner_of_election(input):
    result = {}
    for el in input:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1
    return sorted(result.items(), key=lambda x: (-x[1], x[0]))[0]


votes = ["john", "johnny", "jackie",
         "johnny", "john", "jackie",
         "jamie", "jamie", "john",
         "johnny", "jamie", "johnny",
         "john"]
res = winner_of_election(votes)
print(f'Winner Is {res}')

data = Counter(votes)
ic(data)
print(data[0])