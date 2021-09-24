class myclass:

    def __init__(self, msg = ''):
        self.msg = (lambda msg: msg if msg != '' else 'Hello World!')(msg)

    def myprint(self):
        print(self.msg)
    
    @classmethod
    def cm_print(cls): # I know the class, but I don't know the object (instance of the class)
        pass

    @staticmethod
    def sm_print(arg1, arg2, any_arg):  # I don't know the class and the object (instance of the class), I know arguments only
        pass

m1 = myclass()
m1.myprint()
del m1

m1 = myclass('my message')
m1.myprint()
