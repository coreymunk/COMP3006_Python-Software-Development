import os
import re
from collections import namedtuple

class AutoMPG:
    
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
        if isinstance(self,other.__class__):
            return self == other
        else:
            return NotImplemented

    #Hash
    def __hash__(self):
        return hash(self.make,self.model,self.year,self.mpg)
    
    #Less Than
    def __lt__(self, other):
        if isinstance(self,other.__class__):
            return self < other
        else:
            return NotImplemented
    


class AutoMPGData:
    
    #Constructor
    def __init__(self, data):
        self.data = data 

        self.data = AutoMPGData._load_data()

    #Data Loader
    def _load_data(self,data):
        self.data = data
        Record = namedtuple('Record',['mpg','cylinders','displacement','horsepower','weight','acceleration','year','origin','name'])
        clean_data = 'auto-mpg.clean.txt'

        if os.path.exists(clean_data):
            with open(clean_data, 'r') as f:
                self.data = f.readlines()
            return self.data
        else:
            AutoMPGData._clean_data()

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
    pass
    
    ## Data Columns & Types
    # 1. mpg:           continuous
    # 2. cylinders:     multi-valued discrete
    # 3. displacement:  continuous
    # 4. horsepower:    continuous
    # 5. weight:        continuous
    # 6. acceleration:  continuous
    # 7. model year:    multi-valued discrete
    # 8. origin:        multi-valued discrete
    # 9. car name:      string (unique for each instance)

if __name__ == '__main__':
    main()