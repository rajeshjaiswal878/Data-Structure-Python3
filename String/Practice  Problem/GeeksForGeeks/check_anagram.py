str1 = 'abcd'
str2 = 'bdce'


def check_anagram(str1_p, str2_p):
    sum = 0
    if len(str1_p) != len(str2_p):
        return 'Not Anagram'
    else:
        for i in range(len(str1_p)):
            sum = sum + ord(str1_p[i])
            sum = sum - ord(str2_p[i])
        if sum == 0:
            return 'Anagram'
        else:
            return 'Not Anagram'


res = check_anagram(str1, str2)
print('AnaGram Check:', res)
