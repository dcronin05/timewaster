print("Hello world")


class AClass(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getter(self):
        return self.a


newObj = AClass(3, "hello")
print(newObj.getter())
