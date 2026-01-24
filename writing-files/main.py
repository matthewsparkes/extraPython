
txt_data = "I like cheese!"

file_path = "output.txt"        # relative file path (when i generate it, it will be in the same folder as the python file)

with open(file=file_path, mode="w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}'")