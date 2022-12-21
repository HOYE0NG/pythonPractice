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

#자료구조 변경
lst = [1,2,3,3]
print(lst)
print(type(lst))
tpl = tuple(lst)
print(tpl)
print(type(tpl))
st = set(tpl)
print(st)
print(type(st))
lst = list(st)
print(lst)
print(type(lst))

#if문
# temp = int(input("오늘 기온은? "))
temp = 30
if temp >=30 :
    print("덥습니다.")
elif temp>=10 and temp<30:
    print("딱 좋습니다.")
else :
    print("춥습니다.")
    
#for문
for i in range(5):
    print(i)
for i in range(1,6):
    print(i)
lst = [1,2,3,4,5]
for i in lst :
    print(i)
lst.clear()
lst = ["유리", "수영", "태연"]
for cus in lst:
    print("{0}님, 커피가 준비되었습니다.".format(cus))
    print(f"{cus}님, 토스트가 준비되었습니다.")
    
#while문
index = 10
while(index>0):
    print(index)
    if(index==8):
        print("continue")
        index -= 1
        continue
    elif(index==5):
        print("break")
        break
    print("출력")
    index -= 1

#한줄 for문
std = [1,2,3,4,5]
print(std)
std = [i+100 for i in std]
print(std)
std = ["nhy", "jssss", "jackson", "danaka"]
print(std)
std = [i.upper() for i in std]
print(std)
std = [len(i) for i in std]
print(std)

# 당신은 코코아 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다.

from random import *

cuss = [randint(5,51) for i in range(50)]
i = 0
cnt = 0
for cus in cuss:
    i += 1
    if(cus<15):
        print(f"[O] {i}번째 손님 (소요시간 : {cus}분)")
        cnt += 1
    else:
        print(f"[ ] {i}번째 손님 (소요시간 : {cus}분)")
print("총 탑승 승객 : {0} 분".format(cnt))

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money

deposit(300,100)    

balance = 0
balance = deposit(balance, 10000)
print(balance)

def withdraw(balance, money):
    if(balance > money):
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.",format(balance))
        return balance

balance = withdraw(balance, 5000)

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

#함수 기본값
def profile(name, age=17, main_lang="파이썬"):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

profile("유재석")
profile("김태호")

#키워드값
def profile2(name, age, main_lang):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

profile(name="유재석", age=20,main_lang="파이썬")
profile(age=20, name="유재석", main_lang="파이썬")

