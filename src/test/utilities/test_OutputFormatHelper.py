import unittest
import sys
import json

sys.path.append('../../')

from utilities.OutputFormatHelper import OutputJson

expectedOutput = {'Output': [{'machines': "[('8XLarge', 7), ('XLarge', 1), ('Large', 1)]",
             'region': 'New York',
             'total_cost': 10150},
            {'machines': "[('8XLarge', 7), ('Large', 3)]",
             'region': 'India',
             'total_cost': 9520},
            {'machines': "[('8XLarge', 7), ('XLarge', 1), ('Large', 1)]",
             'region': 'China',
             'total_cost': 8570}]}


class TestOutputFormatHelper(unittest.TestCase): 

    def test_output_json(self):
        regionMap = {'New York': {'cost': 10150, 'subset': {160: 7, 20: 1, 10: 1}}, 'India': {'cost': 9520, 'subset': {160: 7, 10: 3}}, 'China': {'cost': 8570, 'subset': {160: 7, 20: 1, 10: 1}}}
        actualResponse = OutputJson(regionMap)
        self.assertEqual(json.loads(actualResponse),expectedOutput)
    
          
  
if __name__ == '__main__': 
    unittest.main() 
