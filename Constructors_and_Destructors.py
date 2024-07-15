class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self,age = age

    def __del__(self):
        return f"Farewell {self.name}"
    