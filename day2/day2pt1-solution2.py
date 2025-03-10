def is_safe(line):
    if len(line) == 1:
        return True
    increases = decreases = True
    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            return False
        if not ( 1 <= abs(int(line[i]) - int(line[i+1])) <= 3 ):
            return False
        if int(line[i]) < int(line[i+1]):
            decreases = False
        else:
            increases = False
    return increases or decreases

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            safe_count = 0
            for line in file:
                if is_safe(line.split()):
                    safe_count += 1
            return safe_count
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

if __name__ == "__main__":
    safe_count = read_file("day2/input.txt")
    print(f"There are {safe_count} safe reports")