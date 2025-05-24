def get_compact_disk_map_from_file(filepath: str) -> str:
    with open (filepath, 'r') as file:
        return file.readline()

def get_disk_map_from_compacted(compact_disk_map: str) -> list:
    full_map = []
    next_file_id = 0
    is_reading_file = True
    for digit in compact_disk_map:
        if is_reading_file:
            for _ in range(int(digit)):
                full_map.append(str(next_file_id))
            next_file_id += 1
        else:
            for _ in range(int(digit)):
                full_map.append(".")
        is_reading_file = not is_reading_file
    return full_map

def get_next_space_position(full_disk_map: list) -> int|None:
    for i in range(len(full_disk_map)):
        if full_disk_map[i] == ".":
            return i

def order_full_disk_map(full_disk_map: list) -> None:
    # Returns nothing, modifies the list itself
    for i in range(len(full_disk_map)):
        reverse_array_digit = full_disk_map[len(full_disk_map) - i - 1]
        if reverse_array_digit != ".":
            temp = reverse_array_digit
            next_space_position = get_next_space_position(full_disk_map)
            if (len(full_disk_map) - i) == next_space_position:
                break
            full_disk_map[len(full_disk_map) - i - 1] = "."
            full_disk_map[next_space_position] = temp

def filesystem_checksum(map: list) -> int:
    result = 0
    for i in range(len(map)):
        if map[i] != ".":
            result += int(map[i]) * i
    return result

def main():
    filepath = "input.txt"
    compact_disk_map = get_compact_disk_map_from_file(filepath)

    full_disk_map = get_disk_map_from_compacted(compact_disk_map)
    
    order_full_disk_map(full_disk_map)
    # WRITE THE EXPECTED TYPES

    print("System Checksum:", filesystem_checksum(full_disk_map))

if __name__ == "__main__":
    main()

