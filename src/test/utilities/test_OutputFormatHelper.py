import unittest
import sys
import json

sys.path.append('../../')

from utilities.OutputFormatHelper import OutputJson

expectedOutput = {
    "Output": [
        {
            "region": "NY",
            "total_cost": 8850,
            "machines": {
                "8XLarge": 6,
                "2XLarge": 1
            }
        },
        {
            "region": "IND",
            "total_cost": 8213,
            "machines": {
                "8XLarge": 6,
                "2XLarge": 1
            }
        },
        {
            "region": "CHN",
            "total_cost": 7480,
            "machines": {
                "8XLarge": 6,
                "XLarge": 2
            }
        }
    ]
}


class TestOutputFormatHelper(unittest.TestCase): 

    def test_output_json(self):
        regionMap = {'NY': {'cost': 8850, 'subset': {160: 6, 40: 1}}, 'IND': {'cost': 8213, 'subset': {160: 6, 40: 1}}, 'CHN': {'cost': 7480, 'subset': {160: 6, 20: 2}}}
        actualResponse = OutputJson(regionMap)
        self.assertEqual(json.loads(actualResponse),expectedOutput)
    
          
  
if __name__ == '__main__': 
    unittest.main() 