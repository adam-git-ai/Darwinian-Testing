# A script which logs failed TC's parameter sets in database

def storeFails(self):

    def findFails(self):
        for i in range(0,len(self.popVerdict)):        # Sums up the fails for each population, the higher the sum the higher the fitness of that population.    
            index = 0
            for verd in self.popVerdict[i]:
                if verd == 'fail':
                    save(self, i, index)
                index += 1

    def save(self, i, index):
        f = open("failedATCs.txt", "a+")
        for each in self.parametersets[self.population[i][index]]:
            f.write(str(each).strip('[').strip(']'))
        f.write("\n")

    findFails(self)