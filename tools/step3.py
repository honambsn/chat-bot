def remove_line_breaks_and_spaces(file_path, new_file_path):
    # Open the file and read its content
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove all line breaks from the content
    modified_content = content.replace('\n', '')

    # Remove spaces after periods (.)
    modified_content = modified_content.replace('. ', '.')

    # Write the modified content to a new file
    with open(new_file_path, 'w') as new_file:
        new_file.write(modified_content)


# input_file = "D:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tools\\output.txt"
# output_file = "D:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tools\\new.txt"
# remove_line_breaks_and_spaces(input_file, output_file)
# print("Done")