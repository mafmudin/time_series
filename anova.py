import scipy.stats as stats

if __name__ == '__main__':

    # Scores for each group
    group_A = [85, 90, 88, 87, 95, 92]
    group_B = [78, 82, 79, 80, 87, 90]
    group_C = [92, 88, 85, 91, 90, 82]

    # Perform one-way ANOVA
    f_stat, p_value = stats.f_oneway(group_A, group_B, group_C)

    # Output the results
    print("F-Statistic:", f_stat)
    print("P-Value:", p_value)