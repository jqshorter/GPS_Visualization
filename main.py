from gps_csv_class import GPSVis
from gps_list_class import GPSVisList
import time

vis = GPSVisList(map_path='map.png',  # Path to map downloaded from the OSM.
                 points=(34.06076, -117.82309, 34.05837, -117.82047))  # Two coordinates of the map (upper left, lower right)

while 1:
    vis.create_image(color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks.
    vis.plot_map(output='save')
    time.sleep(1000)
