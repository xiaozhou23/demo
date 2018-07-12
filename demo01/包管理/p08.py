import pkg01.p01

stu = pkg01.p01.Student("Lily")

stu.say()

pkg01.p01.sayHello()

print(type(pkg01))
print(type(pkg01.p01))
print(type(pkg01.p01.sayHello))
print(type(pkg01.p01.Student))
print(type(pkg01.p01.Student.say))