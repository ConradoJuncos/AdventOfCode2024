def get_rules_and_updates(filepath):
    rules = ""
    updates = ""
    end_of_rules = False
    with open(filepath, "r") as file:
        for line in file:
            if line != "\n" and not end_of_rules:
                rules += line
            # keeps entering first if until line is "\n", which makes the program only enter second if
            else:
                end_of_rules = True
            if line != "\n" and end_of_rules:
                updates += line
    return rules, updates

def get_rules_list(rules):
    line = ""
    rules_list = []
    for i in rules:
        if i != "\n":
            line += i
        else:
            left = line[0:2]
            right = line[3:5]
            rules_list.append(((int(left)), int((right))))
            line = ""
    return rules_list

def get_updates_list(updates):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    updates_list = []
    single_update = []
    single_number = ''
    for i in updates:
        if i in nums:
            single_number += i
        elif i == ',':
            single_update.append(int(single_number))
            single_number = ''
        elif i == "\n":
            if single_number:
                single_update.append(int(single_number))
                single_number = ''
            if single_update:
                updates_list.append(single_update)
                single_update = []
    if single_number:
        single_update.append(int(single_number))
    if single_update:
        updates_list.append(single_update)
    return updates_list

def middle_number(update):
    mid = int(len(update) / 2 - 0.5)
    return update[mid]

def is_ordered(update, rules):
    relevant_rules = []
    relevant_rules += [rule for rule in rules if rule[0] in update or rule[1] in update]
    for i in range(len(update) - 1):
        pair = (update[i], update[i+1])
        for rule in relevant_rules:
            unordered_rule = (pair[1], pair[0])
            if rule == unordered_rule:
                return False
    return True

def sum_of_middle_numbers_from_ordered_updates(rules_list, updates_list):
    sum = 0

    for update in updates_list:
        if is_ordered(update, rules_list):
            sum += middle_number(update)

    return sum


def main():
    filepath = "day5/input.txt"
    rules, updates = get_rules_and_updates(filepath)
    rules_list = get_rules_list(rules)
    updates_list = get_updates_list(updates)

    sum = sum_of_middle_numbers_from_ordered_updates(rules_list, updates_list)

    print("Sum:", sum)

if __name__ == "__main__":
    main()

'''
Agarrar un subset de las reglas que afectan a las paginas de la update actual
Para cada X Y, verificar si una update dice que sea Y|X
else pass 
'''