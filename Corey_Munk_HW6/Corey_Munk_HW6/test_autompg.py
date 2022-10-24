#%%
from autompg import *
import unittest

class TestAttributes(unittest.TestCase):
    
    def test__init__(self):
        ret = 123
        self.assertEqual(ret,123)

    def test__eq__(self,other):
        pass

    def test__lt__(self,other):
        pass

    def test_load_data(self,other):
        pass

    def test_clean_data(self,other):
        pass

if __name__ == '__main__':
    unittest.main()