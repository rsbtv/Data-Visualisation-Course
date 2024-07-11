import json
import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Изучение структуры данных
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    lats_indx = header_row.index('latitude')
    lons_indx = header_row.index('longitude')
    date_indx = header_row.index('acq_date')

    lats, lons, dates = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[5], "%Y-%m-%d")
            lat = float(row[lats_indx])
            lon = float(row[lons_indx])
        except IndexError:
            print(f"Missing data for {row}")
        else:
            dates.append(current_date)
            lats.append(lat)
            lons.append(lon)

#
# # Нанесение данных на карту
# # data = [Scattergeo(lon=lons, lat=lats)]
# # другой вариант
#
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': dates,
    #   'marker': {
    # 'size': [5 * mag for mag in mags],
    # 'color': mags,
    # 'colorscale': 'Viridis',
    # 'reversescale': True,
    # 'colorbar': {'title': 'Magnitude'}
    #   }
}]
title = 'World fires for 7 days'
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires_7days.html')
