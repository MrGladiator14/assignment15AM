#!/usr/bin/env python3
"""
Central Limit Theorem Simulation for Product Managers.

This script demonstrates how the CLT transforms non-normal distributions
into normal sampling distributions through repeated sampling.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple
import random


def generate_bimodal_distribution(sample_size: int = 10000) -> np.ndarray:
    """
    Generate a bimodal distribution (two peaks) to simulate non-normal data.
    
    This represents real-world scenarios like user engagement where you have
    two distinct user groups (e.g., power users vs casual users).
    
    Args:
        sample_size: Number of data points to generate
        
    Returns:
        Array of bimodally distributed data
    """
    # Mix of two normal distributions with different means
    group1 = np.random.normal(loc=2.0, scale=0.5, size=sample_size // 2)
    group2 = np.random.normal(loc=8.0, scale=1.0, size=sample_size // 2)
    
    return np.concatenate([group1, group2])


def generate_exponential_distribution(sample_size: int = 10000) -> np.ndarray:
    """
    Generate an exponential distribution to simulate skewed data.
    
    This represents scenarios like customer purchase amounts or time between events.
    
    Args:
        sample_size: Number of data points to generate
        
    Returns:
        Array of exponentially distributed data
    """
    return np.random.exponential(scale=2.0, size=sample_size)


def calculate_sample_means(
    population_data: np.ndarray,
    sample_size: int,
    num_samples: int
) -> List[float]:
    """
    Calculate means of repeated samples from the population.
    
    Args:
        population_data: The complete population data
        sample_size: Size of each sample
        num_samples: Number of samples to draw
        
    Returns:
        List of sample means
    """
    sample_means = []
    
    for _ in range(num_samples):
        # Randomly sample without replacement
        sample = np.random.choice(
            population_data,
            size=sample_size,
            replace=False
        )
        sample_means.append(np.mean(sample))
    
    return sample_means


def create_visualization(
    original_data: np.ndarray,
    sample_means_exponential: List[float],
    sample_means_bimodal: List[float]
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create comprehensive visualization of CLT demonstration.
    
    Args:
        original_data: Original population data
        sample_means_exponential: Sample means from exponential distribution
        sample_means_bimodal: Sample means from bimodal distribution
        
    Returns:
        Matplotlib figure and axes objects
    """
    # Set up the plotting style
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Central Limit Theorem: From Messy Data to Normal Distributions', 
                 fontsize=16, fontweight='bold')
    
    # Generate exponential data for demonstration
    exp_data = generate_exponential_distribution(10000)
    bimodal_data = generate_bimodal_distribution(10000)
    
    # Row 1: Original Distributions
    # Exponential distribution
    axes[0, 0].hist(exp_data, bins=50, alpha=0.7, color='red', density=True)
    axes[0, 0].set_title('Original Exponential Distribution\n(Skewed Data)', 
                         fontweight='bold')
    axes[0, 0].set_xlabel('Value')
    axes[0, 0].set_ylabel('Density')
    
    # Bimodal distribution
    axes[0, 1].hist(bimodal_data, bins=50, alpha=0.7, color='orange', density=True)
    axes[0, 1].set_title('Original Bimodal Distribution\n(Two User Groups)', 
                         fontweight='bold')
    axes[0, 1].set_xlabel('Value')
    axes[0, 1].set_ylabel('Density')
    
    # Combined view
    axes[0, 2].hist(exp_data, bins=50, alpha=0.5, color='red', density=True, 
                   label='Exponential')
    axes[0, 2].hist(bimodal_data, bins=50, alpha=0.5, color='orange', density=True,
                   label='Bimodal')
    axes[0, 2].set_title('Both Non-Normal Distributions', fontweight='bold')
    axes[0, 2].set_xlabel('Value')
    axes[0, 2].set_ylabel('Density')
    axes[0, 2].legend()
    
    # Row 2: Sampling Distributions (CLT in action!)
    # Exponential sampling distribution
    axes[1, 0].hist(sample_means_exponential, bins=30, alpha=0.7, 
                   color='blue', density=True)
    axes[1, 0].set_title('Sampling Distribution\n(Exponential → Normal)', 
                         fontweight='bold')
    axes[1, 0].set_xlabel('Sample Mean')
    axes[1, 0].set_ylabel('Density')
    
    # Bimodal sampling distribution
    axes[1, 1].hist(sample_means_bimodal, bins=30, alpha=0.7, 
                   color='green', density=True)
    axes[1, 1].set_title('Sampling Distribution\n(Bimodal → Normal)', 
                         fontweight='bold')
    axes[1, 1].set_xlabel('Sample Mean')
    axes[1, 1].set_ylabel('Density')
    
    # Combined sampling distributions
    axes[1, 2].hist(sample_means_exponential, bins=30, alpha=0.5, 
                   color='blue', density=True, label='Exp. Samples')
    axes[1, 2].hist(sample_means_bimodal, bins=30, alpha=0.5, 
                   color='green', density=True, label='Bimodal Samples')
    axes[1, 2].set_title('CLT Result: Both Become Normal!', fontweight='bold')
    axes[1, 2].set_xlabel('Sample Mean')
    axes[1, 2].set_ylabel('Density')
    axes[1, 2].legend()
    
    plt.tight_layout()
    return fig, axes


def print_statistics(
    sample_means_exponential: List[float],
    sample_means_bimodal: List[float]
) -> None:
    """
    Print key statistics demonstrating the CLT.
    
    Args:
        sample_means_exponential: Sample means from exponential distribution
        sample_means_bimodal: Sample means from bimodal distribution
    """
    print("\n" + "="*60)
    print("CENTRAL LIMIT THEOREM DEMONSTRATION RESULTS")
    print("="*60)
    
    print("\n📊 SAMPLING DISTRIBUTION STATISTICS:")
    print(f"{'':20} {'Exponential':>15} {'Bimodal':>15}")
    print("-" * 55)
    
    # Calculate statistics
    exp_mean = np.mean(sample_means_exponential)
    exp_std = np.std(sample_means_exponential)
    bimodal_mean = np.mean(sample_means_bimodal)
    bimodal_std = np.std(sample_means_bimodal)
    
    print(f"{'Mean of Sample Means':20} {exp_mean:>15.3f} {bimodal_mean:>15.3f}")
    print(f"{'Std Dev of Samples':20} {exp_std:>15.3f} {bimodal_std:>15.3f}")
    
    # Theoretical vs actual standard error
    exp_true_mean = 2.0  # True mean of exponential(2.0)
    bimodal_true_mean = 5.0  # True mean of our bimodal distribution
    
    print(f"\n🎯 ACCURACY CHECK:")
    print(f"Exponential - True Mean: {exp_true_mean:.3f}, "
          f"Sample Mean: {exp_mean:.3f}, Error: {abs(exp_mean - exp_true_mean):.3f}")
    print(f"Bimodal - True Mean: {bimodal_true_mean:.3f}, "
          f"Sample Mean: {bimodal_mean:.3f}, Error: {abs(bimodal_mean - bimodal_true_mean):.3f}")
    
    print(f"\n🔍 CLT INSIGHT:")
    print(f"• Both messy distributions became approximately normal")
    print(f"• Sample means cluster around true population means")
    print(f"• Standard deviation decreases with larger samples")
    print(f"• This enables reliable A/B testing p-values!")


def main() -> None:
    """
    Main function to run the CLT simulation.
    """
    print("🎲 Central Limit Theorem Simulation for Product Managers")
    print("=" * 60)
    
    # Simulation parameters
    SAMPLE_SIZE = 50  # Size of each sample
    NUM_SAMPLES = 1000  # Number of samples to draw
    POPULATION_SIZE = 10000  # Size of population
    
    print(f"\n📋 SIMULATION PARAMETERS:")
    print(f"• Sample size: {SAMPLE_SIZE}")
    print(f"• Number of samples: {NUM_SAMPLES}")
    print(f"• Population size: {POPULATION_SIZE}")
    
    # Generate population data
    print(f"\n🔧 Generating non-normal population data...")
    exp_population = generate_exponential_distribution(POPULATION_SIZE)
    bimodal_population = generate_bimodal_distribution(POPULATION_SIZE)
    
    # Calculate sample means
    print(f"📊 Calculating sample means (this demonstrates CLT)...")
    sample_means_exp = calculate_sample_means(
        exp_population, SAMPLE_SIZE, NUM_SAMPLES
    )
    sample_means_bimodal = calculate_sample_means(
        bimodal_population, SAMPLE_SIZE, NUM_SAMPLES
    )
    
    # Create visualization
    print(f"📈 Creating visualization...")
    fig, axes = create_visualization(
        exp_population, sample_means_exp, sample_means_bimodal
    )
    
    # Print statistics
    print_statistics(sample_means_exp, sample_means_bimodal)
    
    # Save the plot
    plt.savefig('/home/bryson/dev/week-3/assignment15AM/clt_visualization.png', 
                dpi=300, bbox_inches='tight')
    print(f"\n💾 Visualization saved as 'clt_visualization.png'")
    
    print(f"\n🎉 CLT Simulation Complete!")
    print(f"   The visualization shows how messy data becomes normal through averaging!")


if __name__ == "__main__":
    main()
