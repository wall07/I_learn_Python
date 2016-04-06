#1
'''
class Student(object):
    def __init__(self,name):
        self.name = name

print(Student('Michael'))
'''

#2
'''
class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student name is: %s'%self.name

#s = Student('Jiangliu')

print(Student('Bob'))
'''

#3
'''
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student names is %s'%self.name
    __repr__ = __str__

s = Student('Michael')
print(s)
'''

#4
'''
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 10000000:
            raise StopIteration();
        return self.a

for n in Fib():
    print(n)
'''
#5

class Fib(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a

f = Fib()
print(f[0])
print(f[199])
































