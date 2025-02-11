import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Константы
q = 1  # Заряд в единицах СГС

# Определение сетки
x = np.arange(-5, 5.2, 0.2)
y = np.arange(-5, 5.2, 0.2)
z = np.arange(-5, 5.2, 0.2)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Расчет потенциала
R = np.sqrt(X**2 + Y**2 + Z**2)
V = np.where(R != 0, q / R, 0)  # Избегаем деления на ноль

# Расчет компонентов электрического поля
Ex, Ey, Ez = np.gradient(-V, 0.2, axis=(0, 1, 2))

# Визуализация силовых линий
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Выборка точек для построения векторного поля
skip = (slice(None, None, 5), slice(None, None, 5), slice(None, None, 5))
ax.quiver(X[skip], Y[skip], Z[skip], Ex[skip], Ey[skip], Ez[skip], length=0.5, normalize=True)

ax.set_xlabel('X, cm')
ax.set_ylabel('Y, cm')
ax.set_zlabel('Z, cm')
ax.set_title('Силовые линии электрического поля')
plt.show()

# Визуализация эквипотенциальных поверхностей в трех проекциях
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Средние индексы по осям
z_index = len(z) // 2  # Для XY
y_index = len(y) // 2  # Для XZ
x_index = len(x) // 2  # Для YZ

# YZ плоскость
Y_slice, Z_slice, V_slice = Y[x_index, :, :], Z[x_index, :, :], V[x_index, :, :]
contour3 = axes[2].contour(Y_slice, Z_slice, V_slice, levels=[0.2, 0.5, 0.8, 1.1, 1.4], colors='black')
axes[2].set_xlabel('Y, cm')
axes[2].set_ylabel('Z, cm')
axes[2].set_title('Эквипотенциалы в плоскости X=0')

# XZ плоскость
X_slice, Z_slice, V_slice = X[:, y_index, :], Z[:, y_index, :], V[:, y_index, :]
contour2 = axes[1].contour(X_slice, Z_slice, V_slice, levels=[0.2, 0.5, 0.8, 1.1, 1.4], colors='black')
axes[1].set_xlabel('X, cm')
axes[1].set_ylabel('Z, cm')
axes[1].set_title('Эквипотенциалы в плоскости Y=0')

# XY плоскость
X_slice, Y_slice, V_slice = X[:, :, z_index], Y[:, :, z_index], V[:, :, z_index]
contour1 = axes[0].contour(X_slice, Y_slice, V_slice, levels=[0.2, 0.5, 0.8, 1.1, 1.4], colors='black')
axes[0].set_xlabel('X, cm')
axes[0].set_ylabel('Y, cm')
axes[0].set_title('Эквипотенциалы в плоскости Z=0')

plt.tight_layout()
plt.show()