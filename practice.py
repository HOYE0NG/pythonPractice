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

#문자열 포맷팅
print("a"+"b") #붙여쓰기
print("a","b") #?
# % 사용
print("나는 %d살입니다." %20) #한 개 포맷팅
print("나는 %d살이고 %s를 좋아합니다." % (20, "사과")) #두 개 이상 포맷팅
# {} 사용
print("나는 {}살이고 {}를 좋아합니다." .format(20,"사과"))
print("나는 {1}살이고 {0}를 좋아합니다.".format("사과",20))
print("나는 {age}살이고 {fruit}를 좋아합니다.".format(age=20, fruit="사과"))

# f 사용 (~3.6v)
age = 20
fruit = "사과"
print(f"나는 {age}살이고 {fruit}를 좋아해요.")

# etc + 탈출문자
print("""i 
do
soccer""") #여러 줄 출력
print("i do \tsoccer") #tab
print("i do \nsoccer") #enter
print("\\") #\\ 역슬래쉬 출력
print("red apple\rpine") #\r 커서 이동
print("apple") #\b 백스페이스 한글자 삭제

#리스트
lst = ["유재석", "강호동", "박명수"]
print(lst)
#리스트 인덱스
print(lst.index("박명수"))
#리스트 추가
lst.append("하하")
print(lst)
#리스트 삽입
lst.insert(1,"조세호")
print(lst)
#리스트 제거
print(lst.pop())
print(lst)
#몇개 원소 있는지 확인
print(lst.count("유재석"))
print(lst.count("길"))
#정렬
numLst = [4,2,5,1,3]
numLst.sort()
print(numLst)
#순서뒤집기
numLst.reverse()
print(numLst)
#리스트 확장
numLst.extend(lst)
print(numLst)

#사전
dic = {"C-1":"유재석", "C-2":"하하"}
print(dic)
#가져오기
print(dic["C-1"])
print(dic.get("C-1"))
# print(dic["C-3"]) <-- 오류
print(dic.get("C-3")) #오류 아님
print(dic.get("C-3","사용 가능")) #디폴트값 설정
print("C-3" in dic) #값 있는지 확인
#추가
dic["C-3"] = "박명수"
dic["C-4"] = "길"
print(dic)
#삭제
del dic["C-3"]
print(dic)
del dic["C-4"]
print(dic)
#key 값 출력
print(dic.keys())
#values 값 출력
print(dic.values())
#key-values 출력
print(dic.items())
#전부 삭제
dic.clear()
print(dic)

 #튜플
 #변경 불가하지만 속도가 빠름
tpl = ("돈까스", "치즈까스")
print(tpl)
name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)
name,age,hobby = "김종국",20,"코딩"
print(name,age,hobby)
name = "유재석"
print(name,age,hobby)

#집합
mySet = {1,2,3,3,3}
print(mySet)
java = {"카이", "백현", "세훈"}
python =set(["카이", "시우민"])
#교집합
print(java&python)
print(java.intersection(python))
#합집합
print(java|python)
print(java.union(python))
#차집합
print(java - python)
print(java.difference(python))
#추가
python.add("백현")
print(python)
#삭제
java.remove("카이")
print(java) 