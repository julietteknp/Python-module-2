if __name__ == "__main__":
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

        def show(self):
            print(self.name, ":", self.height, ",", self.age)

    plant1 = Plant("Rose", "25cm", "3 days old")
    plant2 = Plant("Sunflower", "80cm", "45 days old")
    plant3 = Plant("Cactus", "15cm", "120 days old")
    plant1.show()
    plant2.show()
    plant3.show()
        

        
