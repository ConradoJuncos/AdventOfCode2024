def read_file(filename):
    try:
        with open(filename, 'r') as file:
            first_list = []
            second_list = []
            for line in file:
                first_list.append(line.split()[0])
                second_list.append(line.split()[1])
        return first_list, second_list
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# def sum(previous_sum, i, first_list, second_list):
#     return previous_sum + sum(abs(int(first_list[i]) - int(second_list[i])), i, first_list, second_list)

def get_distance(first_list, second_list):
    distances = []
    for i in range(len(first_list)):
        distances.append(abs(int(first_list[i]) - int(second_list[i])))
    return sum(distances)

if __name__ == "__main__":
    first_list, second_list = read_file("day1/input.txt")
    sorted_first_list = sorted(first_list)
    sorted_second_list = sorted(second_list)

    sum = get_distance(sorted_first_list, sorted_second_list)
    print(f"The sum of the distances between the two sorted lists is: {sum}")    
