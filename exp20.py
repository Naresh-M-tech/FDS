import numpy as np
from scipy.stats import ttest_ind

design_A = np.array([0.12,0.15,0.14,0.10,0.13])
design_B = np.array([0.18,0.20,0.17,0.19,0.21])

t_stat, p_value = ttest_ind(design_A, design_B)

print("T Statistic:", t_stat)
print("P Value:", p_value)

if p_value < 0.05:
    print("Significant difference between A and B")
else:
    print("No significant difference")
