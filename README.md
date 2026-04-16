# Universe Inside a Black Hole — Bouncing Cosmology Simulation

A numerical simulation exploring the hypothesis that our observable universe resides inside a black hole, using Planck 2018 cosmological parameters and a bouncing scale factor model.

**ORCID**: [https://orcid.org/0009-0008-0069-693X](https://orcid.org/0009-0008-0069-693X)

## Overview

This project computes whether the observable universe's total mass fits within its own Schwarzschild radius — a key prediction of the "universe inside a black hole" hypothesis — and models a bouncing cosmology where the Big Bang singularity is replaced by a smooth minimum in the scale factor.

### What does this simulation do?

1. **Schwarzschild radius comparison** — Computes the gravitational radius of the universe's total mass (from critical density × observable volume) and compares it to the actual comoving radius
2. **Bouncing scale factor model** — Replaces the Big Bang singularity with a symmetric bounce: `a(t) = √(a_min² + (t/t₀)²)`
3. **Visualization** — Generates a plot of the scale factor evolution showing contraction, bounce, and expansion phases

## Key Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Hubble constant (H₀) | 67.15 km/s/Mpc | Planck 2018 |
| Critical density (ρ_crit) | ~8.5 × 10⁻²⁷ kg/m³ | Derived |
| Observable universe radius | 46.6 billion light-years | Comoving |
| Gravitational constant (G) | 6.67430 × 10⁻¹¹ m³ kg⁻¹ s⁻² | CODATA |
| Speed of light (c) | 299,792,458 m/s | Exact |

## The Hypothesis

If we calculate the total mass of the observable universe using the critical density and comoving volume, its Schwarzschild radius is remarkably close to the actual radius of the observable universe. This coincidence motivates the hypothesis that our universe may exist inside the event horizon of a massive black hole.

The bouncing cosmology model extends this idea: rather than a singular Big Bang, the universe undergoes a smooth bounce at a minimum scale factor, consistent with what might occur inside a black hole's interior where classical singularity theorems may be modified by quantum gravity effects.

## Repository Structure

```
universe-inside-blackhole/
├── README.md                              # This file
├── LICENSE                                # MIT License
├── requirements.txt                       # Python dependencies
├── black_hole_universe_simulation.py      # Main simulation script
├── docs/
│   └── getting-started.md                 # Setup and usage guide
├── Research on black holes.docx           # Background research document
└── Research on black holes.pdf            # Background research (PDF)
```

## Output

The simulation prints computed values to the console:

```
Critical density (Planck 2018): 8.500e-27 kg/m^3
Observable Universe radius: 4.408e+26 m
Total mass (critical density × volume): 3.045e+54 kg
Gravitational radius of that mass: 4.527e+27 m
Ratio of Universe radius / gravitational radius: 9.737e-02
```

And generates a bouncing scale factor plot showing cosmic time (billions of years) vs scale factor.

## Technical Requirements

- Python 3.10+
- `numpy` — Numerical computing
- `matplotlib` — Plotting

## References

- **Planck 2018 Results** — Planck Collaboration (2020), A&A 641, A6
- **Schwarzschild metric** — K. Schwarzschild (1916), Sitzungsber. Preuss. Akad. Wiss.
- **Universe inside a black hole** — L. Smolin (1992), *Did the Universe Evolve?*, Class. Quantum Grav. 9, 173
- **Bouncing cosmology** — R. Brandenberger & P. Peter (2017), *Bouncing Cosmologies: Progress and Problems*, Found. Phys. 47, 797

## License & Attribution

**Developer**: Prabhu Sadasivam
**ORCID**: https://orcid.org/0009-0008-0069-693X

Data and constants courtesy of Planck Collaboration and CODATA.
