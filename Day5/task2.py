def get_lookup_table(mapping: str) -> list[tuple[range, int]]:

        table = []
        print(mapping.splitlines()[0])
        for line in mapping.splitlines()[1:]:
            dest_start, src_start, range_ = [int(x) for x in line.split()]

            table.append((
                range(src_start, src_start + range_),
                dest_start - src_start,
            ))
        return table
def find_intersection(range1, range2):
    return range(
                        max(range1.start, range2.start),
                        min(range1.stop, range2.stop),
                    )

try: 
    with open("./Day5/input.txt") as f:
        file_content = f.read()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
   
    curr_data, *maps = file_content.split('\n\n')
    curr_data = [int(item) for item in curr_data.removeprefix('seeds: ').split()]
    curr_data_range = []
    for i in range(0, len(curr_data), 2):
        curr_data_range.append(range(curr_data[i], curr_data[i]+ curr_data[i+1]))
    for mapping in maps:
        temp_curr_data_range = []
        table = get_lookup_table(mapping)
        for item in curr_data_range:
            for map_range, diff in enumerate(table):
                # get the intersection of the two ranges
                intersection = find_intersection(item, map_range)
                # if the intersection is not empty
                if intersection:
                    # add the new range to the list
                    temp_curr_data_range.append(range(min(intersection) + diff, max(intersection) + diff))
                    # for the ones that are not in the intersection, add two ranges to the list
                    temp_curr_data_range.append(range(item.start, min(intersection)))
                    temp_curr_data_range.append(range(max(intersection), item.stop))
                else:
                    temp_curr_data_range.append(item)
        curr_data_range = temp_curr_data_range
    print( min(range_.start for range_ in curr_data_range))

