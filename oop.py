class Dog:
  def speak(self):
    return "Woof!"

class Cat:
  def speak(self):
    return "Meow!"

class Cow:
  def speak(self):
    return "Moo!"

class AnimalFactory:
  @staticmethod
  def get_animal(animal_type):
    if animal_type == "dog":
      return Dog()
    elif animal_type == "cat":
      return Cat()
    elif animal_type == "cow":
      return Cow()
    else:
      raise ValueError(f"Unknown animal type: {animal_type}")

for animal_type in ["dog", "cat", "cow"]:
  animal = AnimalFactory.get_animal(animal_type)
  print(f"The {animal_type} says: {animal.speak()}")          