import json
from utilities.ArgParser import cli_input
from utilities.ResourceAllocation import knapsack, construct_solution
from utilities.OutputFormatHelper import output_json
from constants import activity_constants as ACTIVITY_CONSTANTS

inventory_file = open('constants/regionwise_inventory.json', )
REGION_WISE_INVENTORY = json.load(inventory_file)


def resource_allocation_engine():
    # Obtain inputs from commandline
    args = cli_input()
    units = args["units"]
    hours = args["hours"]

    assert units != None, "Please specify units required"
    assert hours != None, "Please specify total hours required"
    
    # Map to save region wise cost and resource allocation information
    regionMap = dict()

    # Allocate resources region wise
    for region in ACTIVITY_CONSTANTS.REGION_LIST:
        optimalVal = dict()
        regionUnitList = list()
        regionCostList = list()
        regionInventory = REGION_WISE_INVENTORY[region]["machines_dict"]
        for machine in regionInventory.keys():
            regionUnitList.append(regionInventory[machine].get("unit", 0))
            regionCostList.append(regionInventory[machine].get("cost", 0))

        optimalSolution, dp = knapsack(units,  regionUnitList, regionCostList)
        construct_solution(dp, regionUnitList, len(regionUnitList), units, optimalVal)

        regionMap[region] = {
            "cost": optimalSolution * hours,
            "subset": optimalVal
        }

    # Generate output
    output_json(regionMap)


if __name__ == "__main__":
    resource_allocation_engine()
