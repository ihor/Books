class Actor:
    name = 'actor'
    def line(self, text):
        print(self.__class__.name + ':', text)

class Customer(Actor):
    name = 'customer'

class Clerk(Actor):
    name = 'clerk'

class Parrot(Actor):
    name = 'parrot'

class Scene:
    def action(self):
        Customer().line("that's one ex-bird!")
        Clerk().line("no it isn't...")
        Parrot().line('None')

if __name__ == '__main__':
    Scene().action()