def get_lookup_table(mapping: str) -> list[tuple[range, int]]:

        table = []
        for line in mapping.splitlines()[1:]:
            dest_start, src_start, range_ = [int(x) for x in line.split()]

            table.append((
                range(src_start, src_start + range_),
                dest_start - src_start,
            ))
        return table

try: 
    with open("./Day5/input.txt") as f:
        file_content = f.read()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
   
    curr_data, *maps = file_content.split('\n\n')
    curr_data = [int(item) for item in curr_data.removeprefix('seeds: ').split()]
    for mapping in maps:
        table = get_lookup_table(mapping)

        for i, item in enumerate(curr_data):
            curr_data[i] = ([
                item + diff for map_range, diff in table if item in map_range
            ] or [item])[0]

    print(min(curr_data))