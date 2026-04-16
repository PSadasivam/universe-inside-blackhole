# Getting Started — Universe Inside a Black Hole

## Prerequisites

- **Python 3.10+** (tested with 3.13)
- Internet connection is **not required** — all computations use built-in constants

## 1. Environment Setup

```bash
# Clone or navigate to the project
cd universe-inside-blackhole

# Create virtual environment
python -m venv .venv

# Activate
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Running the Simulation

```bash
python black_hole_universe_simulation.py
```

### Expected Console Output

```
Critical density (Planck 2018): 8.500e-27 kg/m^3
Observable Universe radius: 4.408e+26 m
Total mass (critical density × volume): 3.045e+54 kg
Gravitational radius of that mass: 4.527e+27 m
Ratio of Universe radius / gravitational radius: 9.737e-02
```

### Generated Plot

The script produces a **bouncing scale factor** plot showing:
- X-axis: Cosmic time in billions of years (centered on the bounce at t=0)
- Y-axis: Scale factor a(t) in arbitrary units
- The curve reaches a minimum at t=0 (the bounce) and grows symmetrically in both directions

## 3. Understanding the Output

### Schwarzschild Radius Comparison

The ratio `Universe radius / Gravitational radius ≈ 0.097` means the observable universe's radius is about 10% of the Schwarzschild radius corresponding to its total mass. This means:
- The universe's mass, if concentrated, would form a black hole **larger** than the observable universe
- This is consistent with the hypothesis that we reside inside a black hole

### Bouncing Scale Factor

The model `a(t) = √(a_min² + (t/t₀)²)` avoids the Big Bang singularity:
- `a_min = 1.0` — minimum scale factor at the bounce (never reaches zero)
- `t₀ = 10¹⁷ s` — characteristic bounce timescale (~3.2 billion years)
- For |t| >> t₀, the scale factor grows linearly, resembling standard expansion

## 4. Modifying Parameters

Key variables in `black_hole_universe_simulation.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `H0_kms_per_Mpc` | 67.15 | Hubble constant (km/s/Mpc) |
| `radius_ly` | 46.6e9 | Observable universe radius (light-years) |
| `a_min` | 1.0 | Minimum scale factor at bounce |
| `t0` | 1e17 | Bounce timescale (seconds) |
| `t_max` | 2e17 | Simulation time range (seconds) |

## 5. Background Reading

- The `Research on black holes.pdf` document provides theoretical context for the hypothesis
- See the README for academic references on bouncing cosmology and Smolin's cosmological natural selection
