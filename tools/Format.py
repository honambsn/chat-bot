import step1 as s1
import step2 as s2
import step3 as s3



#step 1 : get first line - name of story
file_path = 'd:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tmp.txt'

# Call the function to get the first line
first_line = s1.get_first_line(file_path)
first_line = first_line[:-1]
print(first_line) 

print("Done step 1")

#step 2: get text content except the first line (name of story)
output_file_path = "D:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tools\\pre-output.txt"
file_content_except_first_line = s2.get_text_file_content_except_first_line(file_path)
s2.write_content_to_new_file(file_content_except_first_line, output_file_path)

print("Done step 2")


#step 3: get text content and format it
input_file = "D:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tools\\pre-output.txt"
output_file = "D:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\story2\\" + first_line + ".txt"
s3.remove_line_breaks_and_spaces(input_file, output_file)
print("Done step 3")
    

import os

file_path = "D:\\Ba Nam\\nam 4 hoc ky 2\\chatbot\\demo\\tools\\pre-output.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
else:
    print(f"File '{file_path}' does not exist.")
