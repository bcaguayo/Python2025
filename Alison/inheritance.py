class A:
    def method1(self):
        print("Method 1 from Class A")
    def method2(self):
        print("Method 2 from Class A")
class B(A):
    def method3(self):
        print("Method 3 from Class B")
    def method4(self):
        print("Method 4 from Class B")
class C(A, B):
    def __init__(self):
        super().__init__()
        print("c")

    def method5(self):
            print("5")
    
a = A()
b = B()
c = C()

a.method1()
a.method2()
# No
# a.method3()
# Yes
b.method1()
b.method2()