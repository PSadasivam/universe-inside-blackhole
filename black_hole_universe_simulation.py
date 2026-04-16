import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
c = 299792458.0  # speed of light (m/s)

# Current cosmological parameters (Planck 2018 values)
H0_kms_per_Mpc = 67.15  # Hubble constant in km/s/Mpc
H0 = H0_kms_per_Mpc * 1000 / (3.08567758128e22)  # convert to s^-1
rho_crit = 3 * H0**2 / (8 * np.pi * G)  # critical density (kg/m^3)

# Volume of the observable Universe (comoving radius 46.6 billion light-years)
radius_ly = 46.6e9  # radius in light‑years
meters_per_ly = 9.4607304725808e15
radius_m = radius_ly * meters_per_ly
volume_universe = (4/3) * np.pi * radius_m**3  # volume (m^3)

# Total mass from the critical density
mass_total = rho_crit * volume_universe  # kg

# Gravitational (Schwarzschild) radius corresponding to this mass
R_g = 2 * G * mass_total / c**2  # m

print("Critical density (Planck 2018): {:.3e} kg/m^3".format(rho_crit))
print("Observable Universe radius: {:.3e} m".format(radius_m))
print("Total mass (critical density × volume): {:.3e} kg".format(mass_total))
print("Gravitational radius of that mass: {:.3e} m".format(R_g))
print("Ratio of Universe radius / gravitational radius: {:.3e}".format(radius_m / R_g))

# Simple bounce model for the scale factor
t_max = 2e17  # seconds (approx 6.3 billion years) for demonstration
n_points = 1000
t = np.linspace(-t_max, t_max, n_points)

# Choose a minimal scale factor at the bounce (dimensionless)
a_min = 1.0
# Characteristic time scale of the bounce (in seconds)
t0 = 1e17  # adjust to set how sharply the bounce occurs

# Define a symmetric bouncing scale factor: a(t) = sqrt(a_min^2 + (t/t0)^2)
a = np.sqrt(a_min**2 + (t / t0)**2)

# Plot the bouncing scale factor
earth_years_per_sec = 1/(3600*24*365.25)
t_years = t * earth_years_per_sec

plt.figure(figsize=(8, 5))
plt.plot(t_years / 1e9, a)
plt.xlabel('Cosmic time (billions of years relative to bounce)')
plt.ylabel('Scale factor a(t) (arbitrary units)')
plt.title('Illustrative bouncing universe with a minimal scale factor at t=0')
plt.axvline(0, color='k', linestyle='--', linewidth=0.8)
plt.grid(True)

# Save the plot
plt.tight_layout()
plt.savefig('bounce_scale_factor.png', dpi=300)
plt.show()
