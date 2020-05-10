import json
import sys

sys.path.append('../')

import constants.ActivityConstants as activityConstants

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

def getMachineMap(subset):
    machineMap = dict()
    for machine in subset.keys():
        machineMap[activityConstants.MACHINES_DICT[machine]] = subset[machine]
    return machineMap        