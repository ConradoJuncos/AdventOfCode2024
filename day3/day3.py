nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def mul(x, y):
    return x * y

def get_sum(filepath):
    with open(filepath, 'r') as file:
        do = True
        sum = 0
        for line in file:
            for i in range(len(line)):
                if line[i:i+7] == "don't()":
                    do = False
                if line[i:i+4] == "do()":
                    do = True
                if line[i:i+4] == "mul(" and do:
                    num1 = ""
                    j = i + 4
                    while j < len(line) and line[j] in nums:
                        num1 += line[j]
                        j += 1
                    if 1 <= len(num1) <= 3 and line[j] == ",":
                        j += 1
                        num2 = ""
                        while j < len(line) and line[j] in nums:
                            num2 += line[j]
                            j += 1
                        if 1 <= len(num2) <= 3 and line[j] == ")":
                            sum += mul(int(num1), int(num2))
        return sum

if __name__ == "__main__":
    filepath = "day3/input.txt"
    sum = get_sum(filepath)
    print(sum)