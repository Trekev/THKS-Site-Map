import folium
from SitelistProcessor import getsitenames,getthnkslist
import re

S = getsitenames()
T = getthnkslist()

f = open("Resources/Lat1.csv","r")
rawlist = f.read()

Lat = re.split('\s', rawlist)


f = open("Resources/Lon1.csv","r")
rawlist = f.read()

Lon = re.split('\s', rawlist)


color=[]
for item in T:
    if item == 'THKS':
        color.append('green')
    elif item == ' No data':
        color.append('red')
    else:
        color.append('blue')
print(color)
    

map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=6)
for index, item in enumerate(S):
    map_1.simple_marker([Lat[index],Lon[index]], popup=S[index]+' '+T[index],marker_color=color[index])


map_1.add_wms_layer(wms_name='radar', wms_url="http://gis.srh.noaa.gov/arcgis/rest/services/RIDGERadar/MapServer", wms_transparent=False)
map_1.save('iconTest.html')


print(S.index("Wilmington, OH"))
print(S.index("Springfield, MO"))
print(S.index("????"))


print(S.index("Wallops Island, VA"))
