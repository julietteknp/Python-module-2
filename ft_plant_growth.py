if __name__ == "__main__":
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

        def show(self):
            print(plant1.name, f"{self.height:.1f}", "cm", plant1.age, "days old")
        def grow(self):
            self.height = self.height + 0.8
        def aging(self):
            self.age = self.age + 1
        
    plant1 = Plant("rose", 25, 30)
    print("=== Garden Plant Growth ===")
    plant1.show()
    for i in range (1, 8):
        print("=== Day", i, "===")
        plant1.grow()
        plant1.aging()
        plant1.show()
       
        
                
