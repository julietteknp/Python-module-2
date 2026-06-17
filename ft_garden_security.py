if __name__ == "__main__":
    class Plant:
        def __init__(self, name, height, age):
            self._name = name
            self._height = height
            self._age = age       
        def set_height(self, x):
            if x >= 0:
                self._height = x
                print(f"Height updated: {self._height}cm")
            else:
                print("Error, height can’t be negative \nHeight update rejected")
        def set_age(self, y):
            if y >= 0:
                self._age = y
                print(f"Age updated: {self._age} days")
            else:
                print("Error, age can’t be negative \nAge update rejected")
        def get_height(self):
            return self._height
        def get_age(self):
            return self._age
        def show(self):
            print(f"{plant1._name}: {plant1.get_height()}cm, {plant1.get_age()} days old")
 
    plant1 = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    plant1.show()
    print()
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-5)
    plant1.set_age(-10)
    print()
    print("Current state: ", end=" ")
    plant1.show()
