import matplotlib.pyplot as plt
from particula import Particula

# Configurações iniciais
x0, y0 = 0, 0
vx0, vy0 = 10, 10
massa = 1
g = 9.8
dt = 0.01
tempo_total = 5


p = Particula(x0, y0, vx0, vy0, massa)

# Listas para armazenar os dados
tempos = []
ys = []

# Simulação
t = 0
while t <= tempo_total and p.y >= 0:
    fx = 0
    fy = -massa * g
    x, y, vx, vy = p.newton(fx, fy, dt)

    tempos.append(t)
    ys.append(y)

    t += dt


plt.plot(tempos, ys, label="y(t)")
plt.xlabel("Tempo (s)")
plt.ylabel("Altura (m)")
plt.title("Trajetória da partícula")
plt.grid(True)
plt.legend()
plt.show()

