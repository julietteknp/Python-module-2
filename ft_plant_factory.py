if __name__ == "__main__":
    class Plant:
        def __init__(self, name, size, age):
            self.name = name
            self.size = size
            self.age = age
        def show(self):
            print(f"Created: {self.name.capitalize()}: {self.size}cm, {self.age} days old")
    plant1 = Plant("Rose", 25.0 , 30)
    plant2 = Plant("Oak", 200.0 , 365)
    plant3 = Plant("Cactus", 5.0 , 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)

    plants = [plant1, plant2, plant3, plant4, plant5]
    
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()

