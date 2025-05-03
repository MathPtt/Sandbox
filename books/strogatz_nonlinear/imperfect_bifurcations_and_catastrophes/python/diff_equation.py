# 3.6 Imperfect Bifurcations and Catastrophes
#
# There is the:
# x = h + rx - (x on the third power)
#
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def ode(t, x, h, r):
    return h + r * x - x**3


# Parameters
h = 0.1
r = -0.1

# Time span for the solution
t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

# initial condition
x0 = [1.0]

# Solve the ODE using solve_ivp
sol = solve_ivp(
    fun=lambda t, x: ode(t, x, h, r),
    t_span=t_span,
    y0=x0,
    t_eval=t_eval,
    method="RK45",  # Runge-Kutta method for numerical integration
)

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], "b-", label=f"x(t), h={h}, r={r}")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.title("Solution of dx/dt = h + rx - x^3")
plt.grid(True)
plt.legend()

# Save the plot to a file
plt.savefig("diff_equation.png")
plt.close()


# Print equilibrium points
def find_equilibria(h, r):
    # Solve the cubic equation x^3 - r*x - h = 0
    coeffs = [1, 0, -r, -h]  # coefficients for x^3 + 0*x^2 - r*x - h
    roots = np.roots(coeffs)
    return roots


equilibria = find_equilibria(h, r)
print(f"Equilibrium points: {equilibria}")
