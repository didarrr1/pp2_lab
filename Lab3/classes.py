#task1
class String:
    def getString(self):
        self.userInput = input()
    def printString(self):   
        print(self.userInput.upper())
string = String()
string.getString()
string.printString()

#square
class Shape():
    def __init__(self) -> None:
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return self.length * self.length
x = int(input())
s = Square(x)
print(s.area())
print(Square().area())

#rectangle
class Shape():
    def __init__(self):
        pass
    def area(self, length, width):
        return 0
class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        Shape.__init__(self)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
l = int(input())
w = int(input())
r = Rectangle(l, w)
print(r.area())
print(Rectangle().area())

#point
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    def dist(self, p2):
        newx = math.sqrt((p2.x - self.x) * (p2.x - self.x))
        newy = math.sqrt((p2.y - self.y) * (p2.y - self.y))
        return newx, newy
    
p1 = Point(5, 4)
p2 = Point(3, 4)
print(p1.show())
p1.move(1, 1)
print(p1.show())
print(p1.dist(p2))

#bank
class Account():
    owner = ""
    balance = 0
    def __init__(self, owner, balance):
        self.owner = owner 
        self.balance = balance
    def __str__(self):
        return f"Owner of an account is: {self.owner}\nAccount balance is: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return "Deposit!!"
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            return "Withdraw accepted"
        else:
            return "Withdraw can not be accepted"
acc1 = Account("Askar", 10000)
print(acc1)
print(acc1.deposit(50))
print(acc1.withdraw(20))
print(acc1.balance)

#prime number
class Filter_prime():
    def isPrime(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, num):
                if(num % i == 0):
                    return False
        return True   
    def filter_primes(self, listofnums):
        return filter(lambda x : self.isPrime(x), listofnums)
prime_filter = Filter_prime()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(prime_filter.filter_primes(nums))
print(prime_numbers)
#result: [2, 3, 5, 7]