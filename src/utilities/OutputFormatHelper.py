import json
import sys

sys.path.append('../')

import constants.ActivityConstants as activityConstants

# Method which generates the required format of json from the region map 
# region map -> {'NY': {'cost': 8850, 'subset': {160: 6, 40: 1}}, 'IND': {'cost': 8213, 'subset': {160: 6, 40: 1}}, 'CHN': {'cost': 7480, 'subset': {160: 6, 20: 2}}}
def OutputJson(regionMap):
    outputJson = dict()
    outputMap = list()
    for region in regionMap.keys():
        regionValues = dict()
        regionValues[activityConstants.REGION] = region
        regionValues[activityConstants.TOTAL_COST] = regionMap[region]['cost']
        regionValues["machines"] = getMachineMap(regionMap[region]['subset'])
        outputMap.append(regionValues)
    outputJson["Output"] = outputMap
    jsonString = json.dumps(outputJson, indent=4)
    return jsonString
# Maps coresponding subset map to machine based on units 
# ex. LARGE -> 10 units
def getMachineMap(subset):
    machineMap = dict()
    for machine in subset.keys():
        machineMap[activityConstants.MACHINES_DICT[machine]] = subset[machine]
    return machineMap        
