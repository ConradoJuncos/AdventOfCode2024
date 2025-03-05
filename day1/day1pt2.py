def get_lists(filename):
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

def get_cant_num(num, second_list):
    count = 0
    for i in range(len(second_list)):
        if num == second_list[i]:
            count += 1
    return count

def get_similarity_score(first_list, second_list):
    score = 0
    for i in range(len(first_list)):
        num = first_list[i]
        cant_num = get_cant_num(num, second_list)
        score += int(num) * cant_num
    return score

if __name__ == "__main__":
    first_list, second_list = get_lists("day1/input.txt")

    score = get_similarity_score(first_list, second_list)
    print(f"The similarity score is: {score}")