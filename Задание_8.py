import numpy as np
import matplotlib.pyplot as plt

R = 10
L = 0.01
C = 100e-6
U = 2000
omega = np.linspace(10, 5000, 500)

# Задание 1: Последовательное соединение
Z_series = R + 1j * omega * L + 1 / (1j * omega * C)
I_series = U / np.abs(Z_series)  # Ток
P_series = R * I_series**2       # Активная мощность
Q_series = I_series**2 * (np.abs(omega * L) - np.abs(1 / (omega * C)))  # Реактивная мощность

# Построение графиков для последовательного соединения
plt.figure(figsize=(18, 12))

# Зависимость тока от частоты
plt.subplot(3, 1, 1)
plt.plot(omega, I_series, label="Ток I(ω)", color="blue", linewidth=1.5)
plt.xlabel("ω (рад/с)")
plt.ylabel("I (А)")

plt.title("Зависимость тока от частоты (последовательное соединение)")
plt.legend()
plt.grid(True)

# Зависимость активной мощности от частоты
plt.subplot(3, 1, 2)
plt.plot(omega, P_series, label="Активная мощность P(ω)", color="orange", linewidth=1.5)
plt.xlabel("ω (рад/с)")
plt.ylabel("P (Вт)")

plt.title("Зависимость активной мощности от частоты")
plt.legend()
plt.grid(True)

# Зависимость реактивной мощности от частоты
plt.subplot(3, 1, 3)
plt.plot(omega, Q_series, label="Реактивная мощность Q(ω)", color="green", linewidth=1.5)
plt.xlabel("ω (рад/с)")
plt.ylabel("Q (ВАр)")
plt.title("Зависимость реактивной мощности от частоты")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

R = 10
L = 0.01
C = 100e-6
U = 2000
omega = np.linspace(10, 5000, 500)

# Задание 2: Параллельное соединение
Z_parallel = 1 / (1 / (1j * omega * L) + 1j * omega * C + 1 / R)
I_parallel = U / np.abs(Z_parallel)  # Ток
P_parallel = U**2 / R                # Активная мощность
Q_parallel = U**2 * (1 / np.abs(omega * L) - np.abs(1 / (omega * C)))  # Реактивная мощность

# Построение графиков для параллельного соединения
plt.figure(figsize=(18, 12))

# Зависимость тока от частоты
plt.subplot(3, 1, 1)
plt.plot(omega, I_parallel, label="Ток I(ω)", color="blue", linewidth=1.5)
plt.xlabel("ω (рад/с)")
plt.ylabel("I (А)")
plt.title("Зависимость тока от частоты (параллельное соединение)")
plt.legend()
plt.grid(True)

# Зависимость активной мощности от частоты
plt.subplot(3, 1, 2)
plt.plot(omega, np.full_like(omega, P_parallel), label="Активная мощность P(ω)", color="orange", linewidth=1.5)
plt.xlabel("ω (рад/с)")
plt.ylabel("P (Вт)")
plt.title("Зависимость активной мощности от частоты")
plt.legend()
plt.grid(True)

# Зависимость реактивной мощности от частоты
plt.subplot(3, 1, 3)
plt.plot(omega, Q_parallel, label="Реактивная мощность Q(ω)", color="green", linewidth=1.5)
plt.xlabel("ω (рад/с)")
plt.ylabel("Q (ВАр)")
plt.title("Зависимость реактивной мощности от частоты")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

