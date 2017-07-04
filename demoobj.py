class MyClass():              #定义类
    def printMethod(self):       #定义方法(self类似于Java中的this，类方法和静态方法不需要)
        print("hello world")

mycls=MyClass()
mycls.printMethod()

#创建类
class AddrBookEntry(object):
    'address book entry class'

    def __init__(self,nm,ph):
        self.name=nm
        self.phone=ph
        print("create instance for",self.name)

    def updatePhone(self,newph):
        self.phone=newph
        print("updated phone# for",self.phone)

john=AddrBookEntry("john",13078587303)
jane=AddrBookEntry("jane",111)

#创建子类
class EmplAddrBookEntry(AddrBookEntry):

    'employee address book entry class'#员工地址簿

    def __init__(self,nm,ph,id,em):
        AddrBookEntry.__init__(self,nm,ph)
        self.emid=id
        self.email=em

    'employee address'

    def updateEmail(self,newem):
        self.email=newem
        print("updated e-mail address for:"+self.name)

john1=EmplAddrBookEntry("john doe","400-800-901",42,"jhon@john.com")
print(john1.__doc__)