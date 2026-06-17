if __name__ == "__main__":
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self._height = height
            self._age = age
        def set_age(self, x):
            if x >= 0:
                self._age = x
            else:
                print("Error")
        def set_height(self, y):
            if y >= 0:
                self._height = y
            else:
                print("Error")
        def get_age(self):
            return self._age
        def get_height(self):
            return self._height
        def aging(self, days):
            self._age += days
        def growing(self, days):
            self._height += 2*days + 2
        def show(self):
            print(f"{self.name.capitalize()}: {self.get_height()}cm, {self.get_age()} days old")
    
    class Flower(Plant):
        def __init__(self, name, height, age, color):
            super().__init__(name, height, age)
            self._color = color
        def show(self):
            super().show()
            print(f"Color: {self._color}")
        def bloom(self):
            print("Rose is blooming beautifully!")

    class Tree(Plant):
        def __init__(self, name, height, age, trunk):
            super().__init__(name, height, age)
            self._trunk = trunk
        def show(self):
            super().show()
            print(f"Trunk diameter: {self._trunk}cm")
        def shade(self):
            print("[asking the oak to produce shade]")
            print(f"Tree Oak now produces a shade of {self._height}cm long and {self._trunk}cm wide.")

    
    class Vegetable(Plant):
        def __init__(self, name, height, age, harvest, nutritional):
            super().__init__(name, height, age)
            self._harvest = harvest
            self._nutritional = nutritional
        def growing(self, days):
            super().growing(days)
            self._nutritional += 20
        def show(self):
            super().show()
            print(f"Harvest season: {self._harvest}")
            print(f"Nutritional value: {self._nutritional}")


    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower1=Flower("Rose", 15, 10, "red")
    flower1.show()
    print("Rose has not bloomed yet \n[asking the rose to bloom]")
    flower1.show()
    flower1.bloom()
    print("\n=== Tree")
    tree1=Tree("Oak", 200, 365, 5.0)
    tree1.show()
    tree1.shade()
    print("\n=== Vegetable")
    vegetable1 = Vegetable("Tomato", 5, 10, "April", 0)
    vegetable1.show()
    print("[make tomato grow and age for 20 days]")
    vegetable1.aging(20)
    vegetable1.growing(20)
    vegetable1.show()

    
