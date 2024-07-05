"""
多態
"""


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


print("#####################################")


class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制熱"""
        pass

    def swing_l_r(self):
        """左右擺風"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空調制冷")

    def hot_wind(self):
        print("美的空調制熱")

    def swing_l_r(self):
        print("美的空調左右擺風")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空調制冷")

    def hot_wind(self):
        print("格力空調制熱")

    def swing_l_r(self):
        print("格力空調左右擺風")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)