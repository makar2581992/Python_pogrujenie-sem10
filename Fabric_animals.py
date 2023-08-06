# 1.Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

from Animals import Animal, Dog, Bird, Fish


class AnimalsCreator:

    @staticmethod
    def create_animal(name: str, age: int):
        return Animal(name, age)

    @staticmethod
    def create_bird(name: str, age: int, bird_type: str):
        return Bird(name, age, bird_type)

    @staticmethod
    def create_dog(name: str, age: int, dog_type: str):
        return Dog(name, age, dog_type)

    @staticmethod
    def create_fish(name: str, age: int, fish_type: str):
        return Fish(name, age, fish_type)


if __name__ == '__main__':
    jack = AnimalsCreator.create_dog('Джек', 5, 'Питбуль')
    print(jack)
    freddy = AnimalsCreator.create_fish('Фредди', 1, 'Камбала')
    print(freddy)
    # anim = AnimalsCreator.create_animal('Кто-то', 30, 4)
    # print(anim)