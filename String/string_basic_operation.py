# Basic String Operations
# from icecream import ic

str_one = 'Rajesh Ashok Jaiswal Rajesh Ashok Jaiswal'
pat = 'Raj'
# ic(str_one)

print('Given String:', str_one)
print('Given Pattern:', pat)

# Find Operations
print('-' * 20)

# 1. Find 1st Position of {pat} in Given String syntax[ str.find(pat,start,end)]
print('1. 1st Find:', str_one.find(pat))

# 2. Find Last Position of {pat} in Given String syntax[str.rfind(pat,start,end)]
print('2. Last Find:', str_one.rfind(pat))

# B Start & End Check
print('-' * 20)

# 3. Starts with Check Does Given String Start With Pat
print('3. StartsWith:', str_one.startswith(pat))

# 4. EndsWith Check Does Given String Ends with Pat
print('4. Ends With:', str_one.endswith(pat))

# C Check Upper,Lower,Capitalize, Title Case
print('-' * 20)

# 5. Upper and Upper Check
print('5. Check All Upper:', str_one.isupper())
print('5. Convert To Upper:', str_one.upper())

# 6. Lower and Lower Check
print('6. Check All Lower:', str_one.islower())
print('6. Convert To Lower:', str_one.lower())

# 7. Title and Title Check
print('7. Check All Title:', str_one.istitle())
print('7. Convert To Title:', str_one.title())

# 8. Capitalize
print('8. Convert All Capitalize:', str_one.capitalize())

# 9. SwapCase
print('9. Convert All SwapCase:', str_one.swapcase())

# D Length Count
print('-' * 20)

# 10. Get The Length Of String
print(f'10. Length Of | {str_one} | Is:', len(str_one))

# 11. Count of Pattern In Given String
print(f'11. Count Of {pat} in String :', str_one.count(pat))

# E. Alignment Center,Left,Right
print('-' * 20)

# 12. Center Alignment in Given Space
print('12. Center Alignment in 20 Char "-" Space:', pat.center(20, '-'))

# 13. Left Alignment in Given Space
print('13. Left Alignment in 20 Char "-" Space:', pat.ljust(20, '-'))

# 14. Center Alignment in Given Space
print('14. Right Alignment in 20 Char "-" Space:', pat.rjust(20, '-'))

# F. Type of Characters In String
print('-' * 20)

# 15. Check Does All String is Alphabetical?
print('15. IS Alpha:', str_one.isalpha())

# 16. Check Does All String is Numerical
print('16. IS Digits:', str_one.isdigit())

# 17. Check Does String is Combination of Digits and Characters
print('17. Is Alpha Numerical:', str_one.isalnum())

# 18. Check Does All The Characters as Space
print('18. Is Space:', str_one.isspace())

# 19. Join Sequence OF String by Other String
pat_one = 'ABC'
pat_two = '-'
print('19. Join Sequence:', pat_two.join(pat_one))

# G. Striping Space and Other Characters
print('-' * 20)

# 20. Striping Both Left Right Side once
str_two = '---Rajesh---'
print('String with "-" non required Characters:', str_two)
# ic(str_two)
print('20. Strip Both Side:', str_two.strip('-'))

# 21. Striping Left Side
print('21. Strip Left Side:', str_two.lstrip('-'))

# 22. Striping Right Side
print('22. Strip Right Side:', str_two.rstrip('-'))

# H. Maximum ,Minimum Char In String
print('-' * 20)

# 23. Maximum Char By ORD Value
print('23 .Maximum Char In String:', max(str_one))

# 24. Minimum Char By ORD Value
print('24. Minimum Char In String:', min(str_one))

# I. Replace ,MakeTrans,Translate pat in  String
print('-' * 20)

# 25 Make Trans Mapping
pat_three = 'Um'
# mapped=# maketrans(pat_one,pat_three)
# print('Translate Using Mapped',str_one.translate(mapped))

# 26. Replace pat InString n Times
print('26. Replace n times:', str_one.replace(pat, pat_three, 2))

# 27. Expandtabs
str_three = 'Rajesh\tUmesh'
print('27 .Expand Tabs:', str_three.expandtabs(2))

''' 
Output Results:
Given String: Rajesh Ashok Jaiswal Rajesh Ashok Jaiswal
Given Pattern: Raj
--------------------
1. 1st Find: 0
2. Last Find: 21
--------------------
3. StartsWith: True
4. Ends With: False
--------------------
5. Check All Upper: False
5. Convert To Upper: RAJESH ASHOK JAISWAL RAJESH ASHOK JAISWAL
6. Check All Lower: False
6. Convert To Lower: rajesh ashok jaiswal rajesh ashok jaiswal
7. Check All Title: True
7. Convert To Title: Rajesh Ashok Jaiswal Rajesh Ashok Jaiswal
8. Convert All Capitalize: Rajesh ashok jaiswal rajesh ashok jaiswal
9. Convert All SwapCase: rAJESH aSHOK jAISWAL rAJESH aSHOK jAISWAL
--------------------
10. Length Of | Rajesh Ashok Jaiswal Rajesh Ashok Jaiswal | Is: 41
11. Count Of Raj in String : 2
--------------------
12. Center Alignment in 20 Char "-" Space: --------Raj---------
13. Left Alignment in 20 Char "-" Space: Raj-----------------
14. Right Alignment in 20 Char "-" Space: -----------------Raj
--------------------
15. IS Alpha: False
16. IS Digits: False
17. Is Alpha Numerical: False
18. Is Space: False
19. Join Sequence: A-B-C
--------------------
String with "-" non required Characters: ---Rajesh---
20. Strip Both Side: Rajesh
21. Strip Left Side: Rajesh---
22. Strip Right Side: ---Rajesh
--------------------
23 .Maximum Char In String: w
24. Minimum Char In String:  
--------------------
26. Replace n times: Umesh Ashok Jaiswal Umesh Ashok Jaiswal
27 .Expand Tabs: Rajesh  Umesh

Process finished with exit code 0

'''
