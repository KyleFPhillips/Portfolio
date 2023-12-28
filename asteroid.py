import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def eulereqns(t, angvel):
    return (-np.subtract(*principal_intertia[2:0:-1]) * np.multiply(*angvel[1:]) / principal_intertia[0],
            -np.subtract(*principal_intertia[::2]) * np.multiply(*angvel[::-2]) / principal_intertia[1],
            -np.subtract(*principal_intertia[1::-1]) * np.multiply(*angvel[:2]) / principal_intertia[2])


principal_intertia = np.array([1, 2, 4])
angvel0 = np.array([0.01, 0.01, 1])
tfinal = 1000
inenergy = 0.5 * np.sum(principal_intertia * angvel0 ** 2)
tspan = [0, tfinal, int(1e4)]
angvel = odeint(eulereqns, angvel0, np.linspace(*tspan), tfirst=True)
tend = len(angvel) - 1
finenergy = 0.5 * np.sum(principal_intertia * angvel[tend] ** 2)
accuracy = abs((finenergy - inenergy) / inenergy)
print(f'Accuracy = {accuracy: .4%}')
plt.figure(1, figsize=(8, 5))
plt.plot(angvel[:, 2], angvel[:, 1])
fig = plt.figure(2, figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot(angvel[:, 2], angvel[:, 1], angvel[:, 0])
plt.show()
