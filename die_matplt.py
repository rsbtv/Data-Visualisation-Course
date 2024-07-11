import matplotlib.pyplot as plt
from die import Die
import matplotlib

matplotlib.use('TkAgg')

die_1 = Die()
die_2 = Die()
results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]
max_result = die_1.num_sides + die_2.num_sides
# x_values = list(range(2, max_result+1))
x_values = [x for x in range(2, max_result+1)]
frequencies = [results.count(value) for value in range(2, max_result+1)]
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(2, max_result+1)
ax.bar(x_values, frequencies, width=1, edgecolor="white", linewidth=0.7)
plt.show()