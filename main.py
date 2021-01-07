with open("text_files/groceries.txt", "r") as f:
    # my_string = f.read()
    my_data = []
    i = 0
    for line in f:
        if line.strip()[0] == "m":
            my_data.append(line.strip())
print(my_data)

with open("text_files/new_file.txt", "w+") as f:
    for item in my_data:
        f.write(item + "\n")
