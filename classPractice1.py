#스타크래프트
#클래스 : 붕어빵 틀

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank1 = Unit("탱크", 150, 30)

#__init__ : 생성자 

#멤버 변수
wraith = Unit("레이스",80, 5)
wraith.clocking = True #외부에서 멤버 변수를 생성하거나 초기화 가능

if wraith.clocking:
    print("{}은 현재 클로킹 상태입니다.".format(wraith.name))
    
#메서드

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def attack(self, location):
        print("{}:{} 방향으로 적군을 공격합니다.[공격력:{}]".\
            format(self.name, location, self.damage))

    
    def damaged(self, damage):
        print("{}:{} 대미지를 입었습니다..".\
            format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 채력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

firebat = AttackUnit("파이어뱃",50,16)
firebat.attack("5시")

firebat.damaged(25)
firebat.damaged(25)


