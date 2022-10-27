import os
import re
from collections import namedtuple

class AutoMPG:
    """Creates an AutoMPG object"""
    #Constructor
    def __init__(self,make:str,model:str,year:int,mpg:float):
        self.make = str(make)
        self.model = str(model)
        self.year = int(year)
        self.mpg = float(mpg)
    
    #String
    def __str__(self):
        return f'The {self.year} {self.make} {self.model} gets {self.mpg} mpg'
    def __repr__(self):
        return f'AutoMPG:{self.make},{self.model},{self.year},{self.mpg}'
    
    #Equality
    def __eq__(self, other):
        if not isinstance(other,AutoMPG):
            return False
        else:
            return hash(self) == hash(other)
            
    #Hash
    def __hash__(self):
        return hash((self.make,self.model,self.year,self.mpg))
    
    #Less Than
    def __lt__(self, other):
        if isinstance(self,other.__class__):
            return self < other
        else:
            return NotImplemented
    

class AutoMPGData:
    """Loads and cleans auto mpg data"""
    #Constructor
    def __init__(self):
        self.data = []
        self._load_data()

    #Data Loader
    def _load_data(self,data):
        self.data = data
        Record = namedtuple('Record',['mpg','cylinders','displacement','horsepower','weight','acceleration','year','origin','name'])
        clean_data = 'auto-mpg.clean.txt'

        if not os.path.exists(clean_data):
            self._clean_data()
        
        with open(clean_data, 'r') as f:
            self.data = f.readlines()
            return self.data
        
        #iterate through txt file and apply 

    #Data Cleaner
    def _clean_data(self):
        with open('auto-mpg.data.txt', 'r') as f:
            lines = f.readlines()

        df = [line.expandtabs() for line in lines]
        df = [re.sub('  +',',',line) for line in df]
        df = [re.sub('\n','',line) for line in df]
        df = [re.sub('"','',line) for line in df]
        df = [line.split(",") for line in df]

        with open('auto-mpg.clean.txt', 'w') as f:
            f.writelines(str(df))
    
    #Iterator & Next
    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self): #needed to use iter?
        pass

#%%
def main():

    for vehicle in AutoMPGData():
        print(vehicle) 

if __name__ == '__main__':
    main()