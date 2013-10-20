# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Choosing the Live Feed

# <markdowncell>

# We first need to choose a relevant feed for study. If we wanted to choose another feed, we could just copy and paste a different URL into the url variable. 

# <codecell>

import urllib
import json
import pandas as pd
from pprint import pprint

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson'

# <markdowncell>

# We use the code below to look at the structure of the JSON data. 

# <codecell>

d = json.loads(urllib.urlopen(url).read())

data = pd.DataFrame(d.items())

data

# <markdowncell>

# We can see that the data is stored in a dictionary.

# <codecell>

data[1][1][0]

# <markdowncell>

# We can thus write code to extract the desired values from the dictionary.

# <codecell>

earthquakes = []

for categories in data[1][1]:
    
    src = categories['properties']['net']
    code = categories['properties']['code']
    time = categories['properties']['time']
    longitude = categories['geometry']['coordinates'][0]
    latitude = categories['geometry']['coordinates'][1]
    magnitude = categories['properties']['mag']
    depth = categories['geometry']['coordinates'][2]
    nst = categories['properties']['nst']
    place = categories['properties']['place']
    earthquake_columns = [src, code, time, longitude, latitude, magnitude, depth, nst, place]
    
    earthquakes.append(earthquake_columns)

#earthquakes

df = pd.DataFrame(np.array(earthquakes),
 columns = ['Src','Code','Time','Latitude','Longitude','Magnitude','Depth','Nst','Place'])
df[0:20]

# <markdowncell>

# This should print out the unique places with earthquakes

# <codecell>

set(df.Src)

# <markdowncell>

# Let's look at California

# <codecell>

california = df[df.Src=='ci']
california[0:5]
print california.Longitude[0:5]
california.Latitude[0:5]

# <codecell>

from mpl_toolkits.basemap import Basemap

def plot_quakes(quakes):
    m = Basemap(llcrnrlon=-124.960938,llcrnrlat=41.956070,
                urcrnrlon=-114.062500,urcrnrlat=32.236792,
                resolution='l',area_thresh=1000.,projection='merc',
                lat_0=37.147894,lon_0=-119.599609)
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='coral',lake_color='blue')
    m.drawmapboundary(fill_color='aqua')
    x, y = m(quakes.Lon, quakes.Lat)
    m.plot(x, y, 'k.')
    return m

plot_quakes(california)

# <codecell>


# <codecell>


