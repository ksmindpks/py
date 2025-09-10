# 클래스 관계

# 1. 사용 (Use)
# 내(이름)가 지하철을 타고 가는 상황

class Person:
    def __init__(self, name):
        self.name = name
    
    def take(self, subway):
        print(f'{self.name}가 {subway.line}라인 지하철을 타고간다')

class Subway:
    def __init__(self, line):
        self.line = line

me = Person('PKS')
print(me.name)

my_line = Subway('신림선')
print(my_line.line)

me.take(my_line)

# 2. 포함 (Composition)
# 이전 지하철 역에서 출발했다

class Operation:
    def start(self):
        print("이전 역에서 출발했다")

class Subway2:  # 이름 충돌 방지를 위해 Subway2로 변경
    def __init__(self, line):
        self.line = line
        self.operation = Operation()
    
    def take(self):
        self.operation.start()
        print(f"{self.line} 지하철을 탈거다")

my_subway = Subway2('2호선')

my_subway.take()

# 3. 상속 (Inheritance): 부모가 가진 필드(변수), 메소드 상속
# 지하철(부모) - 기차(자식)
# 기차는 지하철의 한 종류다

class Train(Subway2):
    def __init__(self, line):
        super().__init__(line)  # 부모 클래스의 초기화 메소드 호출
        print(f"{line} 기차가 생성되었습니다")

train = Train('신림선')

train.take()