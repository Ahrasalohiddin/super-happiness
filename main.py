import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np

# Настройка карты
fig, ax = plt.subplots(figsize=(10, 5), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

# Заливка континентов и океанов
ax.add_feature(cartopy.feature.LAND, edgecolor='black')
ax.add_feature(cartopy.feature.OCEAN, edgecolor='black')

# Добавление границ
ax.gridlines(draw_labels=True)

# Функция для отображения маркеров с выбором цвета
def plot_markers(locations, colors):
    for (lat, lon), color in zip(locations, colors):
        ax.plot(lon, lat, 'o', color=color, markersize=8, transform=ccrs.PlateCarree())

# Пример данных для маркеров
locations = [(-34.6037, -58.3816), (40.7128, -74.0060), (51.5074, -0.1278)]
colors = ['red', 'blue', 'green']  # Цвета маркеров

plot_markers(locations, colors)

plt.title('Карточка с маркерами')
plt.show()
