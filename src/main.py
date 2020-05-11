import json
import sys

import constants.ActivityConstants as ACTIVITY_CONSTANTS
import constants.regionConstants.India as IND
import constants.regionConstants.NewYork as NY
import constants.regionConstants.China as CHN

from utilities.ArgParser import parse_args
from utilities.ResourceAllocation import knapsack, _construct_solution 
from utilities.OutputFormatHelper import OutputJson

def mainFunc(args):
    parser = parse_args(args[1:])

    assert parser.units != None, "Please specify units required"
    assert parser.hours != None, "Please specify total hours required"

    units = parser.units
    hours = parser.hours

    regionMap = dict()

    for region in ACTIVITY_CONSTANTS.REGION_LIST:
        optimalVal = dict()
        regionalOptimalValue = dict()

        if region == "NY":
            optimalSolution, dp = knapsack(units, NY.REGION_MACHINE_UNIT_LIST, NY.REGION_MACHINE_COST_LIST, NY.REGION_MACHINE_COUNT)
            _construct_solution(dp ,NY.REGION_MACHINE_UNIT_LIST ,NY.REGION_MACHINE_COUNT ,units ,optimalVal)
        elif region == "IND":
            optimalSolution, dp = knapsack(units ,IND.REGION_MACHINE_UNIT_LIST ,IND.REGION_MACHINE_COST_LIST ,IND.REGION_MACHINE_COUNT)
            _construct_solution(dp ,IND.REGION_MACHINE_UNIT_LIST ,IND.REGION_MACHINE_COUNT ,units ,optimalVal)
        elif region == "CHN":
            optimalSolution, dp = knapsack(units ,CHN.REGION_MACHINE_UNIT_LIST ,CHN.REGION_MACHINE_COST_LIST ,CHN.REGION_MACHINE_COUNT)
            _construct_solution(dp, CHN.REGION_MACHINE_UNIT_LIST ,CHN.REGION_MACHINE_COUNT ,units ,optimalVal)

        regionalOptimalValue["cost"] = optimalSolution * hours
        regionalOptimalValue["subset"] = optimalVal
        regionMap[region] = regionalOptimalValue

    print(OutputJson(regionMap))

if __name__ == "__main__":
    mainFunc(sys.argv)
