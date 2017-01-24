## @package gmapcatcher.mapServers.cloudMade
# All the interaction with CloudMade.com

from gmapcatcher.mapConst import MAP_MAX_ZOOM_LEVEL
from gmapcatcher.mapConst import INVERTED_ZOOM


## Returns a template URL for CloudMade
def layer_url_template(API_KEY):
    return 'http://%s.tile.cloudmade.com/' + API_KEY + '/%i/%i/%i/%i/%i.png'


## Returns the URL to the CloudMade tile
def get_url(counter, coord, layer, conf):
    server = ['a', 'b', 'c']
    if INVERTED_ZOOM :
        zoom = MAP_MAX_ZOOM_LEVEL - coord[2]
    else :
        zoom = coord[2]
    zoom = MAP_MAX_ZOOM_LEVEL - coord[2]
    return layer_url_template(conf.cloudMade_API) % (server[counter % 3],
            conf.cloudMade_styleID, 256,
            zoom, coord[0], coord[1])
