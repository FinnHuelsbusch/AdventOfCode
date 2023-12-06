def get_lookup_table(mapping: str) -> list[tuple[range, int]]:

        table = []
        print(mapping.splitlines()[0])
        for line in mapping.splitlines()[1:]:
            dest_start, src_start, range_ = [int(x) for x in line.split()]
            table.append((range(src_start, src_start + range_), dest_start - src_start))
        # Sort by source range start
        table.sort(key=lambda x: x[0].start)
        return table
  

try: 
    with open("./Day5/input.txt") as f:
        file_content = f.read()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
   
    curr_data, *maps = file_content.split('\n\n')
    curr_data = [int(item) for item in curr_data.removeprefix('seeds: ').split()]
    curr_data_ranges = []
    for i in range(0, len(curr_data), 2):
        curr_data_ranges.append(range(curr_data[i], curr_data[i]+ curr_data[i+1]))
    for mapping in maps:
        temp_curr_data_ranges = []
        table = get_lookup_table(mapping)
        
        while curr_data_ranges:
            curr_data_range = curr_data_ranges.pop()
            intersection_found = False
            for map_range, diff in table:
                intersection = range(max(map_range.start, curr_data_range.start),min(map_range.stop, curr_data_range.stop))
                # if the intersection is not empty
                if intersection.stop > intersection.start:
                    intersection_found = True
                    # add the new range to the list
                    temp_curr_data_ranges.append(range(intersection.start + diff, intersection.stop + diff))
                    if intersection.start > curr_data_range.start:
                        below_intersection = range(curr_data_range.start, intersection.start)
                        curr_data_ranges.append(below_intersection)
                    if intersection.stop < curr_data_range.stop:
                        above_intersection = range(intersection.stop, curr_data_range.stop)
                        curr_data_ranges.append(above_intersection)
                    continue
            if not intersection_found:
                temp_curr_data_ranges.append(curr_data_range)
        curr_data_ranges = temp_curr_data_ranges
        print(len(curr_data_ranges))
        
    print( min(range_.start for range_ in curr_data_ranges))

