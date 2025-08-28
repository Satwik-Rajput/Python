class animal():
    pass


class pet(animal):
    pass


class dog(pet):
    @staticmethod
    def bark():
        bark = "Bow-Bow"
        print(bark)
d = dog()
d.bark()