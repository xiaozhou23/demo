# 定义一个空类
class Student():
    pass


# 定义一个对象
Lily = Student()


# 定义一个类，学习Python的学生
class StudentPython():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("I am doing homework")
        # 末尾加return
        return None


# 实例化对象
sam = StudentPython()
print(sam.name)
print(sam.age)

# 调用类函数，没有参数传入
sam.doHomework()

print("test")
print(StudentPython.__dict__)

print(sam.__dict__)
