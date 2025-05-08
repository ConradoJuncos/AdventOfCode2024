import time
from itertools import product

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

def operate_with_concatenation(numbers, chars):
    result = int(numbers[0])
    for i in range(len(chars)):
        if chars[i] == 'a':
            result = int(result) * int(numbers[i+1])
        if chars[i] == 'b':
            result = int(result) + int(numbers[i+1])
        if chars[i] == 'c':
            result = str(result) + str(numbers[i+1])
    return int(result)


def get_list_of_results(numbers, chars): 
    numbers = numbers.split(" ")
    results = []
    for i in chars:
        results.append(operate_with_concatenation(numbers, i))
    return results

def get_chars(length):
    return [''.join(p) for p in product('abc', repeat=length)]

def result_is_obtainable_with_concatenation(result, numbers):
    # Creates an array of strings with every ordered combination of "a b c" characters
    length = 0
    for i in numbers:
        if i == " ":
            length += 1
    chars = get_chars(length)
    list_of_results = get_list_of_results(numbers, chars)
    for i in list_of_results:
        if int(result) == i:
            return int(result)
    return 0

def main():
    filepath = "./input.txt"
    equations = get_equations(filepath)
    # Results: [int, int, ...]
    # Numbers: [[int, int, ...], [int, int, ...], ...]
    results, numbers = [], []
    for i in equations:
        an, op = i.split(",")
        results.append(an)
        numbers.append(op)

    # Part 1
    start1 = time.time()
    
    valid_sum = 0
    for i in range(len(results)):
        valid_sum += result_is_obtainable(results[i], numbers[i])
    print(valid_sum)

    time1 = time.time() - start1
    print(f"Part 1 executed in {time1:.4f} seconds")

    # Part 2
    start2 = time.time()

    valid_sum_2 = 0
    for i in range(len(results)):
        valid_sum_2 += result_is_obtainable_with_concatenation(results[i], numbers[i])
    print(valid_sum_2)

    time2 = time.time() - start2
    print(f"Part 2 executed in {time2:.4f} seconds")

if __name__ == "__main__":
    main()
