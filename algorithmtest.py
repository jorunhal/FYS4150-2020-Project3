import numpy as np
import eulerforward as ef
import velocityverlet as vv
import matplotlib.pyplot as plt
from time import perf_counter_ns

GM = 4.0*np.pi**2		# [AU^3/yr^2]

def F(t, x):
	r = np.linalg.norm(x)
	return -(GM/r**3)*x

N = 1000
T = 4.0					# One year
x0 = np.array([1.0, 0.0])		# [AU]
v0 = np.array([0.0, np.sqrt(GM)])	# [AU/yr]

# Forward Euler method

print("Euler forward method")
start = perf_counter_ns()/10**9
t, x, v = ef.solve(F, T, N, x0, v0)
end = perf_counter_ns()/10**9
print("\tTime taken (s): " + str(end-start))

plt.plot(t, x[:, 0])
plt.plot(t, x[:, 1])
plt.title("Euler Forward method: $x$- and $y$-coordinates")
plt.legend(("$x(t)$", "$y(t)$"))
plt.xlabel("$t$")
plt.show()

# Plot norms of position and velocity vector with time

plt.plot(t, np.linalg.norm(x, axis=1))
plt.plot(t, np.linalg.norm(v, axis=1)/(2.0*np.pi))
plt.title("Euler Forward method: $|\mathbf{x}(t)|$ and $|\mathbf{y}(t)|$")
plt.legend(("$|\mathbf{x}(t)|$", "$|\mathbf{v}(t)|/2\pi$"))
plt.axis([0.0, T, 0.0, 2.0])
plt.xlabel("$t$")
plt.show()

# Velocity Verlet method

print("Velocity Verlet method")
start = perf_counter_ns()/10**9
t, x, v = vv.solve(F, T, N, x0, v0)
end = perf_counter_ns()/10**9
print("\tTime taken (s): " + str(end - start))

plt.plot(t, x[:, 0])
plt.plot(t, x[:, 1])
plt.title("Velocity Verlet method: $x$- and $y$-coordinates")
plt.legend(("$x(t)$", "$y(t)$"))
plt.xlabel("$t$")
plt.show()

# Plot norms of position and velocity vector with time

plt.plot(t, np.linalg.norm(x, ord=2, axis=1))
plt.plot(t, np.linalg.norm(v, ord=2, axis=1)/(2.0*np.pi))
plt.title("Velocity Verlet method: $|\mathbf{x}(t)|$ and $|\mathbf{y}(t)|$")
plt.axis([0.0, T, 0.0, 1.5])
plt.legend(("$|\mathbf{x}(t)|$", "$|\mathbf{v}(t)|/2\pi$"))
plt.xlabel("$t$")
plt.show()