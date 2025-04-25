def get_equations(filepath):
    with open (filepath, 'r') as file:
        equations = []
        for line in file:
            equ = ""
            eq = ""
            l = line.strip().split(":")
            count = 0
            for i in l[1]:
                if count == 0:
                    count += 1
                    continue
                eq += i
            equ += l[0]
            equ += ","
            equ += eq
            equations.append(equ)
        return equations

def operate(numbers, bin, digits):
    while len(bin) < digits:
        bin = '0' + bin
    
    result = int(numbers[0])
    for i in range(len(numbers) - 1):
        if bin[i] == '1':
            result *= int(numbers[i+1])
        if bin[i] == '0':
            result += int(numbers[i+1])
    return result

def get_results(numbers):
    comb = pow(2, len(numbers) - 1)
    digits = len(numbers) - 1
    binary_number = bin(comb-1)[2:len(bin(comb))]
    results = []
    for _ in range(comb):
        results.append(operate(numbers, binary_number, digits))
        comb -= 1
        binary_number = bin(comb-1)[2:len(bin(comb))]
    return results

def result_is_obtainable(result, numbers):
    ints = []
    ints += numbers.split(" ")
    possible_results = get_results(ints)   
    if int(result) in possible_results:
        return int(result)
    return 0

def main():
    filepath = "./input.txt"
    equations = get_equations(filepath)
    results, numbers = [], []
    for i in equations:
        an, op = i.split(",")
        results.append(an)
        numbers.append(op)

    valid_sum = 0
    for i in range(len(results)):
        valid_sum += result_is_obtainable(results[i], numbers[i])
    print(valid_sum)

if __name__ == "__main__":
    main()
