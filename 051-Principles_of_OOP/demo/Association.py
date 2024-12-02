class Human:
    def __init__(self,name,heart):
        self.name = name
        self.__heart = heart
    def get_heart(self):
        print(f"{self.name}: Ouch,owie.")
        return self.__heart

class Heart:
    def __init__(self,bpm,type_of_heart):
        self.__bpm = bpm
        self.__type = type_of_heart
    def information(self):
        print(f"Interesting, a heart that can reach up to {self.__bpm} and is {self.__type}")

if __name__ == "__main__":
    human = Human("George",Heart(200,"Impure"))
    ritualistic_sacrifice_result = human.get_heart()
    ritualistic_sacrifice_result.information()
