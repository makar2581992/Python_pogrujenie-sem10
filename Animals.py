class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

class Bird(Animal):
    def __init__(self, name: str, age: int, bird_type: str):
        super().__init__(name, age)
        self.bird_type = bird_type

    def __str__(self):
        return f"{super().__str__()} {self.bird_type}"


class Dog(Animal):
    def __init__(self, name: str, age: int, dog_type: str):
        super().__init__(name, age)
        self.dog_type = dog_type

    def __str__(self):
        return f"{super().__str__()} {self.dog_type}"

class Fish(Animal):
    def __init__(self, name: str,  age: int, fish_type: str):
        super().__init__(name, age)
        self.fish_type = fish_type

    def __str__(self):
        return f"{super().__str__()} {self.fish_type}"


if __name__ == '__main__':
    dog = Dog("Jack",  1, "Такса")
    bird = Bird("Jessy", 3, "penguin")
    print(dog)
    print(bird)
