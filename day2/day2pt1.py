def get_reports(filepath):
    with open(filepath, 'r') as file:
        reports = []
        for line in file:
            reports.append(line.split())
    return reports

def is_safe(report):
    if len(report) == 1:
        return True
    increases = report[0] < report[1]
    decreases = report[0] > report[1]
    for i in range(len(report) - 1):
        if report[i] == report[i+1]:
            return False
        if not (1 <= abs(int(report[i]) - int(report[i+1])) <= 3):
            return False
        if increases:
            if report[i] > report[i+1]:
                return False
        if decreases:
            if report[i] < report[i+1]:
                return False
    return True

def main():
    filepath = "day2/input.txt"
    reports = get_reports(filepath)
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
    print(f"There are {safe_reports} safe reports")

if __name__ == "__main__":
    main()