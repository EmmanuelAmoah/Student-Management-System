class Student:

    def __init__(self, id, first_name, middle_name, last_name, dob, course, duration):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dob = dob
        self.course = course
        self.duration = duration

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def Set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def get_middle_name(self):
        return self.middle_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_dob(self, dob):
        self.dob = dob

    def get_dob(self):
        return self.dob

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_course(self, course):
        self.course = course

    def get_course(self):
        return self.course

    def set_period(self, duration):
        self.duration = duration

    def get_period(self):
        return self.duration
