import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# (1) Plot PDF for different Beta distributions
x = np.linspace(0, 1, 1000)

plt.figure(figsize=(12, 4))

# Beta(2,5)
plt.subplot(1, 3, 1)
plt.plot(x, beta.pdf(x, 2, 5), 'b-', linewidth=2)
plt.title('Beta(2,5)')
plt.xlabel('θ')
plt.ylabel('PDF')
plt.grid(True, alpha=0.3)

# Beta(5,5)
plt.subplot(1, 3, 2)
plt.plot(x, beta.pdf(x, 5, 5), 'g-', linewidth=2)
plt.title('Beta(5,5)')
plt.xlabel('θ')
plt.grid(True, alpha=0.3)

# Beta(0.5,0.5)
plt.subplot(1, 3, 3)
plt.plot(x, beta.pdf(x, 0.5, 0.5), 'r-', linewidth=2)
plt.title('Beta(0.5,0.5)')
plt.xlabel('θ')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('beta_distributions.png', dpi=150, bbox_inches='tight')
print("Saved: beta_distributions.png")

# (2) Explanation of shapes as prior beliefs
""" 
Prior beliefs about coin bias:

Beta(2,5): Believes coin is biased towards tails (more prior weight on low θ)
Beta(5,5): Symmetric, believes coin is likely fair (peaked at θ=0.5)
Beta(0.5,0.5): U-shaped, believes coin is either heavily biased to heads or tails
"""
# (3) Posterior update from Beta(1,1) prior with 7 heads in 10 flips
prior_alpha, prior_beta = 1, 1
observed_heads, observed_tails = 7, 3

# Posterior parameters (conjugate update)
posterior_alpha = prior_alpha + observed_heads
posterior_beta = prior_beta + observed_tails

print(f"\n(3) Posterior update:")
print(f"Prior: Beta({prior_alpha}, {prior_beta})")
print(f"Data: {observed_heads} heads, {observed_tails} tails")
print(f"Posterior: Beta({posterior_alpha}, {posterior_beta})")

# Plot prior vs posterior
plt.figure(figsize=(10, 5))
plt.plot(x, beta.pdf(x, prior_alpha, prior_beta), 'b--', label=f'Prior Beta({prior_alpha},{prior_beta})', linewidth=2)
plt.plot(x, beta.pdf(x, posterior_alpha, posterior_beta), 'r-', label=f'Posterior Beta({posterior_alpha},{posterior_beta})', linewidth=2)
plt.xlabel('θ (coin bias)')
plt.ylabel('PDF')
plt.title('Prior vs Posterior after observing 7 heads in 10 flips')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('prior_vs_posterior.png', dpi=150, bbox_inches='tight')
print("Saved: prior_vs_posterior.png")

# Posterior statistics
posterior_mean = posterior_alpha / (posterior_alpha + posterior_beta)
print(f"Posterior mean: {posterior_mean:.3f}")
print(f"This means we believe the coin has about {posterior_mean*100:.1f}% probability of landing heads")
