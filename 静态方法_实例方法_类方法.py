class A:
    def __init__(self):
        self.a=0

    @staticmethod
    def out():
        print("This is a static method.")

    @classmethod
    def func(cls):
        print("%s This is a class method."%cls)

    def func2(self):
        print("%s This is a self method."%self)

    # out = staticmethod(out)        
    # func = classmethod(func)


if __name__ == "__main__":
    a = A()

    A.out()       #正确，通过类调用静态方法
    a.out()       #正确，通过实例调用静态方法

    # A.func2()   # 对于非类方法，不会自动传入类对象，因此参数个数不匹配，出错。
    a.func2()

    A.func()      #正确，通过类调用类方法
    a.func()      #正确，通过实例调用静态方法（仍然自动传入类对象不是实例对象）


