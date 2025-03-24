# Vesely’s Enhanced Approach for MooN

## Problem
IEC 61508 (Table D.5) and PDS Method Handbook use precomputed values for specific MooN architectures (up to 4oo5 and 7oo8, respectively). Vesely’s method generalizes CCF calculations, allowing for any MooN configuration, including large-scale redundancy (e.g., 3oo15, 4oo20, etc.).It provides a systematic, probability-based approach rather than relying on lookup tables.

## Solution
The Vesely approach is a probabilistic method that determines the probability of common cause failure in a system by considering all possible failure combinations. It was developed by Dr. William Vesely, a reliability engineering expert who contributed significantly to fault tree analysis and risk assessment methodologies. This project calculates the effective β-factor for any M-out-of-N (MooN) voting system beyond IEC 61508 and PDS Handbook tables.

**Example: 2oo3 Voting System using the Enhanced Vesely formula**

### Parameters
- ( M = 2 ): Minimum number of components required to fail for system failure.
- ( N = 3 ): Total number of redundant components.
- ( Channel 1 beta = 0.05 ): Base common cause failure fraction (5%).
- ( Channel 2 beta = 0.07 ): Base common cause failure fraction (7%).
- ( Channel 3 beta = 0.03 ): Base common cause failure fraction (3%).

### Vesely Formula

$$
\beta_{\text{MooN}} = \sum_{k=M}^{N} \binom{N}{k} \cdot \beta^k \cdot (1 - \beta)^{N - k}
$$

### Enhanced Example: 2oo3 with Non-Identical Beta Values

### Parameters

- M = 2
- N = 3
- Beta values:
  - Channel 1: 0.05
  - Channel 2: 0.07
  - Channel 3: 0.03

### Breakdown of Contributing Combinations

| Selected Channels | Unselected Channels | Probability Contribution |
|-------------------|---------------------|---------------------------|
| [1, 2]            | [3]                 | 0.003395                  |
| [1, 3]            | [2]                 | 0.001395                  |
| [2, 3]            | [1]                 | 0.001995                  |
| [1, 2, 3]         | []                  | 0.000105                  |
| **TOTAL**         |                     | **0.006890** → **0.6890%** |

By doing this we will be staying true to Vesely’s mathematical foundation while accounting for differences in channel susceptibility to common cause failure.

## Use Cases
- Fault Tree Analysis (FTA)
- Probabilistic Risk Assessment (PRA)
- Safety Instrumented Systems (SIS)
- Reliability Engineering
- Industrial Automation
- Nuclear and Aerospace Common Cause Failure Analysis

## Planned Enhancements
- GUI with Tkinter

## References
- IEC 61508-6 Table D.5
- PDS Method Handbook Appendix B
- Vesely, W.E. (Nuclear Regulatory Commission – Common Cause Failure Models)