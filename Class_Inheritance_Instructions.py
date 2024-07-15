class Animal:
    def __init__(self, eat, sleep) -> None:
        self.eat = eat
        self.sleep = sleep
        
    def eat(self):
        return f"big bowl"
    
    def sleep(self):
        return f"sleep on fluffy bed"
    
    def noise(self):
        print("WAHWAHfapsompowe")


class Dog(Animal):
    def __init__(self, eat, sleep) -> None:
        super().__init__(eat, sleep)
        self.eat = eat
        self.sleep = sleep

    def noise(self):
        super().__init__()
        print("WOOF!")
    
    
dog = Dog("Kibble", "Snore")
dog_sound = dog.noise
print(f"Dogs {dog_sound} after eating {dog.eat} then {dog.sleep}")