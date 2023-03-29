class Cat:
    biology_class = "Animal"
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
    def jump(self):
        return "I can jump!"
    def get_name(self):
        return f"Hello! My name is {self.name}"
    def set_name(self, new_name):
        self._name = new_name

cat1 = Cat("Murzik", 1, "red")
print(cat1.name)
print(cat1.get_name())
print(cat1.color)
print(cat1.biology_class)

cat2 = Cat("Barsik", 3, "black")
print(cat2.biology_class)
print(cat2.get_name())
cat2._name = "Martusik"
print(cat2._name)
