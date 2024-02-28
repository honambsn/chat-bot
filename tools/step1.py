def get_first_line(file_path):
    # Open the file for reading
    with open(file_path, 'r', encoding='utf-8') as f:
        # Read the first line
        first_line = f.readline()
    # Return the first line
    return first_line

# Define the file path
# file_path = 'd:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tmp.txt'

# # Call the function to get the first line
# first_line = get_first_line(file_path)

# # Print the first line
# print(first_line)
