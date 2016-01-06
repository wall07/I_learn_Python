#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name','age')

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'JiangL'
s.age = 22

try:
    s.score = 100
except AttributeError as e:
    print('AttributeError:',e)

g = GraduateStudent()
g.score = 101
print('g.score = ',g.score)

