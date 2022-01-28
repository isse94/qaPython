
# import pdb
# pdb.set_trace()

# class Dog:
#     energy = "high"

#     def speak(self):
#         print("woof")

# bilbo_waggins = Dog()

# print(bilbo_waggins.energy)
# bilbo_waggins.speak()

#tutorial
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# John = Student("John", "21")
# Jane = Student("Jane", "22")       

# print(getattr(John, "age")) 

#excercise 
# create a class of students.
# It should contain the following attributes: name, age, and class with default value "student".
# It should also contain a method which takes in 3 test scores and prints the students average test score.



class students:
    def __init__(self, age, testScore, className, name = "student"):
            self.name = name
            self.age = age
            self.className = className
            # self.testScore = testScore
            # print(testScore)
    def scoreAV(self,score1:int ,score2:int ,score3:int) :
                avgScore = (score1 + score2 + score3) / 3
                
                return avgScore                
    
cr7 = students("37",int(20),"Art",)
Messi = students("33",int(10),"Maths","Messi")    
Neymar = students("30",int(30),"Drama","Neymar") 
# totalScore = 0
# print(getattr(cr7, "name")) 
# print(cr7.testScore) 

# avgTestScore(cr7, Messi, Neymar) 
print(cr7.scoreAV(1,2,3))      
print(Messi.scoreAV(6,6,6))      
print(Neymar.scoreAV(7,7,7))      

