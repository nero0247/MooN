# Vesely’s Approach for MooN

## Problem
IEC 61508 (Table D.5) and PDS Method Handbook use precomputed values for specific MooN architectures (up to 4oo5 and 7oo8, respectively).
Vesely’s method generalizes CCF calculations, allowing for any MooN configuration, including large-scale redundancy (e.g., 3oo15, 4oo20, etc.).It provides a systematic, probability-based approach rather than relying on lookup tables.

## Solution
The Vesely approach is a probabilistic method that determines the probability of common cause failure in a system by considering all possible failure combinations. It was developed by Dr. William Vesely, a reliability engineering expert who contributed significantly to fault tree analysis and risk assessment methodologies. This project calculates the effective β-factor for any M-out-of-N (MooN) voting system beyond IEC 61508 and PDS Handbook tables.

**Example: 2oo3 Voting System using the Vesely formula**

### Parameters

- ( M = 2 ): Minimum number of components required to fail for system failure.
- ( N = 3 ): Total number of redundant components.
- ( beta = 0.05 ): Base common cause failure fraction (5%).

### Vesely Formula

$$
\beta_{\text{MooN}} = \sum_{k=M}^{N} \binom{N}{k} \cdot \beta^k \cdot (1 - \beta)^{N - k}
$$

### Apply to 2oo3
$$
\beta_{2oo3} = \sum_{k=2}^{3} \binom{3}{k} \cdot (0.05)^k \cdot (1 - 0.05)^{3 - k}
$$

**Break it down:**

#### 1. Term for ( k = 2 )
$$
\binom{3}{2} \cdot (0.05)^2 \cdot (0.95)^1 = 3 \cdot 0.0025 \cdot 0.95 = 0.007125
$$

#### 2. Term for ( k = 3 )
$$
\binom{3}{3} \cdot (0.05)^3 \cdot (0.95)^0 = 1 \cdot 0.000125 \cdot 1 = 0.000125
$$

### Final Calculation

$$
\beta_{2oo3} = 0.007125 + 0.000125 = 0.00725
$$

So the system wide beta factor for a 2oo3 system with a base 5% common cause failure rate is:
$$
(\beta_{2oo3} \approx 0.00725 )\ or\ 0.725\%
$$

## Problems with this Approach
The issue with this approach is that the general MooN beta factor calculation assumes that all components/channels are identical in terms of:

- Failure rates
- Exposure to common cause
- Operational role

What this means is all channels are assumed to have equal probability of independent and common cause failure. The beta factor is applied uniformly across all channels. There is no weighting or differentiation between channels so a voter, a sensor, or a logic solver are all treated as functionally symmetric if included in the MooN count.

Different channels may have different technologies (e.g., pressure switch vs. smart transmitter). Some may be more exposed to environmental conditions or more complex in function. One channel may be more critical or have a higher demand rate. This uniform assumption simplifies calculations but may overestimate or underestimate actual risk in non-homogeneous systems.

## Use Cases
- Fault Tree Analysis (FTA)
- Probabilistic Risk Assessment (PRA)
- Safety Instrumented Systems (SIS)
- Reliability Engineering
- Industrial Automation
- Nuclear and Aerospace Common Cause Failure Analysis

## Planned Enhancements
- GUI with Tkinter
- Support for heterogeneous failure rates per channel

## References

- IEC 61508-6 Table D.5
- PDS Method Handbook Appendix B
- Vesely, W.E. (Nuclear Regulatory Commission – Common Cause Failure Models)