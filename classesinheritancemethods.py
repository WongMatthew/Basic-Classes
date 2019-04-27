# classesinheritancemethods.py
# Matt Wong
# April 18, 2019

class Mammal():
    def __init__(self):
        print("A mammal has been born")
        name = ""
    def make_noise(self):
        print("Grrrrr says " + self.name)
    def eat(self):
        print("Nom nom nom")
    
class Dog(Mammal):
    def __init__(self):
        print("A dog has been born")
    def make_noise(self):
        print("Bark says " + self.name)

class Cat(Mammal):
    def __init__(self):
        print("A cat has been born")
    def make_noise(self):
        print("Meow says " + self.name)

def main():
    NomNomNom = Mammal()
    NomNomNom.name = "NomNomNom"
    NomNomNom.make_noise()
    NomNomNom.eat()
    bark = Dog()
    yamacha = Dog()
    bark.name = "Bark"
    yamacha.name = "Yamacha"
    bark.make_noise()
    yamacha.make_noise()
    meow = Cat()
    meow.name = "Meow"
    meow.make_noise()

if __name__ == "__main__":
    main()