## @package gmapcatcher.mapServers.nokia
# All the interaction with http://maps.nokia.com

from gmapcatcher.mapConst import MAP_MAX_ZOOM_LEVEL
from gmapcatcher.mapConst import INVERTED_ZOOM


## Returns a template URL for the Yahoo mas
def layer_url_template(layer):
    map_server_query = ["normal", "hybrid", "terrain"]
    return 'http://%i.maps.nlp.nokia.com/maptile/2.1/maptile/newest/' + \
        map_server_query[layer] + \
        '.day/%i/%i/%i/256/png8?app_id=SqE1xcSngCd3m4a1zEGb&token=r0sR1DzqDkS6sDnh902FWQ&lg=ENG'


## Returns the URL to the nokia map tile
def get_url(counter, coord, layer, conf):
    if INVERTED_ZOOM :
        zoom = MAP_MAX_ZOOM_LEVEL - coord[2]
    else :
        zoom = coord[2]
    return layer_url_template(layer) % (counter + 1, zoom, coord[0], coord[1])
