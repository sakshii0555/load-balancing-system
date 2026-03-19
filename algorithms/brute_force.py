def brute_force_partition(loads):
    
    n = len(loads)
    total = sum(loads)

    best_subset = []
    best_diff = float("inf")

    for i in range(1 << n):

        subset = []
        subset_sum = 0

        for j in range(n):

            if i & (1 << j):
                subset.append(loads[j])
                subset_sum += loads[j]

        diff = abs(total - 2 * subset_sum)

        if diff < best_diff:
            best_diff = diff
            best_subset = subset

    return best_subset
