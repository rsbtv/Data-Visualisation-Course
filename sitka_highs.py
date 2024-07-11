import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/3051852.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs_indx = header_row.index("TMAX")
    lows_indx = header_row.index("TMIN")
    prcps_indx = header_row.index("PRCP")
    name_indx = header_row.index("NAME")

    # Чтение дат и максимальных температур из файла
    dates, highs, lows, prcps = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        name = row[name_indx]
        try:
            high = float(row[highs_indx])
            low = float(row[lows_indx])
            prcp = float(row[prcps_indx])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            prcps.append(prcp)

# нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates, prcps, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# форматирование диаграммы
plt.title(f"Daily high and low temperatures - {name}\n2018", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
ax.axis([dates[0], dates[-1], 0, 140])

plt.show()
