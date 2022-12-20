# -*- coding: utf-8 -*-

str = "Python is amazing"

#change lower
print(str.lower())
#change upper
print(str.upper())
#check up
print(str.isupper())
#check low
print(str.islower())
#check length
print(len(str))
#replace
print(str.replace("Python","파이썬"))
#첫번 째로 나오는 해당 문자 인덱스 찾기
print(str.index("a"))
print(str.index("a",str.index("a")+1))
print(str.find("a"))
print(str.find("a",str.find("a")+1))
print(str.find("파"))
#해당 문자의 개수
print(str.count("is"))