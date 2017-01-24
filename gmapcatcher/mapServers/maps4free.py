## @package gmapcatcher.mapServers.WorldVFR
# All the interaction with skyvector.net/tiles/301

from gmapcatcher.mapConst import MAP_MAX_ZOOM_LEVEL, LAYER_TER, LAYER_HYB, INVERTED_ZOOM

max_zoom = 15
min_zoom = 6
hybrid_background = [LAYER_TER, None]

## Returns a template URL for the WorldVFR
def layer_url_template(layer):
    if layer == LAYER_TER:            
        return 'http://www.maps-for-free.com/layer/relief/z%i/row%i/%i_%i-%i.jpg'
    elif layer == LAYER_HYB:
        return 'http://www.maps-for-free.com/layer/water/z%i/row%i/%i_%i-%i.gif'


## Returns the URL to the WorldVFR tile
def get_url(counter, coord, layer, conf):
    if INVERTED_ZOOM :
        zoom = MAP_MAX_ZOOM_LEVEL-coord[2]
    else :
        zoom = coord[2]
    return layer_url_template(layer) % (zoom, coord[1], zoom, coord[0], coord[1])
