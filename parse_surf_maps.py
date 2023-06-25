import re

# Specified rank - 
specified_rank = 100

# Initialize an empty list for storing parsed data
parsed_data = []

with open('surf_maps.log', 'r', encoding='utf-8') as f:
    for line in f:
        if line.count(',') != 2:
            # parsed_data.append((line.strip(), '', 0, 0))  # Uncomment to keep lines that aren't ranks
            continue
        # Split the line into parts
        map_name, time_str, rank = line.split(', ')

        # Extract the current rank from the rank string
        current_rank = int(rank.split('/')[0].split(': ')[1])

        # If the current rank is less than the specified rank, append the line to parsed_data
        if current_rank <= specified_rank:
            time = time_str.split(': ')[1]
            minutes, seconds = time.split(':')
            seconds, milliseconds = seconds.split('.') if '.' in seconds else (seconds, '0')
            total_seconds = int(minutes) * 60 + int(seconds) + float(milliseconds) / 100
            parsed_data.append((line.strip(), map_name.replace('surf_', ''), total_seconds, current_rank))

# Ask user for sorting method
sort_method = input("Do you want to sort by 1) Rank, 2) Alphabetical Order, or 3) Time? ")

if sort_method == '1':
    # Sort by rank
    parsed_data.sort(key=lambda x: x[3])
elif sort_method == '2':
    # Sort by alphabetical order
    parsed_data.sort(key=lambda x: x[1])
elif sort_method == '3':
    # Sort by time
    parsed_data.sort(key=lambda x: x[2])

# Write the sorted data to the new log file
with open('parsed_surf_maps.log', 'w', encoding='utf-8') as f:
    for line in parsed_data:
        f.write(line[0] + '\n')
