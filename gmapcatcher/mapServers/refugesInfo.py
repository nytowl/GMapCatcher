## @package gmapcatcher.mapServers.refugesInfo
# All the interaction with maps.refuges.info
#
# Copyright : openstreetmap.org & contributors CC-BY-SA. Contours and relief are restricted use :ASTER
#
# See http://www.refuges.info/ for deatails.
#


### Layer names
#
# relief   Only relief
# hiking_without_contours   Only the hiking paths
# hiking   Both layers combined in a JPEG


from gmapcatcher.mapConst import MAP_MAX_ZOOM_LEVEL, INVERTED_ZOOM


## Returns a template URL for the Stamen
def layer_url_template():
    return 'http://maps.refuges.info/tiles/renderer.py/%s/%i/%i/%i.png'


## Returns the URL to the Stamen tile
def get_url(counter, coord, layer, conf):
    # server = ['', 'a.', 'b.', 'c.', 'd.']
    if INVERTED_ZOOM :
        zoom = MAP_MAX_ZOOM_LEVEL - coord[2]
    else :
        zoom = coord[2]
    return layer_url_template() % (layer,
                zoom, coord[0], coord[1])
