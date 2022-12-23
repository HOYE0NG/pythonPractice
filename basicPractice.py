# -*- coding: utf-8 -*-

string = "Python is amazing"

#change lower
print(string.lower())
#change upper
print(string.upper())
#check up
print(string.isupper())
#check low
print(string.islower())
#check length
print(len(string))
#replace
print(string.replace("Python","파이썬"))
#첫번 째로 나오는 해당 문자 인덱스 찾기
print(string.index("a"))
print(string.index("a",string.index("a")+1))
print(string.find("a"))
print(string.find("a",string.find("a")+1))
print(string.find("파"))
#해당 문자의 개수
print(string.count("is"))

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

#가변 인자 "*"
def profile3(name, age, l1, l2, l3, l4, l5):
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    print(l1, l2, l3, l4, l5)

profile3("유재석",20,"파이썬","자바","C","C++","C#")
profile3("김태호",24,"파이썬","자바","","","")

def profile4(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()
    
profile4("유재석",20,"파이썬","자바","C","C++","C#")
profile4("김태호",24,"파이썬","자바")

#지역변수와 전역변수

gun = 10

# def checkpoint(soldiers):
#     gun = gun - soldiers <-- 전역 변수를 안에서 사용
#     print(f"[함수 내] 남은 총 : {gun}")
    
# print(f"전체 총 : {gun}")
# checkpoint(2)
# print(f"전체 총 : {gun}")

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")

print(f"전체 총 : {gun}")
checkpoint(2)
print(f"전체 총 : {gun}")

#일반적으로 전역 변수를 많이 사용하면 함수 관리가 어려워진다.
#따라서 파라미터로 넘겨주고 값을 받아서 사용하는 편이 더 권장됨.

#퀴즈
# 표준 체중을 구하는 프로그램
# 남자 : 키 * 키 * 22
# 여자 : 키 * 키 * 22

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# 조건 2 : 전달값 : 키, 성별
# 조건 3 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if(gender=="여자"):
        height /= 100
        weight = round(height*height*21,2)
        print(f"키 {int(height*100)}cm 여자의 표준 체중은 {weight}kg 입니다.")
    else:
        height /= 100
        weight = round(height*height*22,2)
        print(f"키 {int(height*100)}cm 남자의 표준 체중은 {weight}kg 입니다.")

std_weight(175,"남자")
std_weight(160,"여자")

#표준 입출력
print("Python", "Java", "JavaScript", sep=",", end="?")
print("무엇이 더 재밌을까요?")
import sys
print("Python", "Java", file=sys.stdout) #표준 출력
print("Python", "Java", file=sys.stderr) #표준 에러

#시험 성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 50}
for subject, score in scores.items(): #keys = subject, values = score 튜플로 보내준다
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4),sep=":")
    #just(n) n칸의 공백을 확보하고 정렬
    
#은행 대기 순번표
#001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
    #zfill(n) n칸의 공백을 확보하고 나머지 왼 쪽은 0을 채움

#표준 입력
# answer = input("아무 값이나 입력하세요 : ") #항상 str로 나옴
# print(f"입력하신 값은 {answer}입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0:>10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시(부호를 표시함)
print("{0:>+10}".format(500))
print("{0:>+10}".format(-500))
#왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
print("{0:_<10}".format(500))
print("{0:<10}".format(500))
#3자리 마다 콤마를 찍어주기
print("{0:+,}".format(1000000000))
#3자리 마다 콤마를 찍어주고 부호도 붙이고 자릿수 확보하기
#빈자리는 ^ 로 채우기
print("{0:^<+30,}".format(1000000000)) 
#소수점 출력 + 특정 자리수
print("{0:.3f}".format(5/3))


#파일 입출력
# score_file = open("score.txt","w",encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 0", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #a:이어붙여서쓰기
# score_file.write("과학 : 80") #줄바꿈 없음
# score_file.write("\n코딩 : 100")

#읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.r ead())
# score_file.close()

#한줄씩 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한줄 읽고나서 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 몇줄인지 모를때 파일 다 읽기
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line: #반환값 부울값
#         break
#     print(line,end="")
# score_file.close()

#list에 읽기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
print
for line in lines:
    print(line, end="")
score_file.close()

#pickle
#프로그램 상에서 데이터를 파일 상으로 저장시키고 읽어들임
#binary type
#no need set encoding

# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수", "나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# #프로필에 있는 정보를 file에 저장함
# profile_file.close()
import pickle
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) #불러와서 읽음
print(profile)
profile_file.close()

#with
#import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
    #close를 해줄 필요가 없음

#파일 쓰기
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 공부했습니다.")

#파일 읽기
with open("study.txt", "r", encoding="utf8") as read_study_file:
    print(read_study_file.read())


#퀴즈
#주차별 보고서 템플릿 만들기

# for i in range(1,51):
#     report_file = open(f"{i} 주차.txt","w",encoding="utf8")
#     print(f"- {i}주차 주간보고 -",file=report_file)
#     print("부서 :",file=report_file)
#     print("이름 :",file=report_file)
#     print("업무 요약 :",file=report_file)
#     report_file.close() 



#클래스

    

    