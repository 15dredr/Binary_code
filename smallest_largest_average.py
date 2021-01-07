def input_numbers(input_number):
    done = False
    list_of_numbers = []
    while done == False:
        list_of_numbers.append(int(input_number))
        input_number = input("Please type the next number or DONE")
        if input_number == "DONE":
            return list_of_numbers


def average(list_in_order):
    added_together = sum(list_in_order)
    length = len(list_in_order)
    average_of_list = added_together / length
    return average_of_list


first_number = input("Please type your first number")
not_ordered_list = input_numbers(first_number)
ordered_list = sorted(not_ordered_list)
length_list = len(ordered_list)
lowest_number = str(ordered_list[0])
largest_number = str(ordered_list[-1])
average_of_input_list = str(average(ordered_list))
print(
    "The lowest number is " + lowest_number + " the largest number is " + largest_number + " and the average is " + average_of_input_list)
