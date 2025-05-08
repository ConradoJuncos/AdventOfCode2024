def get_map(filepath):
    with open (filepath, 'r') as file:
        map = []
        for line in file:
            map_line = []
            for char in line:
                if char != "\n":
                    map_line.append(char)
            map.append(map_line)
        return map

def print_map(map):
    flag = False
    for i in range(len(map)):
        if flag:
            print()
        flag = True
        for j in range(len(map[i])):
            print(map[i][j], end='')
    print()

def get_antennas_dictionaries(map):
    antennas = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != ".":
                antennas.append({"frequency": map[i][j], "i": i, "j": j, "is_antinode": False})
    return antennas

def calculate_distance(i1, j1, i2, j2):
    dx = i2 - i1
    dy = j2 - j1
    return(2*dx, 2*dy)

def calculate_distance_part2(i1, j1, i2, j2):
    dx = i2 - i1
    dy = j2 - j1
    return(dx, dy)

def set_antenna_as_antinode(antennas, i, j):
    for antenna in antennas:
        if antenna["i"] == i and antenna["j"] == j:
            antenna["is_antinode"] = True
            break
    return antennas

def get_antinodes(map, antennas):
    for antenna in antennas:
        antenna_i = antenna["i"]
        antenna_j = antenna["j"]
        
        for i in range(len(map)):
            for j in range(len(map[i])):
                if i == antenna_i and j == antenna_j:
                    continue
                if map[i][j] == antenna["frequency"]:
                    dx, dy = calculate_distance(antenna_i, antenna_j, i, j)
                    if 0 <= antenna_i + dx < len(map) and 0 <= antenna_j + dy < len(map[i]):
                        if map[antenna_i+dx][antenna_j+dy] != ".":
                            set_antenna_as_antinode(antennas, antenna_i+dx, antenna_j+dy)
                        else: 
                            map[antenna_i+dx][antenna_j+dy] = "#"

def get_antinodes_multiplied(map, antennas):
    for antenna in antennas:
        antenna_i = antenna["i"]
        antenna_j = antenna["j"]
        
        for i in range(len(map)):
            for j in range(len(map[i])):
                if i == antenna_i and j == antenna_j:
                    continue
                if map[i][j] == antenna["frequency"]:
                    dx, dy = calculate_distance_part2(antenna_i, antenna_j, i, j)
                    for k in range(15000):
                        if k == 0:
                            continue
                        if 0 <= antenna_i + (k*dx) < len(map) and 0 <= antenna_j + (k*dy) < len(map[i]):
                            if map[antenna_i+(k*dx)][antenna_j+(k*dy)] != ".":
                                set_antenna_as_antinode(antennas, antenna_i+(k*dx), antenna_j+(k*dy))
                            else: 
                                map[antenna_i+(k*dx)][antenna_j+(k*dy)] = "#"
                        else:
                            break

def count_antinodes(map, antennas):
    counter = 0
    for i in map:
        for j in i:
            if j == "#":
                counter += 1
    for antenna in antennas:
        if antenna["is_antinode"]:
            counter += 1
    return counter

def main():
    # Idea: get a set of every antenna, then go throught the dicts and for each antenna, search for the other antennas
    # calculate every possible antinode for each pair of antennas of the same name, and if inside the boundaries of the map, set the cell as "#" (if not an antenna)
    # set the antenna as "is_antinode": True if neccesary
    # Actually its not neccesary to keep the map in its correct state, as the antennas have already been mapped to the dictionaries
    map = get_map("input.txt")

    antennas = get_antennas_dictionaries(map)

    # get_antinodes(map, antennas)

    get_antinodes_multiplied(map, antennas)

    # Part 1: 341
    # Part 2: 1134
    print(count_antinodes(map, antennas))

if __name__ == "__main__":
    main()
