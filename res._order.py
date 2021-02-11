#res_ord. when we ask particular method and a father_class and son_class have the same method(same names), code will choose son's method
class Human: # name,age
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.salary = 0
    def description(self):#method
        print(f"{self.name} {self.age}")
    def __add__(self, other):
        return self.salary + other.salary
class Male(Human):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.very_strong = True
        self.salary = 50000
class Female(Human): #
    def __init__(self,name,age):
        super().__init__(name,age)
        self.very_beautiful = True
        self.salary = 60000
    def description(self):#method
        print(f"{self.name} {self.age} WOMAN")
male1 = Male(name='steve',age=29)
male1.description()
female1 = Female(name='mary',age=29)
female1.description()
print(male1 + female1)




