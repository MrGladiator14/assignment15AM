"""
For each scenario:
(a) Identify distribution
(b) Justify with 2 specific reasons
(c) Sketch description of PDF/PMF
(d) Compute probability using scipy.stats
"""

from scipy import stats
import numpy as np

# Website traffic
"""
SCENARIO 1: Website traffic - 200 requests/minute on average
Question: P(more than 220 requests in a minute)?

(a) Distribution: Poisson(λ=200)

(b) Justification:
    1. Events occur independently 
    2. Constant average rate (200 requests/minute) over time interval
    3. Events are rare relative to time interval (individual requests are instantaneous)

(d) Computation:
"""
lam1 = 200
p1 = 1 - stats.poisson.cdf(220, lam1)
print(f"S1  P(X > 220)           = {p1:.4f}") 

# Quality control 
"""
SCENARIO 2: Quality control - 2% defective bolts in batch of 50
Question: P(exactly 3 defective)?

(a) Distribution: Binomial(n=50, p=0.02)

(b) Justification:
    1. Fixed number of trials 
    2. Each bolt has same probability of being defective (p=0.02)
    3. Trials are independent 


(d) Computation:
"""
n2, p2 = 50, 0.02
prob2 = stats.binom.pmf(3, n2, p2)
print(f"S2  P(X = 3)            = {prob2:.4f}")  

# Delivery times
"""
SCENARIO 3: Delivery times - Normal(μ=45 min, σ=8)
Question: P(delivery > 60 min)? P(between 40 and 50 min)?

(a) Distribution: Normal(μ=45, σ=8)

(b) Justification:
    1. Delivery times are continuous and tend to cluster around mean
    2. Natural phenomenon affected by many small independent factors
    3. Symmetric distribution is reasonable for delivery times

(d) Computation:
"""
mu3, sigma3 = 45, 8
dist3 = stats.norm(mu3, sigma3)

p3a = 1 - dist3.cdf(60)
p3b = dist3.cdf(50) - dist3.cdf(40)
z60 = (60 - mu3) / sigma3

print(f"S3  P(X > 60)           = {p3a:.4f}")
print(f"S3  P(40 < X < 50)     = {p3b:.4f}")
print(f"S3  z-score at x=60    = {z60:.3f}")

# Customer arrivals
"""
SCENARIO 4: Customer arrivals - 10/hour
Question: P(no customers in next 6 minutes)?

(a) Distribution: Poisson(λ = 10 × 6/60 = 1.0)

(b) Justification:
    1. Events occur randomly and independently in time
    2. Constant average rate (10 customers/hour)
    3. We're counting events in a fixed time interval

(d) Computation:
"""
lam4 = 10 * (6/60)
p4 = stats.poisson.pmf(0, lam4)
print(f"S4  P(X = 0) in 6 min  = {p4:.4f}")

# CLT class of 35
"""
SCENARIO 5: Class of 35 students - CLT approximation
Question: Approximate distribution of class average score

(a) Distribution: Normal(μ, σ/√n) by CLT
   If individual scores ~ (μ=70, σ=15), then X̄ ~ Normal(70, 15/√35)

(b) Justification:
    1. Sample size n=35 is sufficiently large for CLT
    2. Sample mean approaches normal distribution
    3. Standard error decreases as σ/√n

(d) Computation:
"""
mu5, sigma5, n5 = 70, 15, 35
se5 = sigma5 / np.sqrt(n5)
dist5 = stats.norm(mu5, se5)

print(f"S5  Standard error      = {se5:.4f}")
print(f"S5  P(X̄ > 75)          = {1-dist5.cdf(75):.4f}")
print(f"S5  95% CI half-width   = {1.96*se5:.2f}")

# Summary of Results
print("\n" + "="*60)
print("SUMMARY OF PROBABILITY CALCULATIONS")
print("="*60)
print(f"S1 (Poisson):    P(X > 220)              = {p1:.4f}")
print(f"S2 (Binomial):   P(X = 3)                = {prob2:.4f}")
print(f"S3 (Normal):     P(X > 60)               = {p3a:.4f}")
print(f"S3 (Normal):     P(40 < X < 50)          = {p3b:.4f}")
print(f"S4 (Poisson):    P(X = 0) in 6 min       = {p4:.4f}")
print(f"S5 (CLT):        P(X̄ > 75)               = {1-dist5.cdf(75):.4f}")
print("="*60)
