class AirPlane:
    def __init__(self):
        print("비행기 클래스가 생성되었습니다.")
    def tack_off(self):
        print("비행기가 이륙합니다.")
    def fly(self):
        print("비행기가 일반 비행합니다.")
    def land(self):
        print("비행기가 착륙합니다.")

# air1 = AirPlane()
# air1.tack_off()
# air1.fly()
# air1.land()

class SuperSonicAirPlane(AirPlane):
    # 비행모드 1 - NORMAL, 2 - SUPERSONIC
    NORMAL = 1
    SUPERSONIC = 2
    # 멤버 변수 선언 - 비행모드
    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.SUPERSONIC
    def fly(self):
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC:
            print("비행기가 초음속 비행합니다")
        else:
            super().fly()

sa = SuperSonicAirPlane()
sa.fly()
sa.fly_mode = 1
sa.fly()
sa.land()