#1
'''
try:
    print('try......')
    t = 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally......')
print('END')
'''

class Student(object):
    __slots__ = ('name','age')

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'JiangLiu'
s.age = 20

try:
    s.score = 100
except AttributeError as e:
    print('AttributeError:',e)

s1 = GraduateStudent()
s1.score = 150
print(s1.score)
