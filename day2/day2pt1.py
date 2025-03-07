def get_reports(filepath):
    with open(filepath, 'r') as file:
        reports = []
        for line in file:
            reports.append(line.split())
    return reports

def only_increases_or_decreases(report):
    if len(report) == 1:
        return True
    increases = report[0] < report[1]
    decreases = report[0] > report[1]
    for i in range(len(report) - 1):
        if report[i] == report[i+1]:
            return False
        if increases:
            if report[i] > report[i+1]:
                return False
        if decreases:
            if report[i] < report[i+1]:
                return False
    return True

def changes_by_one_to_three(report):
    if len(report) == 1:
        return True
    for i in range(len(report) - 1):
        if not (1 <= abs(int(report[i]) - int(report[i+1])) <= 3):
            return False
    return True

def is_safe(report):
    # Use only one for. Check for increasing or decreasing AND steps in the same cycle
    return only_increases_or_decreases(report) and changes_by_one_to_three(report)

def main():
    filepath = "day2/test.txt"
    reports = get_reports(filepath)
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
    print(f"There are {safe_reports} safe reports")

if __name__ == "__main__":
    main()