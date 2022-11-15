"""
class student:
    pass
    def check_pass_fail(self):
        if self.marks > 40:
            return True
        else:
            return False
student1 = student()
student1.name = "zaki"
student1.marks = 80

did_pass = student1.check_pass_fail()
print(did_pass)

student2 = student()
student2.name = "khan"
student2.marks = 30

did_pass= student2.check_pass_fail()
print(did_pass)
"""


"""

class student:
    

    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

student1 = student("zaki" , 80)
student2 = student("khan" , 30)

did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)

"""

"""
class animal:
    def eat(self):
        print("i can eat")
class dog(animal):
    def bark(self):
        print("i can bark")
class cat(animal):
    def get_grumpy(self):
        print("i am getting grumpy")

dog1 = dog()
dog1.eat()
dog1.bark()

cat1 = cat()
cat1.eat()
"""
"""
class polygon:
    def __init__(self , sides):
        self.sides = sides
    def display_info(self):
        print("a polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
class triangle(polygon):
    def display_info(self):
        print("a trinagle is a plygon with 3 edges")
        polygon.display_info(self)
class quadrilateral(polygon):
    def display_info(self):
        print("a quadrilateral is a ploygon with 4 edges")

t1= triangle([5 ,6 ,7])
perimeter = t1.get_perimeter()
print("the perimeter is" , perimeter)
"""