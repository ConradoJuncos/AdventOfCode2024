# Extremely unefficient, like 10 minutes to compute the final number
def get_matrix(filepath):
    with open(filepath, "r") as file:
        mat = []
        for line in file:
            ln = []
            for char in line:
                if char != '\n':
                    ln.append(char)
            mat.append(ln)
    return mat

def get_direction(direction = None):
    if direction == "n": return "e"
    if direction == "s": return "w"
    if direction == "e": return "s"
    if direction == "w": return "n"
    return "n"

def get_position(matrix):
     for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "^":
                return(i, j)

def get_obstacles(matrix):
    obstacles = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "#":
                obstacles.append((i, j))
    return obstacles


def make_movement(position, current_direction, directions):
    dx, dy = next(value for d in directions if current_direction in d for value in [d[current_direction]])
    return (position[0] + dx, position[1] + dy)

def get_visited_positions(matrix):
    count = 0
    for i in matrix:
        for j in i:
            if j == "X":
                count += 1
    return count

def is_loop(matrix):
    directions = [{'n': (-1, 0)},
                  {'s': (1, 0)},
                  {'e': (0, 1)},
                  {'w': (0, -1)}]

    current_direction = get_direction()
    current_position = get_position(matrix)
    obstacles = get_obstacles(matrix)
    visited = set()
    while True:
        x, y = current_position[0], current_position[1]
        state = (x, y, current_direction)
        if state in visited:
            return True
        visited.add(state)
        next_position = make_movement(current_position, current_direction, directions)
        if not (0 <= next_position[0] <= len(matrix[0])) or not (0 <= next_position[1] <= len(matrix)):
            return False
        if next_position in obstacles:
            current_direction = get_direction(current_direction)
        else:
            current_position = next_position

def main():
    filepath = "./input.txt"
    matrix = get_matrix(filepath)

    loop_counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == ".":
                matrix[i][j] = "#"
                if is_loop(matrix):
                    loop_counter += 1
                matrix[i][j] = "."
    print("Possible loop-generator obstacle positions:", loop_counter)
                

    """
    directions = [{'n': (-1, 0)},
                  {'s': (1, 0)},
                  {'e': (0, 1)},
                  {'w': (0, -1)}]

    current_direction = get_direction()
    current_position = get_position(matrix)
    obstacles = get_obstacles(matrix)
    
    while True:
        x, y = current_position[0], current_position[1]
        next_position = make_movement(current_position, current_direction, directions)
        if not (0 <= next_position[0] <= len(matrix[0])) or not (0 <= next_position[1] <= len(matrix)):
            break
        if next_position in obstacles:
            current_direction = get_direction(current_direction)
        else:
            current_position = next_position
        matrix[x][y] = "X"
    
    print("Visited positions:", get_visited_positions(matrix))
    """

if __name__ == "__main__":
    main()
