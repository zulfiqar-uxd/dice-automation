# Define the input file and output file
input_file = 'new_id copy 2.txt'
output_file = 'cleaned.txt'

# Create a set to store unique lines
unique_lines = set()

# Open the input file and process its lines
with open(input_file, 'r') as infile:
    for line in infile:
        line = line.strip()  # Remove leading/trailing whitespace
        if line not in unique_lines:
            unique_lines.add(line)

# Write the unique lines to the output file
with open(output_file, 'w') as outfile:
    for line in unique_lines:
        outfile.write(line + '\n')

print(f"Duplicate lines removed. Cleaned content saved to {output_file}")
