from models import Animal, Dog, Cat

untitledAnimal = Animal("undefined", 10, "red")
bobikDog = Dog("Bobik", 9, "black")
vasyaCat = Cat("Vasiliy", 11, "tabby brown")

animalList = [untitledAnimal, bobikDog, vasyaCat]

for animal in animalList:
    print(animal)
    animal.speak()
    
    if isinstance(animal, Dog):
        animal.chaseCats()
    elif isinstance(animal, Cat):
        animal.stealFood()
    
    if isinstance(animal, Animal):
        animal.sleep()
    
    print("*", "-" * 5, "*")