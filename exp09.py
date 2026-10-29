class patient :
    def __init__(self,pid,name,age,disease):
        self.pid=pid
        self.name=name
        self.age=age
        self.disease=disease

    def show(self):
        print(F"pid: {self.pid},Name: {self.name},Age: {self.age} Disease :{self.disease}")

obj=patient(121,"Mahesh","55","Flue")
print(obj)
print(obj.disease)
obj.show()

obj1=patient(122,"sahil","45","feaver")

obj1.show()