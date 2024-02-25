def get_text_file_content_except_first_line(file_path):
    # Open the file and read its content
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Join all lines starting from the second line
    content_except_first_line = "".join(lines[1:])

    return content_except_first_line

def write_content_to_new_file(content, output_file_path):
    # Open the new file and write the content to it
    with open(output_file_path, "w") as output_file:
        output_file.write(content)

# Example usage
# file_path = "D:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tmp.txt"
# output_file_path = "D:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tools\\output.txt"

# file_content_except_first_line = get_text_file_content_except_first_line(file_path)
# write_content_to_new_file(file_content_except_first_line, output_file_path)



# print("Done")