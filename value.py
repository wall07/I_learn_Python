class Student(object):

    def get_score(self):
        return self.score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('ValueError:value must be an intger!')
        if value < 0 or value >100:
            raise ValueError('value must between 0~100')
        self.score = value


s = Student()
s.set_score(166)
print(s.get_score())


