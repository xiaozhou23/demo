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

print("This is p01.")