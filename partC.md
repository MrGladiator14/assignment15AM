# Part C - Interview Questions

## Q1 — Base Rate Fallacy

The base rate fallacy occurs when we ignore the base rate (prior probability) of an event and focus only on specific information, leading to incorrect probability assessments.

**Medical Test Example:**
- Disease prevalence: 1 in 10,000 people (0.01%)
- Test accuracy: 99% (both sensitivity and specificity)
- Population: 1,000,000 people

**Analysis:**
- **True positives:** 100 people have the disease × 99% detection = 99 true positives
- **False negatives:** 100 people × 1% missed = 1 false negative
- **True negatives:** 999,900 healthy people × 99% correctly identified = 989,901 true negatives
- **False positives:** 999,900 healthy people × 1% false alarm = 9,999 false positives

**Result:** Out of 10,098 positive tests, only 99 are actually positive (0.98% PPV).

**Why mostly false positives:** The extremely low base rate (0.01%) means that even with a highly accurate test, the vast majority of positive results come from testing the large healthy population rather than the tiny diseased population.

---

## Q2 — Central Limit Theorem Simulation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def simulate_clt(distribution, params, n_samples, n_simulations=1000):
    dist = distribution(**params)
    theoretical_mean = dist.mean()
    theoretical_std = np.sqrt(dist.var() / n_samples)
    
    sample_means = [np.mean(dist.rvs(size=n_samples)) for _ in range(n_simulations)]
    sample_means = np.array(sample_means)
    
    plt.figure(figsize=(12, 6))
    plt.hist(sample_means, bins=50, density=True, alpha=0.7, color='skyblue', label='Sample Means')
    
    x = np.linspace(sample_means.min(), sample_means.max(), 1000)
    plt.plot(x, stats.norm.pdf(x, theoretical_mean, theoretical_std), 'r-', linewidth=2,
             label=f'Normal Approximation\nμ={theoretical_mean:.3f}, σ={theoretical_std:.3f}')
    
    plt.title(f'CLT: {distribution.__name__}, n={n_samples}, simulations={n_simulations}')
    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return sample_means, theoretical_mean, theoretical_std
```

**Key Features:**
- Works with any scipy.stats distribution
- Calculates theoretical sampling distribution parameters
- Generates sample means through simulation
- Creates visualization comparing empirical distribution to theoretical normal
- Returns both empirical and theoretical results for comparison

---

## Q3 — Customer Purchase Amounts Analysis

**Why mean purchase amount is misleading:**

For exponential distributions (common for customer purchases), the mean is heavily influenced by a few very large purchases while most customers make small purchases. This creates a skewed distribution where:

- **Mean ≠ Median:** The mean is pulled upward by outliers
- **High variance:** Most purchases are clustered near zero, but rare large purchases inflate the average
- **Misleading business decisions:** Investors might overestimate typical customer behavior

**What to show instead:**

1. **Median purchase amount:** More representative of typical customer behavior
2. **Distribution visualization:** Histogram or density plot showing the exponential shape
3. **Percentile breakdown:** 25th, 50th (median), 75th, 90th, 95th percentiles
4. **Customer segments:** 
   - Percentage of customers under $X
   - Average purchase amount by customer segment
   - Repeat vs. first-time customer behavior

**Example metrics to present:**
- Median purchase: $15 (vs. mean of $45)
- 80% of purchases under $25
- Top 5% of customers account for 60% of revenue
- Average purchase for repeat customers: $35 vs. first-time: $12

This approach gives investors a more accurate picture of customer behavior and revenue drivers.
