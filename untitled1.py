class sama:
    """designing instance variable and method"""
    girl="mouni"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def insta(self,marriage):
        self.marriage=marriage
        print("hii {} pilla ".format(sama.girl),"i know your age is:",self.age,"marriage",self.marriage)
        print("i know your age:",self.age)
s=sama('mounika',23)
s.insta("inka kaledu")
s.ready="yes iam ready for marriage"
print(sama.girl)
print(s.ready)
print(s.name,s.age)
print(s.__dict__)
