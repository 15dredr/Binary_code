with open("text_files/shakespeare.txt", "r", encoding="UTF-8") as f:
    line_number = 0
    line_number_list = []
    for line in f:
        # print(line_number, line.strip())
        line_number += 1
        if line_number > 134 and line_number < 2911:  # line 134 is the start
            # 2911 is end'''
            if len(list(line)) > 1:
                if (list(line)[-2]) in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] or "THE END" in line:
                    line_number_list.append(line_number)
print(line_number_list)
for i in range(154):
    print(line_number_list[i:i + 2], i)
