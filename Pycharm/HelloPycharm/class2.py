#상속: 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
#부모와 자식 관계가 존재
#자식 클래스: 부모 클래스를 상속 받은 클래스

class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다. [전투력:", self.power, "]")

unit = Unit("홍길동", 375)
unit.attack()

#상속
class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터 이름:", self.name, "/ 몬스터 종류:", self.type)

monster = Monster("슬라임", 10, "초급")
monster.show_info()  #자식 클래스의 메소드는 부모에서는 이용할 수 없지만 자식에서는 사용가능
monster.attack()  #부모 클래스인 Unit에 attack 함수가 있기 때문에 사용 가능