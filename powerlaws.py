import numpy as np
import velocityverlet as vv
import matplotlib.pyplot as plt

GM = 4.0*np.pi**2		# [AU^3/yr^2]

N = 10000
T = 5.0						# One year
x0 = np.array([1.0, 0.0])			# [AU]
v0 = np.sqrt(GM)*np.array([0.1, np.sqrt(0.99)])	# [AU/yr]

b_ = np.linspace(2.0, 3.0, 2)

for b in b_:
	def F(t, x):
		r = np.linalg.norm(x)
		return -(GM/r**(b + 1))*x

	t, x, v = vv.solve(F, T, N, x0, v0)

	plt.plot(x[:, 0], x[:, 1], color="darkred")
	plt.title("Power law: $\\beta = " + str(b) + "$")
	plt.legend(("$x(t)$", "$y(t)$"))
	plt.xlabel("$t$")
	plt.show()

T = 20.0					# Twenty years

b = 2.02

def F(t, x):
	r = np.linalg.norm(x)
	return -(GM/r**(b + 1))*x

t, x, v = vv.solve(F, T, N, x0, v0)

plt.plot(x[:, 0], x[:, 1], color="darkred")
plt.title("Power law: $\\beta = " + str(b) + "$, $T = 20$ yr")
plt.xlabel("$x(t)$")
plt.ylabel("$y(t)$")
plt.show()