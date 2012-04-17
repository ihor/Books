class Lunch:
    def have(self):
        julio = Employee('Julio')
        customer = julio.meetCustomer()
        customer.placeOrder(Employee('Maria'))
        customer.sayThankYou()

class Customer:
    def __init__(self, name):
        self.name = name
        self.food = None

    def placeOrder(self, employee):
        self.food = employee.takeOrder(self)

    def sayThankYou(self):
        print('You: Thank you! The {0} {1} delicious.'.format(
            self.food.name,
            'were' if self.food.name[-1] == 's' else 'was'
        ))

class Employee:
    def __init__(self, name):
        self.name = name

    def meetCustomer(self):
        print("{0}: Hello, I'm {0}. What is your name?\nYou: ".format(self.name), end="")
        customerName = input()
        print("Ok. Here is your table. Please wait. We will bring you a menu.")
        return Customer(customerName)

    def takeOrder(self, customer):
        print("""{1}: Hello, {0}!
I'm {1}. What would you like? 
I recommend tacos, they are very tasty today.
You: """.format(customer.name, self.name), end="")

        foodName = input()
        print('{0}: Your {1}'.format(self.name, foodName))
        return Food(foodName)

class Food:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    Lunch().have()
