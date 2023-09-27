class Parent:

    def __init__(self,fage):
        self.f_age=fage

    def father_style(self):
        print('father style')


class Son(Parent):
    def __init__(self,fage,sage):
        super().__init__(fage)
        self.s_age=sage
    def son_style(self):
        print('son style')