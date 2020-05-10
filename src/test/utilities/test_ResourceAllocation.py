import unittest
import sys

sys.path.append('../../../')

from ResourceAllocation.src.utilities.ResourceAllocation import knapsack, _construct_solution

class TestKnapsackMethod(unittest.TestCase): 

    def test_weight_value(self):
        self.assertRaises(AssertionError, knapsack, 11, [], [], 0)
    def test_size_of_lists(self):
        self.assertRaises(AssertionError, knapsack, 11, [1], [1,2], 1)    
    def test_weight_negative_value(self):
        self.assertRaises(AssertionError, knapsack, -10, [1], [1], 1)  
    def test_n_value(self):
        self.assertRaises(AssertionError, knapsack, -10, [1], [1], 2)
          
  
if __name__ == '__main__': 
    unittest.main() 