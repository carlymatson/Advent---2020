file = open("day20input2.text", 'r')
file_lines = file.readlines()

import time
start_clock = time.time()

# Parse tiles into dictionary.
ids = []
side_length = 0
tile_by_id = {}
end_of_file =  False
while not end_of_file:
    line = file_lines.pop(0).strip()
    tile_id = int(line[5:9])
    line = file_lines.pop(0).strip()
    side_length = len(line)
    tile = []
    while line != "":
        tile.append(line)
        try:
            line = file_lines.pop(0).strip()
        except:
            end_of_file = True
            break
    tile_by_id[tile_id] = tile
    ids.append(tile_id)

### --- Functions for Part 2 --- ###

# Rotate a tiling counterclockwise by 90 degrees.
def rotate(tiling):
    length = len(tiling)
    width = 0
    for row in tiling:
        if len(row) > width:
            width = len(row)
    tiling_z_fill = [row + "z"*(width - len(row)) for row in tiling]
    new_tiling = ["".join([tiling_z_fill[j][width-1-i] for j in range(length)]) for i in range(width)]
    new_tiling = [row.rstrip('z') for row in new_tiling]
    return new_tiling

# Flip a tiling along the i=j diagonal.
def flip(tiling):
    length = len(tiling)
    width = len(tiling[0])
    new_tiling = ["".join([tiling[j][i] for j in range(length)]) for i in range(width)]
    return new_tiling

# Display a tile or the full picture.
def print_pic(tiling):
    print "-"*20
    for row in tiling:
        print row
    print "-"*20
    return True

# See if the tile with given ID can be added to any of the rightmost edges.
def try_to_attach_tile(tile_id):
    tile = tile_by_id[tile_id]
    for y in range(len(picture)/side_length):
        width = len(picture[y*side_length])
        right_edge = "".join([picture[y*side_length + j][width-1] for j in range(side_length)])
        flips = 0
        while flips < 2:
            for turn in range(4):
                left_edge = "".join(tile[j][0] for j in range(side_length))
                if right_edge == left_edge:
                    for j in range(side_length):
                        picture[y*side_length + j] = picture[y*side_length + j] + tile[j]
                    loose_tiles.remove(tile_id)
                    return True
                tile = rotate(tile)
            tile = flip(tile)
            flips += 1
    return False

### --- Part 1 --- ###
# I got the corner IDs by counting which tiles had only 2 edges with matches.
# This assembles the picture, but doesn't save the IDs.

picture = list(tile_by_id[ids[0]])

loose_tiles = list(ids)
loose_tiles.remove(ids[0])

# Try to stick loose tiles onto the right side of the picture.
while len(loose_tiles) > 0:
    found_match = False
    for id in loose_tiles:
        if try_to_attach_tile(id):
            print_pic(picture) # Optional, but fun to watch. Use a large terminal window.
            found_match = True
            break
    if not found_match:
        picture = rotate(picture)

### --- Functions for Part 2 --- ###

# Get rid of tile borders in final picture.
def trim(tiling):
    new_tiling = []
    for i in range(len(tiling)/side_length):
        new_tiling.extend(tiling[side_length*i+1: side_length*i+side_length-1])
    for i in range(len(new_tiling)):
        row = new_tiling[i]
        width = len(row)
        new_row = ""
        for j in range(width/side_length):
            new_row += row[side_length*j + 1 : side_length*j + side_length-1]
        new_tiling[i] = new_row
    return new_tiling

# Get coordinates of all pixels that equal '#'.
def get_poundsign_coords(tiling):
    xy_tuples = []
    for i in range(len(tiling)):
        row = tiling[i]
        for j in range(len(row)):
            if tiling[i][j] == '#':
                xy_tuples.append((i,j))
    return xy_tuples

# Return set of coordinates (if any) of #'s that are part of a monster based at (i,j).
def is_monster(row_num, col_num):
    global picture
    mon_set = set()
    checks = [picture[row_num + pt[0]][col_num+pt[1]] == '#' for pt in monster_coords]
    if all(checks):
        mon_set = set([(row_num + pt[0], col_num + pt[1]) for pt in monster_coords])
    return mon_set

# Go through entire picture, possibly flipping and rotating, and look for monsters.
def scan_for_monsters():
    global picture
    global monster
    pic_length = len(picture)
    pic_width = len(picture[0])
    mon_length = len(monster)
    mon_width = len(monster[0])
    xy_set = set()
    flips = 0
    while flips < 2:
        for turn in range(4):
            for i in range(pic_length + 1 - 3):
                for j in range(pic_width + 1 - 20):
                    xy_set = xy_set.union(is_monster(i,j))
            if len(xy_set) > 0:
                return xy_set
            print "Looking for monsters: Rotated the picture"
            picture = rotate(picture)
        print "Looking for monsters: Flipped the picture"
        picture = flip(picture)
        flips += 1
    return xy_set

### --- Part 2 --- ###

### Trim the borders from the tiles in the picture.
picture = trim(picture)
print "Trimmed borders from picture."

### Read in the sea monster from a text file.
monster_file = open("day20seamonster.text", 'r') # This didn't copy and paste correctly due to the spaces.
monster_lines = monster_file.readlines()
monster = [row.rstrip('\n') for row in monster_lines] # Do not strip spaces.
monster_coords = get_poundsign_coords(monster) # Find relative positions of monster parts.
monster_locations = scan_for_monsters() # Find all locations that have sea monsters.

count_non_monsters = len(set(get_poundsign_coords(picture)) - monster_locations)

print "Number of #-tiles not in a sea monster: %d"%(count_non_monsters)

end_clock = time.time()
print "Time to run: %d seconds"%(end_clock - start_clock)
