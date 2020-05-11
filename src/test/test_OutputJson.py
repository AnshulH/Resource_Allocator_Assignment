import unittest
import sys
sys.path.append('../')

from main import mainFunc
# TODO: Fix issue with args to run complete test
# class TestKnapsackMethod(unittest.TestCase): 
#     def test_weight_value(self):
#         self.assertEquals(mainFunc(['main.py', '--units', '1000', '--hours', '1']),1)
          
if __name__ == '__main__': 
    unittest.main() 

