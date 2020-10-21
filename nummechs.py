import numpy as np

class Body:
	# This class represents a mechanical body with a mass, as well as 
	# a position and a velocity. It is merely used as a holder for these 
	# quantities, to be instantiated and held objects of another class to 
	# implement the mechanical laws of the bodies' motion.

	def __init__(self, mass, x=np.zeros(3), v=np.zeros(3)):
		# This function takes a number which represents the mass of 
		# the body, and a position and velocity vector as initial 
		# conditions.

		self.name = name
		self.mass = mass
		self.x, self.v = x, v

	def getName(self):
		# Returns the name of the body
		return self.name

	def getMass(self):
		# Returns the mass of the body
		return self.mass

	def getPosition(self):
		# Returns the position of the body
		return self.x

	def setPosition(self, x):
		# Sets the position of the body
		self.x = x

	def getVelocity(self):
		# Returns the velocity of the body
		return self.v

	def setVelocity(self, v):
		# Sets the velocity
		self.v = v

class MechanicalSystem:
	# This class is a holder of objects of the class Body, and must upon 
	# instantiation take a function which takes two Body objects and 
	# returns the momentary force with which they act on each other. As such, 
	# it will be assumed that the form of the force is the same for all the 
	# bodies.

	def __init__(self, F):
		self.F = F
		self.bodies = []

	def addBody(self, mass, x0=np.zeros(3), v0=np.zeros(3)):
		# Function which takes a name and a mass, as well as a position 
		# vector and a velocity vector, or else two zero vectors, and defines 
		# a Body object and adds to the list bodies

		self.bodies = self.bodies + [ Body(mass, x0, v0) ]

	def setInitialConditions(self, X0, V0):
		# Takes initial positions and velocities for all bodies in order, 
		# and sets the position and velocity of each object accordingly

		for i in range(len(self.bodies)):
			b = self.bodies[i]
			b.setPositon(X0[i])
			b.setVeloctiy(V0[i])

	def computeMotion(self, T, N):
		# Takes a total time and a number of time steps, and computes 
		# the positions and velocities of each body at every time 
		# n*dt, dt being T/N, based on the force law with which the 
		# MechanicalSystem object in question has been instantiated.
		# The method employed is the velocity Verlet method.

		d = len(self.bodies)		# Number of bodies in the system

		t = np.linspace(0.0, T, N + 1)	# Times, starting at t = 0.0
		dt = T/(1.0*N)			# Length of each time-step

		x = zeros((d, N + 1, 3))
		v = zeros((d, N + 1, 3))

		# Loop through the number of time-steps
		for n in range(N):
			v_mid = zeros((d, 3))

			# Loop through all bodies
			for i in range(d):
				# Create reference to body in question
				b_i = self.bodies[i]

				# Compute the total force on the body, and its 
				# acceleration
				F_n = zeros(3)
				for j in range(d):
					b_j = self.bodies[j]
					if j != i:
						F_n = F_n + F(t[n], b_i, b_j)
				a_n = total_force/b_i.getMass()

				# Estimate velocity v_mid at t + dt/2
				v_mid[i, :] = b_i.getVelocity() + a_n*dt/2.0

				# Compute x(t + dt) using v_mid, store result and 
				# set the Body object's position variable equal 
				# to it
				x[i, n + 1, :] = x[i, n, :] + v_mid*dt
				b_i.setPosition(x[i, n + 1])

			# Loop through bodies again to compute velocities
			for i in range(d):
				# Compute force on the body in question and its
				# acceleration at t + dt
				F_np1 = zeros(3)
				for j in range(d):
					b_j = self.bodies[j]
					if j != i:
						F_n = F_n + F(t[n], b_i, b_j)
				a_np1 = F_np1/b_i.getMass()

				# Use a(t + dt) to compute v(t + dt) from v_mid
				v[i, n + 1, :] = v_mid[i, :] + a_np1*dt/2.0
				b_i.setVelocity(v[i, n + 1])
		
		# Return time values and resulting positions, velocities
		return t, x, t