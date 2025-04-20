"""
Go through every update
For each update, get the relevant rules
For each page of the update, make a dictionary
Key = page | Value = [] of pages that go after that page
12:[13,81,3] -> 12 goes before 13, 81 and 3
Go through every rule X|Y and add Y to the [] of the dictionary of key X
"""

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

def sum_of_middle_numbers_from_unordered_updates(updates_list):
    sum = 0
    for update in updates_list:
        sum += middle_number(update)
    return sum


def order_updates(rules, updates):
    ordered = []
    for update in updates:
        graph = {page: [] for page in update}
        counter = {page: 0 for page in update}
        relevant_rules = []
        relevant_rules += [rule for rule in rules if rule[0] in update and rule[1] in update]
    
        for i in relevant_rules:
            x = i[0]
            y = i[1]
            graph[x].append(y)
            counter[x] = len(graph[x])
        upd = []

        for key, value in counter.items():
            max_value = max(counter.values())
            max_key = -1
            for k, v in counter.items():
                if v == max_value:
                    max_key = k
                    break
            upd.append(max_key)
            counter[max_key] = -1
        ordered.append(tuple(upd))
        upd = []
    return ordered

def main():
    filepath = "day5/input.txt"
    rules, updates = get_rules_and_updates(filepath)
    rules_list = get_rules_list(rules)
    updates_list = get_updates_list(updates)

    # sum = sum_of_middle_numbers_from_ordered_updates(rules_list, updates_list)
    # print("Sum:", sum)

    # pt 2: order the unordered updates and calculate the sum of the middle numbers

    unordered_updates = [update for update in updates_list if not is_ordered(update, rules_list)]
    ordered_unordered_updates = order_updates(rules_list, unordered_updates)
    # print(ordered_unordered_updates)
    sum = sum_of_middle_numbers_from_unordered_updates(ordered_unordered_updates)
    print("Sum of middle numbers of previously unordered updates:", sum)

if __name__ == "__main__":
    main()
