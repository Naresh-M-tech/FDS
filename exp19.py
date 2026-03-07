import numpy as np
import scipy.stats as stats

drug = np.array([8,9,6,7,10,8,9,7])
placebo = np.array([3,4,2,5,3,4,3,2])

confidence = 0.95

drug_ci = stats.t.interval(confidence,
                           len(drug)-1,
                           loc=np.mean(drug),
                           scale=stats.sem(drug))

placebo_ci = stats.t.interval(confidence,
                              len(placebo)-1,
                              loc=np.mean(placebo),
                              scale=stats.sem(placebo))

print("Drug CI:", drug_ci)
print("Placebo CI:", placebo_ci)
