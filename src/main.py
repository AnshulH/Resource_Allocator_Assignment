import json
import constants.ActivityConstants
import constants.regionConstants.India as IND
import constants.regionConstants.NewYork as NY
import constants.regionConstants.China as CHN

from utilities.ResourceAllocation import knapsack, _construct_solution 

if __name__ == "__main__":
    """
    Adding test case for knapsack
    """
    val = [140, 413, 890, 1300, 2970]
    wt = [10, 40, 80, 160, 320]
    n = 5
    w = 1150
    optimal_solution, dp = knapsack(w, wt, val, n)
    optimal_val = dict()
    _construct_solution(dp,wt,n,w,optimal_val)
    print(optimal_val)
    print(optimal_solution)