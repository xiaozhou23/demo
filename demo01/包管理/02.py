import importlib

p = importlib.import_module("01")

stu = p.Student("Lee", 30)

stu.say()

p.sayHello()