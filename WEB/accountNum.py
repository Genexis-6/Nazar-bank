from random import choice

class AccNum:
    def __init__(self):
        self.numlist = [str(x) for x in range(0,10)]
        self.accnum = '664'
        self.create()
        
    def create(self):
        num = ''
        for x in range(7):
            self.accnum += choice(self.numlist)
            
