import numpy as np
import matplotlib.pyplot as plt
from space_base import GravBody, Probe


def gravsun(posvel):
    r = np.sqrt(posvel[0] ** 2 + posvel[1] ** 2); #print(r)
    f = -grav_constant * sun.mass / (r ** 3)
    return f * posvel[0], f * posvel[1]



# def probeqnsearth(t, posvel):
#     current_gravity = gravsun(posvel)
#     return current_gravity[0], current_gravity[1]
def probeqnsearth(t, posvel):
    current_gravity = gravsun(posvel[:2])
    aax, ay = current_gravity[0], current_gravity[1]
    return posvel[2], posvel[3], aax, ay



# Constants
grav_constant = 6.67e-11  # Gravitational constant
sun = GravBody("sun", mass=1.989e30, radius=6.96e8)
q = 1
V = np.sqrt(q*grav_constant*sun.mass/sun.radius)


AU =1.496e11 #radius of earths orbit
marsOrbit = 2.279e11 #radius of orbit

a = 1.262*AU
e = 0.208
r1 = AU
r2 = 1.524*r1
orbitEnergy = -(grav_constant*sun.mass)/(2*a)
print("The orbital energy = ", orbitEnergy)

P = np.sqrt(((4*np.pi**2)/(grav_constant*sun.mass))*(a**3))

ab = -(grav_constant*sun.mass)/(2*a)
abb = -(grav_constant*sun.mass)/r1
abc = -(grav_constant*sun.mass)/r2
v = np.sqrt((ab-abb)*2)
print("Initial speed = ", v)


V = np.sqrt(2*grav_constant*sun.mass*((1/a)-(1/(2*a)))) + 3280
print("Orbital speed for Earth = ", V)

vMars = np.sqrt((ab-abc)*2)
print("Speed when arriving at Mars = ", vMars)

VMars = V = np.sqrt(2*grav_constant*sun.mass*((1/marsOrbit)-(1/(2*marsOrbit))))
print("Orbital Speed of Mars = ", VMars)

#plotting the orbits
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

# Define time array
# t = np.linspace(1, V, 10)

# # Define function to be plotted
# y = np.sin(t)

# # Define initial probe value


# # Loop to update probe values

# # Plot the function
# ax.plot(t, y, 'b')



# z = posvel[:, 0] / 1e3; #print(z)
# zz = posvel[:, 1] / 1e3; #print(zz)


r_earth = 1
r_mars = 1.524
ax.plot(0, 0, 'yo', markersize = 20)

earth_orbit = plt.Circle((0, 0), r_earth, color = 'b', fill=False)
mars_orbit = plt.Circle((0, 0), r_mars, color = 'r', fill=False)
ax.add_artist(earth_orbit)
ax.add_artist(mars_orbit)

t_final = 300
t_num =  t_final
# plot the probe trajectory
z1 = range(1,2)

for i in z1:
    theta = 1*np.pi/12
    posvel0 = (r_earth, 0, V*np.sin(theta), V*np.cos(theta))
    probe = Probe(probeqnsearth, t_final, t_num,  x0=posvel0[0], 
                  y0=posvel0[1], vx0=posvel0[2], vy0=posvel0[3], event = marsOrbit)  # probe as an object
    t, posvel = probe.odesolve()  # solve the differential equations
    ax.plot(posvel[:, 0] / 1e3, posvel[:, 1] / 1e3)
    


ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_xlabel("AU")
ax.set_ylabel("AU")

# Extract the x and y positions from posvel
x_positions = posvel[:, 0]
y_positions = posvel[:, 1]

# # Plot the probe trajectory
# probe_pos = posvel[:, :2] / 1e11; #print(probe_pos)
ax.plot(x_positions, y_positions, 'g', label='Probe')
# ax.legend()


# Add labels and title
ax.set_title("Probe trajectory")

plt.show()  # Display the plot

