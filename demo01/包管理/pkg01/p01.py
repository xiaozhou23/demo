class Student():
    def __init__(self, name="Sam", age = 18):
        self.name = name
        self.age = age
        return

    def say(self):
        print("My name is {0}".format(self.name))
        return


def sayHello():
    print("Wellcome to ZhangZhou !")
    return

if __name__ == '__main__':
    print("This is p01.")

print(type(Student.say))