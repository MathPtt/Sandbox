import numpy as np
import matplotlib.pyplot as plt


def f(x, r):
    """Returns y = r*x - x^3"""
    return r * x - x**3


def g(h):
    """Returns y = -h (constant line)"""
    return -h


r = 1.1
h = 0.0
# dense points for a smooth curve
x = np.linspace(-2, 2, 1000)

y1 = f(x, r)
y2 = np.full_like(x, g(h))


def find_equilibria(r, h):
    coeffs = [1, 0, -r, -h]
    roots = np.roots(coeffs)
    real_roots = roots[np.isreal(roots)].real
    return real_roots


equalibria = find_equilibria(r, h)
equalibria_y = f(equalibria, r)

# plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, "b-", label=f"y = rx - x^3 (r={r})")
plt.plot(x, y2, "r--", label=f"y = -h (r={h})")
plt.scatter(
    equalibria, equalibria_y, color="black", s=100, zorder=5, label="Equilibria"
)
plt.axhline(0, color="gray", linestyle="-", alpha=0.3)
plt.axvline(0, color="gray", linestyle="-", alpha=0.3)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Equilibrium Analysis: y = rx - x^3 and y = -h")
plt.grid(True)
plt.legend()

plt.savefig("book_example.png")
plt.close()

print(f"Parameters: r={r}, h={h}")
print(f"Equilibrium points: {equalibria}")
