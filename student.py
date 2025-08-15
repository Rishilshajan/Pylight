class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return print("HOnors")
        else:
            return False

    def __str__(self):               #The __str__() method controls what should be returned when the class object is represented as a string.
        return f"{self.name}"        