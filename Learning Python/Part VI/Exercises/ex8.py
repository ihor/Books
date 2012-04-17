from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    def reply(self):
        self.speak()

    @abstractmethod
    def speak(self):
        ...

class Mammal(Animal):
    ...

class Cat(Animal):
    def speak(self):
        print('Meow')

class Dog(Animal):
    def speak(self):
        print('Bark')

class Primate(Animal):
    ...

class Hacker(Primate):
    def speak(self):
        print('Hello world!')

if __name__ == '__main__':
    spot = Cat()
    spot.reply()
    
    sharik = Dog()
    sharik.reply()
    
    mark = Hacker()
    mark.reply()
    