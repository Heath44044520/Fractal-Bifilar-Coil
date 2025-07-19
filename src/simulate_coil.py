# src/simulate_coil.py
import numpy as np
import matplotlib.pyplot as plt

def fractal_bifilar_field(frequency=7.83, turns=20, radius=0.1, fractal_factor=1.2):
    """Simulate magnetic field of a fractal bifilar coil."""
    mu_0 = 4 * np.pi * 1e-7
    current = 1.0
    r = np.linspace(-0.2, 0.2, 100)
    B = mu_0 * current * turns * fractal_factor / (2 * np.pi * np.sqrt(radius**2 + r**2))
    plt.plot(r, B)
    plt.xlabel("Distance (m)")
    plt.ylabel("Magnetic Field (T)")
    plt.title(f"Fractal Bifilar Coil Field at {frequency} Hz")
    plt.savefig("data/field_plot.png")
    plt.show()

if __name__ == "__main__":
    fractal_bifilar_field()
