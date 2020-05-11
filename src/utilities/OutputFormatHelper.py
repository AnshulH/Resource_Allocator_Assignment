import json
import pprint
from constants import activity_constants as ACTIVITY_CONSTANTS

output_writer = open("output.json", 'w')

# Method which generates the required format of json from the region map 
def output_json(regionMap):
    outputJsonDict = dict()
    outputMap = list()
    for region in regionMap.keys():
        regionValues = dict()
        regionValues[ACTIVITY_CONSTANTS.REGION] = region
        regionValues[ACTIVITY_CONSTANTS.TOTAL_COST] = regionMap[region]['cost']
        machineList = list()
        for capacity, units in regionMap[region]['subset'].items():
            machineList.append((ACTIVITY_CONSTANTS.CAPACITY_MACHINE_MAP[capacity], units))
        regionValues[ACTIVITY_CONSTANTS.MACHINES] = str(machineList)
        output_map.append(regionValues)
    outputJsonDict["Output"] = output_map

    # Print formatted output
    json.dump(outputJsonDict, output_writer, indent=4)
    pprint.pprint(outputJsonDict)
    return outputJsonDict
