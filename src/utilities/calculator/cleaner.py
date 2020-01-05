'''
this module returns statment after applying all 
effect on after and effect on before modefyers 
'''
class cleaner:
    def __init__(self, statement):
        self.statement = statement
        self.listOfFeallings= statement[0]["fealling"].keys()
        self.listOfTags= statement[0]["fealling"].keys()
    
    def calcAfter(self, index):
        if index >= len(self.statement)-1:
            pass
        else:
            for i in self.listOfFeallings:self.statement[index+1]["feallings"][i]=self.statement[index+1]["feallings"][i]*self.statement[index]["effectOnAfter"][i]
            for i in self.listOfTags:self.statement[index+1]["tags"][i]=self.statement[index+1]["tags"][i]*self.statement[index]["effectOnAfter"][i]

    def calcBefore(self, index):
        if index == 0:
            pass
        else:
            for i in self.listOfFeallings:self.statement[index-1]["feallings"][i]=self.statement[index-1]["feallings"][i]*self.statement[index]["effectOnBefore"][i]
            for i in self.listOfTags:self.statement[index-1]["tags"][i]=self.statement[index-1]["tags"][i]*self.statement[index]["effectOnBefore"][i]


    def excute(self):
        for i in range(len(self.statement)):
            self.calcAfter(i)
            self.calcBefore(i)
         
def cleanAll(statement):
    x = cleaner(statement)
    x.excute()
    return x.statement