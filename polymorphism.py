class Animal:
    """Base class for animals"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def move(self):
        pass
    
    def make_sound(self):
        pass
    
    def get_info(self):
        return f"{self.name} (Age: {self.age})"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def move(self):
        return f" {self.name} is running on four legs!"
    
    def make_sound(self):
        return f" {self.name} says: Woof! Woof!"
    
    def get_info(self):
        return f"{self.name} the {self.breed} (Age: {self.age})"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def move(self):
        return f" {self.name} is sneaking silently!"
    
    def make_sound(self):
        return f" {self.name} says: Meow!"
    
    def get_info(self):
        return f"{self.name} the {self.color} cat (Age: {self.age})"

class Bird(Animal):
    def __init__(self, name, age, wingspan_cm):
        super().__init__(name, age)
        self.wingspan_cm = wingspan_cm
    
    def move(self):
        return f" {self.name} is flying high in the sky!"
    
    def make_sound(self):
        return f" {self.name} says: Tweet! Tweet!"
    
    def get_info(self):
        return f"{self.name} (Wingspan: {self.wingspan_cm}cm, Age: {self.age})"

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type
    
    def move(self):
        return f" {self.name} is swimming gracefully in {self.water_type} water!"
    
    def make_sound(self):
        return f" {self.name} makes: Blub blub!"
    
    def get_info(self):
        return f"{self.name} the {self.water_type} fish (Age: {self.age})"

class Snake(Animal):
    def __init__(self, name, age, length_meters):
        super().__init__(name, age)
        self.length_meters = length_meters
    
    def move(self):
        return f" {self.name} is slithering on the ground!"
    
    def make_sound(self):
        return f" {self.name} hisses: Ssssss!"

    def get_info(self):
        return f"{self.name} ({self.length_meters}m long, Age: {self.age})"

def demonstrate_polymorphism():
    
    # Creating different animal objects
    animals = [
        Dog("Buddy", 3, "Golden Retriever"),
        Cat("Whiskers", 2, "Orange"),
        Bird("Sky", 1, 25),
        Fish("Nemo", 1, "saltwater"),
        Snake("Slippy", 4, 2.5)
    ]
    
    print("Watch how different animals move and make sounds:\n")
    
    for animal in animals:
        print(f"{animal.get_info()}")
        print(f"Movement: {animal.move()}")
        print(f"Sound: {animal.make_sound()}")
        print("-" * 50)

def animal_movement_show():
    print("Type 'show' to see all animals move, or 'quit' to exit\n")
    
    animals = [
        Dog("Max", 5, "German Shepherd"),
        Cat("Luna", 3, "Black"),
        Bird("Eagle", 2, 30),
        Fish("Goldie", 1, "freshwater"),
        Snake("Python", 6, 3.0)
    ]
    
    while True:
        command = input("Enter command: ").lower()
        
        if command == 'quit':
            print("Thanks for watching the animal show!")
            break
        elif command == 'show':
            for animal in animals:
                print(animal.move())
                print()
        else:
            print("Invalid command. Type 'show' or 'quit'")

if __name__ == "__main__":
    demonstrate_polymorphism()
    animal_movement_show()
