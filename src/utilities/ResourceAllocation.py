# This method uses bottom up dp to find the optimal subset of machines and the minimum cost 
def knapsack(W, wt, val):

    assert (W > 0), "Value of W is less than 0"

    assert (W % 10 == 0), "Value of W is not a multiple of 10"

    assert (len(wt) == len(val)), "Length of Units and Costs Lists not equal"

    n = len(wt)

    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(1 , W+1):
        dp[0][i] = 1000000000
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = min(val[i - 1] + dp[i][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]       

    return dp[n][W], dp


def construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: dict):
    """
    Recursively reconstructs one of the optimal subsets given
    a filled DP table and the vector of weights
    Parameters
    ---------
    dp: list of list, the table of a solved integer weight dynamic programming problem
    wt: list or tuple, the vector of weights of the items
    i: int, the index of the  item under consideration
    j: int, the current possible maximum weight
    optimal_set: set, the optimal subset so far. This gets modified by the function.
    Returns
    -------
    None
    """
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            if wt[i - 1] in optimal_set:
                optimal_set[wt[i-1]] += 1
            else:
                optimal_set[wt[i-1]] = 1
            construct_solution(dp, wt, i, j - wt[i - 1], optimal_set)


