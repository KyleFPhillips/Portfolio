import numpy as np
import matplotlib.pyplot as plt
from space_base import GravBody, Probe

    
def atmosphere(h):
    surfacedens=mars.surface_density
    scaleheight=mars.scale_height   
    dens=surfacedens*np.exp(-h/scaleheight)
    return dens

def gravplanetearth(posvel):
    r = np.sqrt(posvel[0] ** 2 + posvel[1] ** 2 + posvel[2] ** 2)
    f = -grav_constant * mars.mass / r ** 3
    return f * posvel[0], f * posvel[1], f * posvel[2]


def probeqnsearth(t, posvel):
    current_gravity = gravplanetearth(posvel)
    cd = 1
    A = 0.01
    mass = 1
    radius =  (posvel[0]**2+posvel[1]**2+posvel[2]**2)**0.5
    height = radius - mars.radius
    density = atmosphere(height)
    speed = (posvel[3]**2+posvel[4]**2+posvel[5]**2)**0.5
    posveldot = [posvel[3], posvel[4], posvel[5], current_gravity[0]-0.5*cd*A*density*speed*posvel[3]/mass, current_gravity[1]-0.5*cd*A*density*speed*posvel[4]/mass, current_gravity[2]-0.5*cd*A*density*speed*posvel[5]/mass]
    return posveldot


# Constants
grav_constant = 6.67e-11  # Gravitational constant
mars  = GravBody("Mars", mass=6.4171e23, radius=3389.5e3, scale_height=11.1e3, surface_density=0.02) #look up scale height surface density in  nasa data sheet
q = 1
V = np.sqrt(q*grav_constant*mars.mass/mars.radius)


# Initial Conditions
t_final = 360000 # determined trajectory time
t_num = t_final  # number of steps in trajectory
fig = plt.figure(figsize=(15, 10))  # create figure, figsize can be changed as preferred
ax = fig.add_subplot(111, projection='3d')
# Running Solver in Loop
theta = np.pi/12
posvel0 = (47972e3, 0, 0, -347.7448, 347.7448*np.sin(1), 347.7448*np.cos(1))
probe = Probe(probeqnsearth, t_final, t_num,  x0=posvel0[0], y0=posvel0[1], z0=posvel0[2], vx0=posvel0[3], vy0=posvel0[4], vz0=posvel0[5], event = mars.radius)  # probe as an object
t, posvel = probe.odesolve()  # solve the differential equations
ax.plot(posvel[:, 0] / 1e3, posvel[:, 1] / 1e3, color='k')

# Plotting Moon
uang = np.linspace(0, 2 * np.pi, 100)
vang = np.linspace(0, np.pi, 100)
x0 = mars.radius / 1e3 * np.outer(np.cos(uang), np.sin(vang))
y0 = mars.radius / 1e3 * np.outer(np.sin(uang), np.sin(vang))
z0 = mars.radius / 1e3 * np.outer(np.ones(np.size(uang)), np.cos(vang))
ax.plot_surface(x0, y0, z0, color='blue')
ax.set_xlabel('x (km)')
ax.set_ylabel('y (km)')
ax.set_zlabel('z (km)')
ax.azim = -90
ax.elev = 90
plt.show()  # make plot appear
