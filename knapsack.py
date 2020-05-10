
def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(1 , W+1):
        dp[0][i] = 100000000
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = min(val[i - 1] + dp[i][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]       

    return dp[n][W], dp


if __name__ == "__main__":
    """
    Adding test case for knapsack
    """
    val = [140, 413, 890, 1300, 2970]
    wt = [10, 40, 80, 160, 320]
    n = 5
    w = 1150
    F = [[0] * (w + 1)] + [[0] + [-1 for i in range(w + 1)] for j in range(n + 1)]
    optimal_solution, dp = knapsack(w, wt, val, n)
    Set = dict()
    # _construct_solution(dp,wt,n,w,Set)
    print(Set)
    print(optimal_solution)