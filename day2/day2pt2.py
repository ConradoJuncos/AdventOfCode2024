def is_safe(report):
    if len(report) == 1:
        return True, -1
    increases = int(report[0]) < int(report[1])
    decreases = int(report[0]) > int(report[1])
    for i in range(len(report) - 1):
        if report[i] == report[i+1]:
            return False, i
        if not (1 <= abs(int(report[i]) - int(report[i+1])) <= 3):
            return False, i
        if increases:
            if int(report[i]) > int(report[i+1]):
                return False, i
        if decreases:
            if int(report[i]) < int(report[i+1]):
                return False, i
    return True, -1

# TEST DE QUE ESTOY SACANDO EN i E i+1

def calls_is_safe(line):
    safe, fail_index = is_safe(line)
    if safe:
        return True
    line_wo_i = []
    line_wo_iplus1 = []
    line_wo_iminus1 = []

    for i in range(len(line)):
        if i == fail_index:
            continue
        line_wo_i.append(line[i])

    for i in range(len(line)):
        if i == fail_index + 1:
            continue
        line_wo_iplus1.append(line[i])

    for i in range(len(line)):
        if i == fail_index - 1:
            continue
        line_wo_iminus1.append(line[i])

    # COULD GIVE A PROBLEM if the exception occurs at i = 0, so that line_wo_iminus1 takes out the last element of line (unintended behaviour)

    return is_safe(line_wo_i)[0] or is_safe(line_wo_iplus1)[0] or is_safe(line_wo_iminus1)[0]
    

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            safe_count = 0
            for line in file:
                if calls_is_safe(line.split()):
                    safe_count += 1
            return safe_count
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

if __name__ == "__main__":
    safe_count = read_file("day2/input.txt")
    print(f"There are {safe_count} safe reports")