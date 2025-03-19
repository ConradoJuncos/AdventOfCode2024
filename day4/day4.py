def count_xmas(mat):

    count = 0
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), 
                  (1, 0), (-1, 1), (0, 1), (1, 1)]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            
            if mat[i][j] == "X":

                for dx, dy in directions:
                    if 0 <= i+dx < len(mat) and 0 <= j+dy < len(mat[0]) and mat[i+dx][j+dy] == "M":
                        if 0 <= i+2*dx < len(mat) and 0 <= j+2*dy < len(mat[0]) and mat[i+2*dx][j+2*dy] == "A":
                            if 0 <= i+3*dx < len(mat) and 0 <= j+3*dy < len(mat[0]) and mat[i+3*dx][j+3*dy] == "S":
                                count += 1
    return count

def count_x_mas(mat):
    # Check within the inner square of the matrix (all values but the first
    #  and last row and column) and look for an "A", then check if diagonals
    #  correspond to "M" and "S"
    count = 0

    for a in range(len(mat) - 2):
        for b in range(len(mat[0]) - 2):
            # Offset of +1 to not check borders and there will never be an "A" 
            # surrounded by "M" "S" in the borders, and I like to use i and j for indexes
            i = a + 1
            j = b + 1

            if mat[i][j] == "A":

                if mat[i-1][j-1] == "M" and mat[i+1][j+1] == "S":
                    if mat[i+1][j-1] == "S" and mat[i-1][j+1] == "M":
                        count += 1
                    if mat[i+1][j-1] == "M" and mat[i-1][j+1] == "S":
                        count += 1
                if mat[i-1][j-1] == "S" and mat[i+1][j+1] == "M":
                    if mat[i+1][j-1] == "S" and mat[i-1][j+1] == "M":
                        count += 1
                    if mat[i+1][j-1] == "M" and mat[i-1][j+1] == "S":
                        count += 1
    return count

def get_matrix(filepath):
    with open(filepath, "r") as file:
        mat = []
        for line in file:
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            mat.append(row)
    return mat

def main():
    filepath = "day4/input.txt"
    matrix = get_matrix(filepath)
    xmas_count = count_xmas(matrix)
    x_mas_count = count_x_mas(matrix)
    print("XMAS Count:", xmas_count)
    print("X-MAS Count:", x_mas_count)

if __name__ == "__main__":
    main()