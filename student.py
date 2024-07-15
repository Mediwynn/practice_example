class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display_info(self):
        info = f"Student name: {self.name}  Student age: {self.age}"
        display = print(info)
        return display
    
    