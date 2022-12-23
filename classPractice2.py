class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
class AttackUnit(Unit): #상속
    def __init__(self, name, hp, damage):
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp) #부모 클래스 생성자
        self.damage = damage
    
    def attack(self, location):
        print("{0} : attack {1} [damage {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} 데미지를 입었습니다.".format(damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{} 유닛이 파괴되었습니다.".format(self.name))



#다중상속        
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다.".format(self.name, location))
        
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
        
        
valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name, "3시")

#pass : 아무것도 안하고 그냥 넘어감
class BuildingUnit(Unit, Flyable):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        #super()은 부모를 뜻하지만 다중 상속일 때는 못쓴다.
    