#%%
from autompg import *
import unittest

auto1 = AutoMPG("Subaru","Impreza",2001,23.0)
auto2 = AutoMPG("Toyota","Supra",1998,19.0)
auto3 = AutoMPG("Toyota","Tacoma",1998,19.0)

class TestAttributes(unittest.TestCase):
    
    #Test Constructor
    def test__init__(self):
        ret = AutoMPG("Subaru","Impreza",1998,17.0)
        self.assertEqual(ret,"The 1998 Subaru Impreza gets 17.0 mpg")

    #Test Equality
    def test__eq__(self):
        ret1 = auto2.make == auto3.make
        self.assertEqual(ret1,True)
        ret2 = auto1.make == auto2.make
        self.assertEqual(ret2,False)

    #Test Less Than
    def test__lt__(self):
        ret = auto2.year < auto1.year
        self.assertEqual(ret,True)

    #Test Load Data
    def test_load_data(self,other):
        pass

    #Test Load Data
    def test_clean_data(self,other):
        pass

if __name__ == '__main__':
    unittest.main()