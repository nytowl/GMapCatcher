## @package gmapcatcher.mapServers.yandex
# All the interaction with http://maps.yandex.ru

from gmapcatcher.mapConst import MAP_MAX_ZOOM_LEVEL, INVERTED_ZOOM


## Returns a template URL for the yandex
def layer_url_template():
    return 'http://vec0%d.maps.yandex.ru/tiles?l=map&v=2.16.0&x=%i&y=%i&z=%i'


## Returns the URL to the yandex tile
def get_url(counter, coord, layer, conf):
    if INVERTED_ZOOM :
        zoom = MAP_MAX_ZOOM_LEVEL - coord[2]
    else :
        zoom = coord[2]
    return layer_url_template() % (counter + 1,
                coord[0], coord[1], zoom)
