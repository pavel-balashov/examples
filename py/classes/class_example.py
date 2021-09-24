class myclass:

    def __init__(self, msg = ''):
        self.msg = (lambda msg: msg if msg != '' else 'Hello World!')(msg)
    
    def myprint(self):
        print(self.msg)


m1 = myclass()
m1.myprint()
del m1

m1 = myclass('my message')
m1.myprint()
