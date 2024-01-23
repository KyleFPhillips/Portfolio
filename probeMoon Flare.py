import numpy as np
import matplotlib.pyplot as plt
from space_base import GravBody, Probe


def gravplanetearth(posvel):
    r = np.sqrt(posvel[0] ** 2 + posvel[1] ** 2 + posvel[2] ** 2)
    f = -grav_constant * moon.mass / r ** 3
    return f * posvel[0], f * posvel[1], f * posvel[2]


def probeqnsearth(t, posvel):
    current_gravity = gravplanetearth(posvel)
    return posvel[3], posvel[4], posvel[5], current_gravity[0], current_gravity[1], current_gravity[2]


# Constants
grav_constant = 6.67e-11  # Gravitational constant
moon  = GravBody("Moon", mass=7.34767309e22, radius=1737400)
q = 1
V = np.sqrt(q*grav_constant*moon.mass/moon.radius)



# Initial Conditions
t_final = 3600 * 12  # determined trajectory time
t_num = t_final  # number of steps in trajectory
fig = plt.figure(figsize=(15, 10))  # create figure, figsize can be changed as preferred
ax = fig.add_subplot(111, projection='3d')
# Running Solver in Loop
z1 = range(-6,6)
z2 = -6
for i in z1:
    z2 = z2 + 1
    theta = z2*np.pi/12
    posvel0 = (moon.radius, 0, 0, V*np.sin(theta), V*np.cos(theta), 0)
    probe = Probe(probeqnsearth, t_final, t_num,  x0=posvel0[0], 
                  y0=posvel0[1], z0=posvel0[2], vx0=posvel0[3], 
                  vy0=posvel0[4], vz0=posvel0[5], event = moon.radius)  # probe as an object
    t, posvel = probe.odesolve()  # solve the differential equations
    ax.plot(posvel[:, 0] / 1e3, posvel[:, 1] / 1e3, label = theta) 
    ax.plot(posvel[:, 0] / 1e3, -posvel[:, 1] / 1e3, label = theta)# plot probe
    plt.legend() # adding the thetas to the legend
# Plotting Moon
uang = np.linspace(0, 2 * np.pi, 100)
vang = np.linspace(0, np.pi, 100)
x0 = moon.radius / 1e3 * np.outer(np.cos(uang), np.sin(vang))
y0 = moon.radius / 1e3 * np.outer(np.sin(uang), np.sin(vang))
z0 = moon.radius / 1e3 * np.outer(np.ones(np.size(uang)), np.cos(vang))
ax.plot_surface(x0, y0, z0, color='blue')
ax.set_xlabel('x (km)')
ax.set_ylabel('y (km)')
ax.set_zlabel('z (km)')
ax.azim = -90
ax.elev = 90
plt.show()  # make plot appear
