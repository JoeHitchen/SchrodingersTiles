from .tile_types import Connector
from .image_tiles import ImageTileSet


conn_black = Connector('B')
conn_white = Connector('W')


class Circles(ImageTileSet):

    images_size = (32, 32)
    boundary_connector = conn_black

    class TileTypes(ImageTileSet.TileTypes):
        BLACK_FULL = 'BF'
        BLACK_HALF = 'BH'
        BLACK_QUARTER = 'BQ'
        BLACK_TIMER = 'BT'
        WHITE_FULL = 'WF'
        WHITE_HALF = 'WH'
        WHITE_QUARTER = 'WQ'
        WHITE_TIMER = 'WT'


    tile_prototypes = {
        TileTypes.BLACK_FULL: {
            'connectors': (conn_black, conn_black, conn_black, conn_black),
            'rotations': 1,
            'image_path': 'tile_sets/images/circles_black_full.png',
        },
        TileTypes.BLACK_HALF: {
            'connectors': (conn_white, conn_black, conn_white, conn_white),
            'rotations': 4,
            'image_path': 'tile_sets/images/circles_black_half.png',
        },
        TileTypes.BLACK_QUARTER: {
            'connectors': (conn_white, conn_black, conn_black, conn_white),
            'rotations': 4,
            'image_path': 'tile_sets/images/circles_black_quarter.png',
        },
        TileTypes.BLACK_TIMER: {
            'connectors': (conn_white, conn_black, conn_white, conn_black),
            'rotations': 2,
            'image_path': 'tile_sets/images/circles_black_timer.png',
        },
        TileTypes.WHITE_FULL: {
            'connectors': (conn_white, conn_white, conn_white, conn_white),
            'rotations': 1,
            'image_path': 'tile_sets/images/circles_white_full.png',
        },
        TileTypes.WHITE_HALF: {
            'connectors': (conn_black, conn_white, conn_black, conn_black),
            'rotations': 4,
            'image_path': 'tile_sets/images/circles_white_half.png',
        },
        TileTypes.WHITE_QUARTER: {
            'connectors': (conn_black, conn_white, conn_white, conn_black),
            'rotations': 4,
            'image_path': 'tile_sets/images/circles_white_quarter.png',
        },
        TileTypes.WHITE_TIMER: {
            'connectors': (conn_black, conn_white, conn_black, conn_white),
            'rotations': 2,
            'image_path': 'tile_sets/images/circles_white_timer.png',
        },
    }

