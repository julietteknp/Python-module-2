if __name__ == "__main__":
    class Plant:
        class Stats:
            def __init__(self):
                self._grow_calls=0
                self._age_calls=0
                self._show_calls=0
            def add_grow_calls(self, x):
                self._grow_calls += x
            def add_age_calls(self, x):
                self._age_calls += x
            def add_show_calls(self, x):
                self._show_calls += x
            def show_stats(self):
                print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")
        def __init__(self, name, height, age):
            self.name = name
            self._height = height
            self._age = age
            self._stats = Plant.Stats()
        @staticmethod
        def is_older_than_a_year(age):
            if (age > 365):
                print("Is",age,"days more than a year? -> True")
            else:
                print("Is",age,"days more than a year? -> False")
        @classmethod
        def anonymous(cls):
            return cls("Unknown plant", 0, 0)
        def get_age(self):
            return self._age
        def get_height(self):
            return self._height
        def aging(self, days):
            self._age += days
            self._stats.add_age_calls(1)
        def growing(self, height):
            self._height += height
            self._stats.add_grow_calls(1)
        def show(self):
            print(f"{self.name.capitalize()}: {self.get_height()}cm, {self.get_age()} days old")
            self._stats.add_show_calls(1)
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls=0
        def add_shade_calls(self, x):
            self._shade_calls += x
        def show_stats(self):
            super().show_stats()
            print(f"{self._shade_calls} shade")
    class Flower(Plant):
        def __init__(self, name, height, age, color):
            super().__init__(name, height, age)
            self._color = color
            self._has_bloomed = False
        def show(self):
            super().show()
            print(f"Color: {self._color}")
            if self._has_bloomed == False:
                print("Rose has not bloomed yet")
            if self._has_bloomed == True:
                print("Rose is blooming beautifully!")
        def bloom(self):
            self_has_bloomed = True
    class Seed(Flower):
        def __init__(self, name, height, age, color):
            super().__init__(name, height, age, color)
            self._n_seed = 0
        def bloom(self, x):
            super().bloom()
            self._n_seed += x
        def show(self):
            super().show()
            print(f"Seeds: {self._n_seed}")
    class Tree(Plant):
        def __init__(self, name, height, age, trunk):
            super().__init__(name, height, age)
            self._trunk = trunk
            self._stats = TreeStats()
        def show(self):
            super().show()
            print(f"Trunk diameter: {self._trunk}cm")
        def shade(self):
            self._stats.add_shade_calls(1)
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
    print("=== Check year-old")
    Plant.is_older_than_a_year(30)
    Plant.is_older_than_a_year(400)
    print("\n=== Flower")
    flower1=Flower("Rose", 15, 10, "red")
    flower1.show()
    print("[statistics for Rose]")
    flower1._stats.show_stats()
    print("[asking the rose to grow bloom]")
    flower1.growing(8)
    flower1.bloom()
    flower1.show()
    print("[statistics for Rose]")
    flower1._stats.show_stats()
    print("\n=== Tree")
    tree1=Tree("Oak", 200, 365, 5.0)
    tree1.show()
    tree1.shade()
    print("[statistics for Oaks]")
    tree1._stats.show_stats()
    print("\n=== Seed")
    seed1=Seed("Sunflower", 80.0, 45, "yellow")
    seed1.show()
    print("[make sunflower grow, age and bloom]")
    seed1.growing(30)
    seed1.aging(20)
    seed1.bloom(42)
    seed1.show()
    print(f"[statistics for {seed1.name}]")
    seed1._stats.show_stats()
    print("\n=== Vegetable")
    vegetable1 = Vegetable("Tomato", 5, 10, "April", 0)
    vegetable1.show()
    print("[make tomato grow and age for 20 days]")
    vegetable1.aging(20)
    vegetable1.growing(20)
    vegetable1.show()
    print("\n=== Anonymous")
    anonymous1=Plant.anonymous()
    anonymous1.show()
    print(f"[statistics for {anonymous1.name}]")
    anonymous1._stats.show_stats()

    
