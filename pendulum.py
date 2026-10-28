import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

mass = 2
length = 2
phi = np.radians(90)

t = 0
dt = 0.001

x = length * np.sin(phi)
y = length - length * np.cos(phi)

vx = 0
vy = 0

xa = []
ya = []

def calc_ds(x, y, phi, vx, vy):
    force = np.array([
        -mass * (vx ** 2 + vy ** 2) / length * np.sin(phi)
        - mass * 9.81 * np.sin(phi) * np.cos(phi),

        mass * (vx ** 2 + vy ** 2) / length * np.cos(phi)
        - mass * 9.81 * np.sin(phi) ** 2
    ])

    vx += force[0] / mass * dt
    vy += force[1] / mass * dt

    x += vx * dt
    y += vy * dt

    phi = np.arcsin(x / length)

    return x, y, phi, vx, vy

while t <= 10:
    x, y, phi, vx, vy = calc_ds(x, y, phi, vx, vy)
    xa.append(x)
    ya.append(y)

    t += dt



fig, ax = plt.subplots()

ax.set_aspect("equal")
ax.set_xlim(-length - 0.5, length + 0.5)
ax.set_ylim(-0.5, length +1)
ax.grid(True)

pivot, = ax.plot([0], [length], "ko")

rope, = ax.plot([], [], "k-")

bob, = ax.plot([], [], "ro", markersize=10)

def init():
    rope.set_data([], [])
    bob.set_data([], [])
    return rope, bob

def update(i):
    rope.set_data([0, xa[i]], [length, ya[i]])

    bob.set_data([xa[i]], [ya[i]])

    return rope, bob

ani = FuncAnimation(
    fig,
    update,
    frames=len(xa),
    init_func=init,
    interval=dt*1000,
    blit=True
)
plt.show()
