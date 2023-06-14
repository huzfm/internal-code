# class father():
#     def cash(self):
#         print('10lac')
# class son(father):
#     def money(self):
#         print("10k")
# obj=son()
# obj.cash()
# obj.money()
    
# class Transport():
#     def fun1(self):
#         print("commute")
# class Car(Transport):
#     def fun2(self):
#         print("comfortable")
# class Bike(Car):
#     def fun3(self):
#         print("fast")
# obj=Bike()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# class Vehicle():
#     def fun1(self):
#         print("The Vehicle")
# class Car(Vehicle):
#     def fun2(self):
#         print("that is comf")
# class Bike(Vehicle):
#     def fun3(self):
#         print("that is fast")
        
# obj=Car()
# obj.fun1()
# obj.fun2()
# obj1=Bike()
# obj.fun1()
# obj1.fun3()
class stu():
    def __init__(self,name,course):
        self.name=name
        self.course=course
        
    def show(self):
        print(self.name)
        print(self.course)
o1=stu("Huzaif","BCA")
o2=stu("Sadiya","IMCA")
o3=stu("Noorain","B.A")


o1.show()
o2.show()
o3.show()
        