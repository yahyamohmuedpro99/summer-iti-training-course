
"""
- this sys is responsible for managing cars and motorcycle data
- sell for new and used cars and show 
- calculate the sales for the agancy , comparing cars [power] and for used cars i can show how much km is move 

- renting cars for customers 

- buying options 
"""


class Car:
    def __init__(self,name,color,model,staus,power,price):
        self.name = name
        self.color = color
        self.model = model
        self.staus = staus
        self.power = power
        self.price = price
    def __str__(self):
        return self.name
    
class Motorcycle:
    def __init__(self,name,color,model,staus,power):
        self.name = name
        self.color = color
        self.model = model
        self.staus = staus
        self.power = power
        
    def __str__(self):
        return self.name

class Employee:
    def __init__(self, name, salary ,commision,role):
        self.name = name
        self.salary = salary
        self.commisison = commision
        self.role = role
    def check(self):
        return self.salary + self.commisison 
    def __str__(self):
        return self.name
        
class Customer:
    def __init__(self, name,deposit,status):
        self.name = name
        self.deposit = deposit
        self.status = status

    def __str__(self):
        return self.name

class Agancy:
    sales = 0
    def __init__(self):
        self.cars = []
        self.motorcycles=[]
        self.selled_cars = []
        self.employees = []
        
    def insert(self, item):
        if isinstance(item,Car):
            self.cars.append(item)
            print(f"you add this car to your agancy {item}")
        else:
            self.motorcycles.append(item)
            print(f"you add this motorcycle to your agancy {item}")
    
    def get_all(self,item):
        if item == 'cars':
            for car in self.cars:
                print(str(car))
        else:
            for mororcycle in self.motorcycles:
                print(str(mororcycle))
    
    def sell_this(self,item,customer,employee):
        # add the price for the sales 
        self.selled_cars.append(item)
        self.sales += item.price
        self.cars.remove(item)
        # sale=Sell(item,customer)
        commisison = item.price*0.025
        employee.commisison += commisison
        self.sales -= commisison
        self.employees.append(employee)
        print(f"this sell done by {employee.name} for {item} selled to {customer.name} ")
    
    def __str__(self):
        return "i'm agancy for cars and motor cycles"


car1= Car('toyota','red','crola','new',2000,5000)
car2= Car('toyota','red','crola 2','new',3000,6500)

agancy=Agancy()
agancy.insert(car1)
agancy.insert(car2)

customer1=Customer('hamada1',2000,'cash')
empoloyee = Employee('hamada_seller',500,0,'seller')

agancy.sell_this(car1,customer1,empoloyee)

print('--------------sales--------------')
print(agancy.sales)
print(empoloyee.check())
print('----------------------------')
print(agancy.get_all('cars'))
