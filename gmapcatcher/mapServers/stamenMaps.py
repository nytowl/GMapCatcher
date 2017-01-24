## @package gmapcatcher.mapServers.stamenMaps
# All the interaction with Stamen.com
#
# Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under CC BY SA
#
# See http://maps.stamen.com/ for deatails.
#

from gmapcatcher.mapConst import MAP_MAX_ZOOM_LEVEL, INVERTED_ZOOM


## Returns a template URL for the Stamen
def layer_url_template():
    return 'http://%s.tile.stamen.com/%s/%i/%i/%i.png'


## Returns the URL to the Stamen tile
def get_url(counter, coord, layer, conf):
    server = ['a', 'b', 'c', 'd']
    if INVERTED_ZOOM :
        zoom = MAP_MAX_ZOOM_LEVEL - coord[2]
    else :
        zoom = coord[2]
    stamen_layers = ['watercolor', 'toner', 'terrain']
    return layer_url_template() % (server[counter % 5], stamen_layers[layer],
                zoom, coord[0], coord[1])
