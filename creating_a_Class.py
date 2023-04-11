class Mobile:
    def __init__(self, model,camera):
        self.model = model
        self.camera = camera
    def make_call(self,number):
        print("calling...{}".format(number))
object_1 = Mobile("Galaxy M53","108MP")
print(object_1)
print(type(object_1))
print(id(object_1))
object_2 = Mobile("Note 12", "48MP")
print(object_2)
print(type(object_2))
print(id(object_2))