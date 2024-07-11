import matplotlib.pyplot as plt

import matplotlib

matplotlib.use('TkAgg')

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Назначение заголовка диаграмм и меток осей
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=24)
ax.set_ylabel('Square of Value', fontsize=24)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона для каждой оси
ax.axis([0, 6000, 0, 110000000000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()