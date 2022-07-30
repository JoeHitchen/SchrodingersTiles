from typing import List, Optional
import random

import tiles

NUM_CONN = 5
GRID_SIZE = 10
GRID_CYCLIC = False


def create_1d_incrementing_tiles(num_conn: int, cyclic: bool = False) -> List[tiles.Tile]:
    """Creates a set of 1D tiles that increments through the connections and (optionally) loops."""
    
    tile_set = []
    for i in range(1, num_conn + 1):
        tile_set.append({tiles.Directions.LEFT: i, tiles.Directions.RIGHT: i})
        if i < num_conn:
            tile_set.append({tiles.Directions.LEFT: i, tiles.Directions.RIGHT: i + 1})
        elif cyclic and i > 1:
            tile_set.append({tiles.Directions.LEFT: i, tiles.Directions.RIGHT: 1})
    
    return tile_set


def tile_to_text(tile: tiles.Tile) -> str:
    return '[{}-{}]'.format(tile[tiles.Directions.LEFT], tile[tiles.Directions.RIGHT])


def render_1d_state(wave_function: List[tiles.Cell], cyclic: bool) -> None:
    
    def render_1d_tile(tile: Optional[tiles.Tile], line: int) -> str:
        left = tile[tiles.Directions.LEFT] if tile else '?'
        right = tile[tiles.Directions.RIGHT] if tile else '?'
        return {
            0: '╔══╗',
            1: '║{}{}║'.format(left, right),
            2: '╚══╝',
        }[line]
    
    # Selected tiles
    selected_tiles = [cell.tile for cell in wave_function]
    for line in range(3):
        tile_strings = [render_1d_tile(tile, line) for tile in selected_tiles]
        if cyclic:
            tile_strings = [
                '···' + tile_strings[-1][-2:],
                *tile_strings,
                tile_strings[0][:2] + '···',
            ]
        print('  ' + ' '.join(tile_strings) + '  ')
    
    print((5 * len(wave_function) + (15 if cyclic else 3)) * '=')
    
    # Cell options
    for i in range(max(len(cell.state) for cell in wave_function)):
        for line in range(3):
            tile_strings = []
            for cell in wave_function:
                tile_strings.append((
                    render_1d_tile(cell.state[i], line)
                    if i < len(cell.state) else '    '
                ))
            print((8 if cyclic else 2) * ' ' + ' '.join(tile_strings) + (8 if cyclic else 2) * ' ')


if __name__ == '__main__':
    
    tile_set = create_1d_incrementing_tiles(NUM_CONN, cyclic = GRID_CYCLIC)
    wave_function = tiles.WaveFunction([
        tiles.Cell(id = str(i + 1), state = tile_set)
        for i in range(GRID_SIZE)
    ])
    tiles.link_1d_grid(wave_function.cells, GRID_CYCLIC)
    
    print('Initial state')
    render_1d_state(wave_function.cells, cyclic = GRID_CYCLIC)
    
    while any([not cell.collapsed for cell in wave_function.cells]):
        print('')
        print('Performing random collapse...')
        cell_index = tiles.get_most_contrained_cell(wave_function.cells)
        tile = random.choice(wave_function.cells[cell_index].state)
        print('Selected {} for {}'.format(tile_to_text(tile), wave_function.cells[cell_index]))
        
        tiles.collapse(wave_function.cells, cell_index, tile)
        render_1d_state(wave_function.cells, cyclic = GRID_CYCLIC)
    
