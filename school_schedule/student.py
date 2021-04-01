class Student:
    def __init__(self, name, grade, classlist):
        self.name = name
        self.grade = grade
        self.classlist = classlist
    
    def add_class(self, new_class):
        self.classlist.append(new_class)
        return self.classlist

    def get_num_classes(self):
        return len(self.classlist)