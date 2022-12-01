class Students:
    val=0
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
        Students.val=max(Students.val,(marks1+marks2+marks3)/3)
    def __del__(self):
        print("destructor called")    
b=Students("Varun",87,97,100)
c=Students("Varun",97,97,99)
d=Students("Varun",100,100,100)
print(Students.val)        