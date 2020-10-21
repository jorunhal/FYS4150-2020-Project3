import numpy as np

def solve(f, T, N, x0, v0):
	# This function implements the velocity Verlet method to solve
	# a second-order integration of the form 
	# 	x''(t) = f(t, x(t))
	# for some function f, with initial conditions x(0) = x0 and 
	# x'(0) = v0, for a set of N evenly spaced points in time, 
	# starting at t = 0 and ending at t = T. The function f, the 
	# initial conditions, the end-time T and the number of timesteps 
	# are given as arguments. The points in time and the computed 
	# positions and velocities are returned in respective arrays.

	t = np.linspace(0.0, T, N + 1)
	dt = T/N

	if isinstance(x0, np.ndarray):
		d = len(x0)
		x, v = np.zeros((2, N + 1, d))
		x[0, :] = x0
		v[0, :] = v0

		for n in range(N):
			v_mid = v[n, :] + f(t[n], x[n, :])*dt/2.0
			x[n + 1, :] = x[n, :] + v_mid*dt
			v[n + 1, :] = v_mid + f(t[n + 1], x[n + 1, :])*dt/2.0

		return t, x, v
	else:
		x, v = np.zeros((2, N + 1))
		x[0] = x0
		v[0] = v0

		for n in range(N):
			v_mid = v[n] + f(t[n], x[n])*dt/2.0
			x[n + 1] = x[n] + v_mid*dt
			v[n + 1] = v_mid + f(t[n + 1], x[n + 1])*dt/2.0

		return t, x, v