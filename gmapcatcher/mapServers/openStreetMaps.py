## @package gmapcatcher.mapServers.openStreetMaps
# All the interaction with OpenStreetMap.org

from gmapcatcher.mapConst import MAP_MAX_ZOOM_LEVEL
from gmapcatcher.mapConst import INVERTED_ZOOM


## Returns a template URL for the openStreetMaps
def layer_url_template():
    return 'http://%s.tile.openstreetmap.org/%i/%i/%i.png'


## Returns the URL to the openStreetMaps tile
def get_url(counter, coord, layer, conf):
    server = ['a', 'b', 'c']
    if INVERTED_ZOOM :
      zoom = MAP_MAX_ZOOM_LEVEL - coord[2]
    else :
      zoom = coord[2]
    return layer_url_template() % (server[counter % 3],
                zoom, coord[0], coord[1])
