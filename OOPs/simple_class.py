class Chai:
    pass
class ChaiTime:
    pass
obj=Chai()
print(type(obj))
print(type(Chai))
print(type(obj) is Chai)
print(type(obj) is ChaiTime)
print(dir(obj))


list_values=[1,2,3,6,4,5,7]
print(sorted(list_values))

name="sachin"
res=''.join(reversed(name))
print(res)

print(name[::-1])
print(list(reversed(name)))

s=lambda x,y: x*y
print(s(10,20))

import random
print(random.randint(1,100))

class Chai:
    origin="India"
Chai.is_hot=True
print(Chai.origin)
print(Chai.is_hot)
#crate an obj
chai_obj=Chai()
print(chai_obj.origin)
print(chai_obj.is_hot)

Chai.is_hot=False
print(Chai.is_hot)
#attribute shadowing
class Chai:
    temperature="hot"
    strength="strong"
cutting=Chai()
cutting.temperature="mild"
# print(cutting.temperature)
# print(cutting.strength)
# print(Chai.temperature)

del cutting.temperature
print(cutting.temperature)

# del Chai.temperature
print(Chai.temperature)
# print(temperature)
# print(Chai.temperature)
# print(Chai.strength)
# print(Chai.temperature)
# print(temperature)

class Chai:
    size = 100
    def describe(self):
        print(f"size of the chai is {self.size}ml")
chai_obj=Chai()
chai_obj.describe()
Chai.describe(chai_obj)
chai_obj_2=Chai()
chai_obj_2.size=200
Chai.describe(chai_obj_2)

# class Chai:
#     def __init__(self,type_,size):
#         self.type=type_
#         self.size=size
#     def summary(self):
#         return f"{self.size} of ml of {self.type}"
# chai_order=Chai("Masala chai",220)
# print(chai_order.summary())

class Employee:
    def __init__(self,type_,size):
        self.type=type_
        self.size=size
    def emp_history(self):
        return f"{self.type} of the employee and size is to be{self.size}"
emp=Employee("IT",200)
print(emp.emp_history())

# class BaseChai:
#     def __init__(self,type_):
#         self.type=type_
#     def prepare(self):
#         print(f"{self.type} chai")
# class MasalaChai(BaseChai):
#     def add_spices(self):
#         print("adding cardamom, ginger")
# chai_type=MasalaChai("ginger")        
# chai_type.prepare()
# chai_type.add_spices()

#inheritance and composition
class BaseChai:
    def __init__(self,type_):
        self.type=type_
    def prepare(self):
        print(f"{self.type} chai")
        
class MasalaChai(BaseChai):
    def prepare_chai(self):
        print(f"{self.type} adding cardamom, ginger")
obj_masala_chai=MasalaChai("ginger")
print(obj_masala_chai.prepare())
obj_masala_chai.prepare_chai()

#composition
class chai_shop:
    chai_cls=BaseChai
    def __init__(self):
        self.chai=self.chai_cls("Regular")
    def serve(self):
        # print(self.chai.prepare())
        self.chai.prepare()
        print(f"{self.chai.type} chai in the shop")
        
class FancyChai(chai_shop):
    chai_cls=MasalaChai
shop=chai_shop()
masala_chai=MasalaChai("milk")
shop.serve()
masala_chai.prepare_chai()


#way to access baseclass
# class BaseChai:
#     def __init__(self,type_,strength):
#         self.type=type_
#         self.strength=strength
# class gingerChai(BaseChai):
#     def __init__(self, type_, strength,spicy_level):
#         self.type=type_
#         self.strength=strength
#         self.spicy_level=spicy_level
        
# class GingerChai(BaseChai):
#         def __init__(self, type_, strength,spice_level):
#             BaseChai.__init__(self,type_,strength)
#             self.spice_level=spice_level

# class GingerChai(BaseChai):
#     def __init__(self, type_, strength,spicy_chai):
#         super().__init__(type_,strength)
#         self.spicy_chai=spicy_chai

#way to access a baseclass
class Employee:
    def __init__(self,type_,name,city):
        self.type=type_
        self.name=name
        self.city=city
class Company(Employee):
    def __init__(self, type_, name, city):
        super().__init__(type_, name, city)

class Company(Employee):
    def __init__(self,type_,name,city,code):
        Employee.__init__(type_,name,city)
        self.code=code
        
#multiple resolution Order MRO

class A:
    label="A: BaseClass"
class B:
    label="B: child1 class"
class C:
    label="C: child2 class"

class D(C,B):
    pass
obj=D()
# print(obj.label)
print(obj.label)
print(D.__mro__)

class Chai_utils:
    @staticmethod
    def chai_ingredients(text):
        return [item.strip() for item in text.split(",")]
raw=" water , milk, coffee, ginger, milk_powder "
# obj=Chai_utils()
# print(obj.chai_ingredients(raw))
print(Chai_utils.chai_ingredients(raw))





    
    
    


        
    
        
    












