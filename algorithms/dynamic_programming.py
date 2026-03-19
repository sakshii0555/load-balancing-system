def dp_partition(loads):
    
    total = sum(loads)
    target = total // 2
    n = len(loads)

    steps = 0

    dp = [[False]*(target+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True
        steps += 1

    for i in range(1, n+1):

        for j in range(1, target+1):

            steps += 1

            if loads[i-1] <= j:

                dp[i][j] = dp[i-1][j] or dp[i-1][j-loads[i-1]]

            else:

                dp[i][j] = dp[i-1][j]

    for j in range(target, -1, -1):

        steps += 1

        if dp[n][j]:

            subset_sum = j
            break

    subset = []
    i = n
    j = subset_sum

    while i > 0 and j >= 0:

        steps += 1

        if dp[i][j] and not dp[i-1][j]:

            subset.append(loads[i-1])
            j -= loads[i-1]

        i -= 1

    return subset, steps