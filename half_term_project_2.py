from collections import Counter
import pygal


def tlm_boiler_plate():
    """
    :return:list of the start and end line of the book, the function makes a new file with only the book in it
    """
    with open('text_files/the_last_man.txt', 'r', encoding="UTF-8") as f:  # opens the text file to be read
        line_number = 0
        book_started = False
        book_start_and_end = []  # so the start and end line can be returned to be used in other functions
        for line in f:
            if line.strip() == "CHAPTER I.":  # this is where the book starts
                book_started = True
                book_start_and_end = book_start_and_end + [line_number]
            if book_started:
                line_number += 1  # line number increases after the book has stated as there is no point including the boiler plate
                i = open('text_files/reduced_books/tlm_reduced.txt', 'a+', encoding="UTF-8")
                i.write(line.strip() + '\n')  # adds the line to a new text file
                i.close()
            if line.strip() == "THE END.":  # this is where the book ends
                book_started = False
                book_start_and_end = book_start_and_end + [line_number]
        return book_start_and_end


def acc_boiler_plate():
    """
        :return:list of the start and end line of the book, the function makes a new file with only the book in it
        """
    with open('text_files/a_christmas_carol.txt', 'r', encoding="UTF-8") as f:  # opens the text file to be read
        line_number = 0
        book_started = False
        book_start_and_end = []  # so the start and end line can be returned to be used in other functions
        for line in f:
            if line.strip() == "STAVE ONE":  # this is where the book starts
                book_started = True
                book_start_and_end = book_start_and_end + [line_number]
            if book_started:
                line_number += 1  # line number increases after the book has stated as there is no point including the boiler plate
                i = open('text_files/reduced_books/acc_reduced.txt', 'a+', encoding="UTF-8")
                i.write(line.strip() + '\n')  # adds the line to a new text file
                i.close()
            if line.strip() == "End of the Project Gutenberg EBook of A Christmas Carol, by Charles Dickens":  # this is where the book ends
                book_started = False
                book_start_and_end = book_start_and_end + [line_number]
        return book_start_and_end


def atotc_boiler_plate():
    """
        :return:list of the start and end line of the book, the function makes a new file with only the book in it
        """
    with open('text_files/a_tale_of_two_cities.txt', 'r', encoding="UTF-8") as f:  # opens the text file to be read
        line_number = 0
        book_started = False
        book_start_and_end = []  # so the start and end line can be returned to be used in other functions
        for line in f:
            if line.strip() == "I. The Period":  # this is where the book starts
                book_started = True
                book_start_and_end = book_start_and_end + [line_number]
            if book_started:
                line_number += 1  # line number increases after the book has stated as there is no point including the boiler plate
                i = open('text_files/reduced_books/atotc_reduced.txt', 'a+', encoding="UTF-8")
                i.write(line.strip() + '\n')  # adds the line to a new text file
                i.close()
            if line.strip() == "End of the Project Gutenberg EBook of A Tale of Two Cities, by Charles Dickens":  # this is where the book ends
                book_started = False
                book_start_and_end = book_start_and_end + [line_number]
        return book_start_and_end


def frank_boiler_plate():
    """
        :return:list of the start and end line of the book, the function makes a new file with only the book in it
        """
    with open('text_files/frankenstein.txt', 'r', encoding="UTF-8") as f:  # opens the text file to be read
        line_number = 0
        book_started = False
        book_start_and_end = []  # so the start and end line can be returned to be used in other functions
        for line in f:
            if line.strip() == "Letter 1":  # this is where the book starts
                book_started = True
                book_start_and_end = book_start_and_end + [line_number]
            if book_started:
                line_number += 1  # line number increases after the book has stated as there is no point including the boiler plate
                i = open('text_files/reduced_books/frank_reduced.txt', 'a+', encoding="UTF-8")
                i.write(line.strip() + '\n')  # adds the line to a new text file
                i.close()
            if line.strip() == "End of the Project Gutenberg EBook of Frankenstein, by Mary Wollstonecraft (Godwin) Shelley":  # this is where the book ends
                book_started = False
                book_start_and_end = book_start_and_end + [line_number]
        return book_start_and_end


def pi_boiler_plate():
    """
        :return:list of the start and end line of the book, the function makes a new file with only the book in it
        """
    with open('text_files/poirot_investigates.txt', 'r', encoding="UTF-8") as f:  # opens the text file to be read
        line_number = 0
        book_started = False
        book_start_and_end = []  # so the start and end line can be returned to be used in other functions
        for line in f:
            if line.strip() == "I":  # this is where the book starts
                book_started = True
                book_start_and_end = book_start_and_end + [line_number]
            if book_started:
                line_number += 1  # line number increases after the book has stated as there is no point including the boiler plate
                i = open('text_files/reduced_books/pi_reduced.txt', 'a+', encoding="UTF-8")
                i.write(line.strip() + '\n')  # adds the line to a new text file
                i.close()
            if line.strip() == "THE END":  # this is where the book ends
                book_started = False
                book_start_and_end = book_start_and_end + [line_number]
        return book_start_and_end


def pap_boiler_plate():
    """
        :return:list of the start and end line of the book, the function makes a new file with only the book in it
        """
    with open('text_files/pride_and_prejudice.txt', 'r', encoding="UTF-8") as f:  # opens the text file to be read
        line_number = 0
        book_started = False
        book_start_and_end = []  # so the start and end line can be returned to be used in other functions
        for line in f:
            if line.strip() == "Chapter 1":  # this is where the book starts
                book_started = True
                book_start_and_end = book_start_and_end + [line_number]
            if book_started:
                line_number += 1  # line number increases after the book has stated as there is no point including the boiler plate
                i = open('text_files/reduced_books/pap_reduced.txt', 'a+', encoding="UTF-8")
                i.write(line.strip() + '\n')  # adds the line to a new text file
                i.close()
            if line.strip() == "End of the Project Gutenberg EBook of Pride and Prejudice, by Jane Austen":  # this is where the book ends
                book_started = False
                book_start_and_end = book_start_and_end + [line_number]
        return book_start_and_end


def sas_boiler_plate():
    """
        :return:list of the start and end line of the book, the function makes a new file with only the book in it
        """
    with open('text_files/sense_and_sensibility.txt', 'r', encoding="UTF-8") as f:  # opens the text file to be read
        line_number = 0
        book_started = False
        book_start_and_end = []  # so the start and end line can be returned to be used in other functions
        for line in f:
            if line.strip() == "CHAPTER I":  # this is where the book starts
                book_started = True
                book_start_and_end = book_start_and_end + [line_number]
            if book_started:
                line_number += 1  # line number increases after the book has stated as there is no point including the boiler plate
                i = open('text_files/reduced_books/sas_reduced.txt', 'a+', encoding="UTF-8")
                i.write(line.strip() + '\n')  # adds the line to a new text file
                i.close()
            if line.strip() == "THE END":  # this is where the book ends
                book_started = False
                book_start_and_end = book_start_and_end + [line_number]
        return book_start_and_end


def tmaas_boiler_plate():
    """
        :return:list of the start and end line of the book, the function makes a new file with only the book in it
        """
    with open('text_files/The_mysterious_affair_at_styles.txt', 'r',
              encoding="UTF-8") as f:  # opens the text file to be read
        line_number = 0
        book_started = False
        book_start_and_end = []  # so the start and end line can be returned to be used in other functions
        for line in f:
            if line.strip() == "CHAPTER I. I GO TO STYLES":  # this is where the book starts
                book_started = True
                book_start_and_end = book_start_and_end + [line_number]
            if book_started:
                line_number += 1  # line number increases after the book has stated as there is no point including the boiler plate
                i = open('text_files/reduced_books/tmaas_reduced.txt', 'a+', encoding="UTF-8")
                i.write(line.strip() + '\n')  # adds the line to a new text file
                i.close()
            if line.strip() == "THE END":  # this is where the book ends
                book_started = False
                book_start_and_end = book_start_and_end + [line_number]
        return book_start_and_end


def tlm_chapters(book_start_and_end):
    """

    :param book_start_and_end: the start and end of the book
    :return: adds the chapter wanted to a new file
    """
    chapter_wanted = int(input("Which chapter do you want to look at?"))
    line_number = 0
    line_number_list = []  # list of the starts and ends of every chapter
    book_start = book_start_and_end[0]  # this position in the list should be the start of the book line number
    book_end = book_start_and_end[-1]  # this position in the list should be the end of the list line number
    line_number_list.append(book_start)  # The start of the book will be the start of the first chapter
    chapter_start_end = []  # blank list for the end and start line of the wanted chapter to go into
    with open('text_files/reduced_books/tlm_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            line_number += 1
            if 'CHAPTER' in line:  # chapter indicates the beginning of a chapter
                line_number_list.append(line_number)
    line_number_list.append(book_end)
    for i in range(len(line_number_list) - 1):
        chapter_start_end.append(
            line_number_list[i: i + 2])  # pairs the line numbers so the start and end of the chapters are together
    chapter_start_end.pop(0)
    chapter_lines = chapter_start_end[(chapter_wanted - 1): chapter_wanted]
    chapter_lines = chapter_lines[0]  # as this is a list of lists
    chapter_start = chapter_lines[0]  # the first term is the start of the chapter
    chapter_end = chapter_lines[-1]  # the second term is the end of the chapter
    chapter_started = False
    with open('text_files/reduced_books/tlm_reduced.txt', 'r', encoding="UTF-8") as fp:
        line_number = 0
        for line in fp:
            line_number += 1
            if line_number == chapter_start:
                chapter_started = True
            if chapter_started:
                i = open('text_files/book_chapters/the_last_man_chapters/tlm_needed_chapter.txt', 'a+',
                         encoding="UTF-8")
                i.write(line.strip() + '\n')
                i.close()
            if line_number == chapter_end:
                chapter_started = False


def acc_chapters(book_start_and_end):
    chapter_wanted = int(input("Which chapter do you want to look at?"))
    line_number = 0
    line_number_list = []  # list of the starts and ends of every chapter
    book_start = book_start_and_end[0]
    book_end = book_start_and_end[-1]
    line_number_list.append(book_start)
    chapter_start_end = []
    with open('text_files/reduced_books/acc_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            line_number += 1
            if 'STAVE' in line:
                line_number_list.append(line_number)
    line_number_list.append(book_end)
    for i in range(len(line_number_list) - 1):
        chapter_start_end.append(line_number_list[i: i + 2])
    chapter_start_end.pop(0)
    chapter_lines = chapter_start_end[(chapter_wanted - 1): chapter_wanted]
    chapter_lines = chapter_lines[0]
    chapter_start = chapter_lines[0]
    chapter_end = chapter_lines[-1]
    chapter_started = False
    with open('text_files/reduced_books/acc_reduced.txt', 'r', encoding="UTF-8") as fp:
        line_number = 0
        for line in fp:
            line_number += 1
            if line_number == chapter_start:
                chapter_started = True
            if chapter_started:
                i = open('text_files/book_chapters/acc_chapter_needed.txt', 'a+',
                         encoding="UTF-8")
                i.write(line.strip() + '\n')
                i.close()
            if line_number == chapter_end:
                chapter_started = False


def atotc_chapters(book_start_and_end):
    chapter_wanted = int(input("Which chapter do you want to look at?"))
    line_number = 0
    line_number_list = []  # list of the starts and ends of every chapter
    book_start = book_start_and_end[0]
    book_end = book_start_and_end[-1]
    line_number_list.append(book_start)
    chapter_start_end = []
    with open('text_files/reduced_books/atotc_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            line_number += 1
            if 'X' or 'I' or 'V' in line:
                line_number_list.append(line_number)
    line_number_list.append(book_end)
    for i in range(len(line_number_list) - 1):
        chapter_start_end.append(line_number_list[i: i + 2])
    chapter_start_end.pop(0)
    chapter_lines = chapter_start_end[(chapter_wanted - 1): chapter_wanted]
    chapter_lines = chapter_lines[0]
    chapter_start = chapter_lines[0]
    chapter_end = chapter_lines[-1]
    chapter_started = False
    with open('text_files/reduced_books/atotc_reduced.txt', 'r', encoding="UTF-8") as fp:
        line_number = 0
        for line in fp:
            line_number += 1
            if line_number == chapter_start:
                chapter_started = True
            if chapter_started:
                i = open('text_files/book_chapters/atotc_chapter_needed.txt', 'a+',
                         encoding="UTF-8")
                i.write(line.strip() + '\n')
                i.close()
            if line_number == chapter_end:
                chapter_started = False


def frank_chapters(book_start_and_end):
    chapter_wanted = int(input("Which chapter do you want to look at?"))
    line_number = 0
    line_number_list = []  # list of the starts and ends of every chapter
    book_start = book_start_and_end[0]
    book_end = book_start_and_end[-1]
    line_number_list.append(book_start)
    chapter_start_end = []
    with open('text_files/reduced_books/frank_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            line_number += 1
            if '—.' or 'Letter' in line:
                line_number_list.append(line_number)
    line_number_list.append(book_end)
    for i in range(len(line_number_list) - 1):
        chapter_start_end.append(line_number_list[i: i + 2])
    chapter_start_end.pop(0)
    chapter_lines = chapter_start_end[(chapter_wanted - 1): chapter_wanted]
    chapter_lines = chapter_lines[0]
    chapter_start = chapter_lines[0]
    chapter_end = chapter_lines[-1]
    chapter_started = False
    with open('text_files/reduced_books/frank_reduced.txt', 'r', encoding="UTF-8") as fp:
        line_number = 0
        for line in fp:
            line_number += 1
            if line_number == chapter_start:
                chapter_started = True
            if chapter_started:
                i = open('text_files/book_chapters/frank_chapter_needed.txt', 'a+',
                         encoding="UTF-8")
                i.write(line.strip() + '\n')
                i.close()
            if line_number == chapter_end:
                chapter_started = False


def pi_chapters(book_start_and_end):
    chapter_wanted = int(input("Which chapter do you want to look at?"))
    line_number = 0
    line_number_list = []  # list of the starts and ends of every chapter
    book_start = book_start_and_end[0]
    book_end = book_start_and_end[-1]
    line_number_list.append(book_start)
    chapter_start_end = []
    with open('text_files/reduced_books/pi_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            line_number += 1
            if 'X' or 'I' or 'V' in line:
                line_number_list.append(line_number)
    line_number_list.append(book_end)
    for i in range(len(line_number_list) - 1):
        chapter_start_end.append(line_number_list[i: i + 2])
    chapter_start_end.pop(0)
    chapter_lines = chapter_start_end[(chapter_wanted - 1): chapter_wanted]
    chapter_lines = chapter_lines[0]
    chapter_start = chapter_lines[0]
    chapter_end = chapter_lines[-1]
    chapter_started = False
    with open('text_files/reduced_books/pi_reduced.txt', 'r', encoding="UTF-8") as fp:
        line_number = 0
        for line in fp:
            line_number += 1
            if line_number == chapter_start:
                chapter_started = True
            if chapter_started:
                i = open('text_files/book_chapters/pi_chapter_needed.txt', 'a+',
                         encoding="UTF-8")
                i.write(line.strip() + '\n')
                i.close()
            if line_number == chapter_end:
                chapter_started = False


def pap_chapters(book_start_and_end):
    chapter_wanted = int(input("Which chapter do you want to look at?"))
    line_number = 0
    line_number_list = []  # list of the starts and ends of every chapter
    book_start = book_start_and_end[0]
    book_end = book_start_and_end[-1]
    line_number_list.append(book_start)
    chapter_start_end = []
    with open('text_files/reduced_books/pap_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            line_number += 1
            if 'Chapter' in line:
                line_number_list.append(line_number)
    line_number_list.append(book_end)
    for i in range(len(line_number_list) - 1):
        chapter_start_end.append(line_number_list[i: i + 2])
    chapter_start_end.pop(0)
    chapter_lines = chapter_start_end[(chapter_wanted - 1): chapter_wanted]
    chapter_lines = chapter_lines[0]
    chapter_start = chapter_lines[0]
    chapter_end = chapter_lines[-1]
    chapter_started = False
    with open('text_files/reduced_books/pap_reduced.txt', 'r', encoding="UTF-8") as fp:
        line_number = 0
        for line in fp:
            line_number += 1
            if line_number == chapter_start:
                chapter_started = True
            if chapter_started:
                i = open('text_files/book_chapters/pap_chapter_needed.txt', 'a+',
                         encoding="UTF-8")
                i.write(line.strip() + '\n')
                i.close()
            if line_number == chapter_end:
                chapter_started = False


def sas_chapters(book_start_and_end):
    chapter_wanted = int(input("Which chapter do you want to look at?"))
    line_number = 0
    line_number_list = []  # list of the starts and ends of every chapter
    book_start = book_start_and_end[0]
    book_end = book_start_and_end[-1]
    line_number_list.append(book_start)
    chapter_start_end = []
    with open('text_files/reduced_books/sas_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            line_number += 1
            if 'CHAPTER' in line:
                line_number_list.append(line_number)
    line_number_list.append(book_end)
    for i in range(len(line_number_list) - 1):
        chapter_start_end.append(line_number_list[i: i + 2])
    chapter_start_end.pop(0)
    chapter_lines = chapter_start_end[(chapter_wanted - 1): chapter_wanted]
    chapter_lines = chapter_lines[0]
    chapter_start = chapter_lines[0]
    chapter_end = chapter_lines[-1]
    chapter_started = False
    with open('text_files/reduced_books/sas_reduced.txt', 'r', encoding="UTF-8") as fp:
        line_number = 0
        for line in fp:
            line_number += 1
            if line_number == chapter_start:
                chapter_started = True
            if chapter_started:
                i = open('text_files/book_chapters/sas_chapter_needed.txt', 'a+',
                         encoding="UTF-8")
                i.write(line.strip() + '\n')
                i.close()
            if line_number == chapter_end:
                chapter_started = False


def tmaas_chapters(book_start_and_end):
    chapter_wanted = int(input("Which chapter do you want to look at?"))
    line_number = 0
    line_number_list = []  # list of the starts and ends of every chapter
    book_start = book_start_and_end[0]
    book_end = book_start_and_end[-1]
    line_number_list.append(book_start)
    chapter_start_end = []
    with open('text_files/reduced_books/tmaas_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            line_number += 1
            if 'CHAPTER' in line:
                line_number_list.append(line_number)
    line_number_list.append(book_end)
    for i in range(len(line_number_list) - 1):
        chapter_start_end.append(line_number_list[i: i + 2])
    chapter_start_end.pop(0)
    chapter_lines = chapter_start_end[(chapter_wanted - 1): chapter_wanted]
    chapter_lines = chapter_lines[0]
    chapter_start = chapter_lines[0]
    chapter_end = chapter_lines[-1]
    chapter_started = False
    with open('text_files/reduced_books/tmaas_reduced.txt', 'r', encoding="UTF-8") as fp:
        line_number = 0
        for line in fp:
            line_number += 1
            if line_number == chapter_start:
                chapter_started = True
            if chapter_started:
                i = open('text_files/book_chapters/tmaas_chapter_needed.txt', 'a+',
                         encoding="UTF-8")
                i.write(line.strip() + '\n')
                i.close()
            if line_number == chapter_end:
                chapter_started = False


def tlm_sentences():
    """

    :return: the number of sentences in a predetermined chapter
    """
    f = open('text_files/book_chapters/the_last_man_chapters/tlm_needed_chapter.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')  # splits the data at every full stop, dividing it into sentences
    number_of_sentences = len(sentences)
    return number_of_sentences


def acc_sentences():
    f = open('text_files/book_chapters/acc_needed_chapter.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')
    number_of_sentences = len(sentences)
    return number_of_sentences


def atotc_sentences():
    f = open('text_files/book_chapters/atotc_needed_chapter.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')
    number_of_sentences = len(sentences)
    return number_of_sentences


def frank_sentences():
    f = open('text_files/book_chapters/frank_needed_chapter.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')
    number_of_sentences = len(sentences)
    return number_of_sentences


def pi_sentences():
    f = open('text_files/book_chapters/pi_needed_chapter.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')
    number_of_sentences = len(sentences)
    return number_of_sentences


def pap_sentences():
    f = open('text_files/book_chapters/pap_needed_chapter.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')
    number_of_sentences = len(sentences)
    return number_of_sentences


def sas_sentences():
    f = open('text_files/book_chapters/sas_needed_chapter.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')
    number_of_sentences = len(sentences)
    return number_of_sentences


def tmaas_sentences():
    f = open('text_files/book_chapters/tmaas_needed_chapter.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')
    number_of_sentences = len(sentences)
    return number_of_sentences


def tlm_number_words():
    chapter = open('text_files/book_chapters/the_last_man_chapters/tlm_needed_chapter.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()  # splits the text everytime there is a blank space, dividing it into words
    number_of_words = len(words)
    return number_of_words


def acc_number_words():
    chapter = open('text_files/book_chapters/acc_needed_chapter.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()
    number_of_words = len(words)
    return number_of_words


def atotc_number_words():
    chapter = open('text_files/book_chapters/atotc_needed_chapter.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()
    number_of_words = len(words)
    return number_of_words


def frank_number_words():
    chapter = open('text_files/book_chapters/frank_needed_chapter.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()
    number_of_words = len(words)
    return number_of_words


def pi_number_words():
    chapter = open('text_files/book_chapters/pi_needed_chapter.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()
    number_of_words = len(words)
    return number_of_words


def pap_number_words():
    chapter = open('text_files/book_chapters/pap_needed_chapter.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()
    number_of_words = len(words)
    return number_of_words


def sas_number_words():
    chapter = open('text_files/book_chapters/sas_needed_chapter.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()
    number_of_words = len(words)
    return number_of_words


def tmaas_number_words():
    chapter = open('text_files/book_chapters/tmaas_needed_chapter.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()
    number_of_words = len(words)
    return number_of_words


def average_sentences(number_of_words, number_of_sentences):
    """

    :param number_of_words: number of words in a specified chunk of text
    :param number_of_sentences: number of sentences in a specified chunk of text
    :return: returns the average number of words per sentence in a chapter
    """
    average_sentence_length = number_of_words / number_of_sentences
    return average_sentence_length


def tlm_unique_words():
    """

    :return: the number of unique words in a specified the last man chapter
    """
    with open('text_files/book_chapters/the_last_man_chapters/tlm_needed_chapter.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()  # makes all words lowercase so capitalised words will be counted as the same word as uncapitalised words
        words = text.split()  # splits the text into words
        words = [word.strip('.,!;()[]') for word in words]  # gets rid of punctuation
        words = [word.replace("'s", '') for word in words]  # makes plural words singular
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def acc_unique_words():
    with open('text_files/book_chapters/acc_needed_chapter', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def atotc_unique_words():
    with open('text_files/book_chapters/atotc_needed_chapter', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def frank_unique_words():
    with open('text_files/book_chapters/frank_needed_chapter', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def pi_unique_words():
    with open('text_files/book_chapters/pi_needed_chapter', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def pap_unique_words():
    with open('text_files/book_chapters/pap_needed_chapter', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def sas_unique_words():
    with open('text_files/book_chapters/sas_needed_chapter', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def tmaas_unique_words():
    with open('text_files/book_chapters/tmaas_needed_chapter', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def tlm_common_words():
    """

    :return: the number of words not in the list of most common english words
    """
    with open('text_files/most_common_words.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    with open('text_files/book_chapters/the_last_man_chapters/tlm_needed_chapter.txt', 'r', encoding="UTF-8") as a:
        chapter_text = a.read()
        chapter_text = chapter_text.lower()  # makes everything lowercase
        words = chapter_text.split()  # splits the text into words
        words = [word.strip('.,!;()[]') for word in words]  # gets rid of punctuation
        words = [word.replace("'s", '') for word in words]  # makes all words singular
        uncommon_words = []
        for word in words:
            if word in text:
                uncommon_words.append(word)
    return len(uncommon_words)


def acc_common_words():
    with open('text_files/most_common_words.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    with open('text_files/book_chapters/acc_needed_chapter.txt', 'r', encoding="UTF-8") as a:
        chapter_text = a.read()
        chapter_text = chapter_text.lower()
        words = chapter_text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        uncommon_words = []
        for word in words:
            if word in text:
                uncommon_words.append(word)
    return len(uncommon_words)


def atotc_common_words():
    with open('text_files/most_common_words.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    with open('text_files/book_chapters/atotc_needed_chapter.txt', 'r', encoding="UTF-8") as a:
        chapter_text = a.read()
        chapter_text = chapter_text.lower()
        words = chapter_text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        uncommon_words = []
        for word in words:
            if word in text:
                uncommon_words.append(word)
    return len(uncommon_words)


def frank_common_words():
    with open('text_files/most_common_words.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    with open('text_files/book_chapters/frank_needed_chapter.txt', 'r', encoding="UTF-8") as a:
        chapter_text = a.read()
        chapter_text = chapter_text.lower()
        words = chapter_text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        uncommon_words = []
        for word in words:
            if word in text:
                uncommon_words.append(word)
    return len(uncommon_words)


def pi_common_words():
    with open('text_files/most_common_words.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    with open('text_files/book_chapters/pi_needed_chapter.txt', 'r', encoding="UTF-8") as a:
        chapter_text = a.read()
        chapter_text = chapter_text.lower()
        words = chapter_text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        uncommon_words = []
        for word in words:
            if word in text:
                uncommon_words.append(word)
    return len(uncommon_words)


def pap_common_words():
    with open('text_files/most_common_words.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    with open('text_files/book_chapters/pap_needed_chapter.txt', 'r', encoding="UTF-8") as a:
        chapter_text = a.read()
        chapter_text = chapter_text.lower()
        words = chapter_text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        uncommon_words = []
        for word in words:
            if word in text:
                uncommon_words.append(word)
    return len(uncommon_words)


def sas_common_words():
    with open('text_files/most_common_words.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    with open('text_files/book_chapters/sas_needed_chapter.txt', 'r', encoding="UTF-8") as a:
        chapter_text = a.read()
        chapter_text = chapter_text.lower()
        words = chapter_text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        uncommon_words = []
        for word in words:
            if word in text:
                uncommon_words.append(word)
    return len(uncommon_words)


def tmaas_common_words():
    with open('text_files/most_common_words.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    with open('text_files/book_chapters/tmaas_needed_chapter.txt', 'r', encoding="UTF-8") as a:
        chapter_text = a.read()
        chapter_text = chapter_text.lower()
        words = chapter_text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        uncommon_words = []
        for word in words:
            if word in text:
                uncommon_words.append(word)
    return len(uncommon_words)


def tlm_analysis_chapter():
    """

    :return: the number of chapters in the last man
    """
    with open('text_files/reduced_books/tlm_reduced.txt', 'r', encoding="UTF-8") as f:
        number_of_chapters = 0
        for line in f:
            if 'CHAPTER' in line:
                number_of_chapters += 1
        return number_of_chapters


def acc_analysis_chapter():
    """

    :return: the number of chapters in a christmas carol
    """
    with open('text_files/reduced_books/acc_reduced.txt', 'r+', encoding="UTF-8") as f:
        number_of_chapters = 0
        for line in f:
            if 'STAVE' in line:
                number_of_chapters += 1
        return number_of_chapters


def atotc_analysis_chapter():
    """

    :return: the number of chapters in a tale of two cities
    """
    with open('text_files/reduced_books/atotc_reduced.txt', 'r+', encoding="UTF-8") as f:
        number_of_chapters = 0
        for line in f:
            if 'X' or 'I' or 'V' in line:
                number_of_chapters += 1
        return number_of_chapters


def frank_analysis_chapter():
    """

    :return: the number of chapters in frankenstein
    """
    with open('text_files/reduced_books/frank_reduced.txt', 'r+', encoding="UTF-8") as f:
        number_of_chapters = 0
        for line in f:
            if 'Chapter' or 'letter' in line:
                number_of_chapters += 1
        return number_of_chapters


def pi_analysis_chapter():
    """

    :return: the number of chapters in poirot investigates
    """
    with open('text_files/reduced_books/pi_reduced.txt', 'r+', encoding="UTF-8") as f:
        number_of_chapters = 0
        for line in f:
            if 'X' or 'I' or 'V' in line:
                number_of_chapters += 1
        return number_of_chapters


def pap_analysis_chapter():
    """

    :return: the number of chapters in pride and prejudice
    """
    with open('text_files/reduced_books/pap_reduced.txt', 'r+', encoding="UTF-8") as f:
        number_of_chapters = 0
        for line in f:
            if 'Chapter' in line:
                number_of_chapters += 1
        return number_of_chapters


def sas_analysis_chapter():
    """

    :return: the number of chapters in sense and sensibility
    """
    with open('text_files/reduced_books/pap_reduced.txt', 'r+', encoding="UTF-8") as f:
        number_of_chapters = 0
        for line in f:
            if 'CHAPTER' in line:
                number_of_chapters += 1
        return number_of_chapters


def tmaas_analysis_chapter():
    """

    :return: the number of chapters in the mysterious affair at styles
    """
    with open('text_files/reduced_books/pap_reduced.txt', 'r+', encoding="UTF-8") as f:
        number_of_chapters = 0
        for line in f:
            if 'CHAPTER' in line:
                number_of_chapters += 1
        return number_of_chapters


def tlm_analysis_sentences():
    """

    :return: number of sentences in a book
    """
    f = open('text_files/reduced_books/tlm_reduced.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')  # splits the data whenever there is a . dividing it into sentences
    number_of_sentences = len(sentences)
    return number_of_sentences


def acc_analysis_sentences():
    """

    :return: number of sentences in a book
    """
    f = open('text_files/reduced_books/acc_reduced.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')  # splits the data whenever there is a . dividing it into sentences
    number_of_sentences = len(sentences)
    return number_of_sentences


def frank_analysis_sentences():
    """

    :return: number of sentences in a book
    """
    f = open('text_files/reduced_books/frank_reduced.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')  # splits the data whenever there is a . dividing it into sentences
    number_of_sentences = len(sentences)
    return number_of_sentences


def pi_analysis_sentences():
    """

    :return: number of sentences in a book
    """
    f = open('text_files/reduced_books/pi_reduced.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')  # splits the data whenever there is a . dividing it into sentences
    number_of_sentences = len(sentences)
    return number_of_sentences


def pap_analysis_sentences():
    """

    :return: number of sentences in a book
    """
    f = open('text_files/reduced_books/pap_reduced.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')  # splits the data whenever there is a . dividing it into sentences
    number_of_sentences = len(sentences)
    return number_of_sentences


def sas_analysis_sentences():
    """

    :return: number of sentences in a book
    """
    f = open('text_files/reduced_books/sas_reduced.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')  # splits the data whenever there is a . dividing it into sentences
    number_of_sentences = len(sentences)
    return number_of_sentences


def tmaas_analysis_sentences():
    """

    :return: number of sentences in a book
    """
    f = open('text_files/reduced_books/tmaas_reduced.txt', 'r', encoding="UTF-8")
    data = f.read()
    sentences = data.split('.')  # splits the data whenever there is a . dividing it into sentences
    number_of_sentences = len(sentences)
    return number_of_sentences


def analysis_num_words(book):
    """

    :param book_reduced: the txt file of the reduced book
    :return: the number of words in a provided book
    """
    chapter = open(f'text_files/reduced_books/{book}_reduced.txt', 'r', encoding="UTF-8")
    chapter_data = chapter.read()
    words = chapter_data.split()
    number_of_words = len(words)
    return number_of_words


def analysis_unique_words(book):
    """

    :param book_reduced: the reduced book that the user wants to find the uncommon words in
    :return: how many unique words there are in the book
    """
    with open(f'text_files/reduced_books/{book}_reduced.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def word_frequency(book):
    """

    :param book_reduced: the reduced book that the user wants the frequency of a word from
    :return: the frequency of the word wanted
    """
    with open(f'text_files/reduced_books/{book}_reduced.txt', 'r', encoding="UTF-8") as f:
        word_wanted = input('What word do you want the frequency of?')
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        word_freq = 0
        for word in words:
            if word == word_wanted:
                word_freq += 1
        return word_freq


def top_50_words(book):
    """

    :param book_reduced: the book the user wants the top 50 words for
    :return: the top 50 important words in the book
    """
    with open(f'text_files/reduced_books/{book}_reduced.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
    number_words = Counter(words)
    important_words = []
    for word in number_words:
        if len(word) > 3:
            if word != 'that' or 'with' or 'from' or 'were' or 'which' or 'their' or 'they' or 'would' or 'have' or 'when' or 'could' or 'while':
                important_words.append(word)
    top_50 = important_words[0:49]
    return top_50


def author_texts(book1, author, book2):
    """

    :param reduced_book_1: the first book by the author
    :param author: author of the books
    :param reduced_book_2: second book by the author
    :return: puts the books by the same author into one file
    """
    with open(f'text_files/reduced_books/{book1}_reduced.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            i = open(f'text_files/full_text_by_author/{author}.txt', 'a+', encoding="UTF-8")
            i.write(line.strip() + '\n')
            i.close()
    with open(f'text_files/reduced_books/{book2}_reduced.txt', 'r', encoding="UTF-8") as a:
        for line in a:
            i = open(f'text_files/full_text_by_author/{author}.txt', 'a+', encoding="UTF-8")
            i.write(line.strip() + '\n')
            i.close()


def author_unique_words(author):
    """

    :param author: author of the books
    :return: the number of unique words in both texts by an author
    """
    with open(f'text_files/full_text_by_author/{author}.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def author_freq_words(author):
    """

    :param author: author of the books you want the word frequency of
    :return: the frequency of the word in the authors texts
    """
    with open(f'text_files/full_text_by_author/{author}.txt', 'r', encoding="UTF-8") as f:
        word_wanted = input('What word do you want the frequency of?')
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        word_freq = 0
        for word in words:
            if word == word_wanted:
                word_freq += 1
        return word_freq


def author_uncommon_words(author):
    with open(f'text_files/full_text_by_author/{author}', 'r', encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        unique_words = set(unique_words)
        return len(unique_words)


def text_graphs_chapters(acc_chapters, atotc_chapters, frank_chapters, pi_chapters, pap_chapters, sas_chapters,
                         tlm_chapters, tmaas_chapters):
    import pygal
    bar_chart_chapters = pygal.HorizontalBar()
    bar_chart_chapters._title = 'Number of chapters in each Novel'
    bar_chart_chapters.add('A Christmas Carol', acc_chapters)
    bar_chart_chapters.add('A Tale of Two Cities', atotc_chapters)
    bar_chart_chapters.add('Frankenstein', frank_chapters)
    bar_chart_chapters.add('Poirot Investigates', pi_chapters)
    bar_chart_chapters.add('Pride and Prejudice', pap_chapters)
    bar_chart_chapters.add('Sense and Sensibility', sas_chapters)
    bar_chart_chapters.add('The Last Man', tlm_chapters)
    bar_chart_chapters.add('The Mysterious Affair at Styles', tmaas_chapters)
    print(bar_chart_chapters.render_to_file('text_files/graphs/chapter_graph.svg'))


def graph_number_of_words(acc_words, atotc_words, frank_words, pi_words, pap_words, sas_words,
                          tlm_words, tmaas_words):
    import pygal
    bar_chart_words = pygal.HorizontalBar()
    bar_chart_words._title = 'Number of words in each Novel'
    bar_chart_words.add('A Christmas Carol', acc_words)
    bar_chart_words.add('A Tale of Two Cities', atotc_words)
    bar_chart_words.add('Frankenstein', frank_words)
    bar_chart_words.add('Poirot Investigates', pi_words)
    bar_chart_words.add('Pride and Prejudice', pap_words)
    bar_chart_words.add('Sense and Sensibility', sas_words)
    bar_chart_words.add('The Last Man', tlm_words)
    bar_chart_words.add('The Mysterious Affair at Styles', tmaas_words)
    print(bar_chart_words.render_to_file('text_files/graphs/words_graph.svg'))


def graph_unique_words(acc_words, atotc_words, frank_words, pi_words, pap_words, sas_words,
                       tlm_words, tmaas_words):
    import pygal
    bar_chart_unique_words = pygal.HorizontalBar()
    bar_chart_unique_words._title = 'Number of unique words in each Novel'
    bar_chart_unique_words.add('A Christmas Carol', acc_words)
    bar_chart_unique_words.add('A Tale of Two Cities', atotc_words)
    bar_chart_unique_words.add('Frankenstein', frank_words)
    bar_chart_unique_words.add('Poirot Investigates', pi_words)
    bar_chart_unique_words.add('Pride and Prejudice', pap_words)
    bar_chart_unique_words.add('Sense and Sensibility', sas_words)
    bar_chart_unique_words.add('The Last Man', tlm_words)
    bar_chart_unique_words.add('The Mysterious Affair at Styles', tmaas_words)
    print(bar_chart_unique_words.render_to_file('text_files/graphs/words_graph.svg'))


def unique_words_by_author(mary_shelley_unique, charles_dickens_unique, agatha_christie_unique, jane_austen_unique):
    import pygal
    bar_chart_unique_words = pygal.HorizontalBar()
    bar_chart_unique_words._title = 'Number of unique words by each author'
    bar_chart_unique_words.add('Mary Shelley', mary_shelley_unique)
    bar_chart_unique_words.add('Charles Dickens', charles_dickens_unique)
    bar_chart_unique_words.add('Agatha Christie', agatha_christie_unique)
    bar_chart_unique_words.add('Jane Austen', jane_austen_unique)
    print(bar_chart_unique_words.render_to_file('text_files/graphs/unique_words_by_author_graph.svg'))


def uncommon_words_by_author(mary_shelley_unique, charles_dickens_unique, agatha_christie_unique, jane_austen_unique):
    import pygal
    bar_chart_unique_words = pygal.HorizontalBar()
    bar_chart_unique_words._title = 'Number of uncommon words by each author'
    bar_chart_unique_words.add('Mary Shelley', mary_shelley_unique)
    bar_chart_unique_words.add('Charles Dickens', charles_dickens_unique)
    bar_chart_unique_words.add('Agatha Christie', agatha_christie_unique)
    bar_chart_unique_words.add('JAne Austen', jane_austen_unique)
    print(bar_chart_unique_words.render_to_file('text_files/graphs/unique_words_by_author_graph.svg'))


author_texts('acc', 'charles_dickens', 'atotc')
author_texts('pap', 'jane_austen', 'sas')
author_texts('pi', 'agatha_christie', 'tmaas')

text_graphs_chapters(acc_analysis_chapter(), atotc_analysis_chapter(), frank_analysis_chapter(), pi_analysis_chapter(),
                     pap_analysis_chapter(), sas_analysis_chapter(), tlm_analysis_chapter(), tmaas_analysis_chapter())
graph_number_of_words(analysis_num_words('acc'), analysis_num_words('atotc'), analysis_num_words('frank'),
                      analysis_num_words('pi'), analysis_num_words('pap'), analysis_num_words('sas'),
                      analysis_num_words('tlm'), analysis_num_words('tmaas'))
graph_unique_words(analysis_unique_words('acc'), analysis_unique_words('atotc'), analysis_unique_words('frank'),
                   analysis_unique_words('pi'), analysis_unique_words('pap'), analysis_unique_words('sas'),
                   analysis_unique_words('tlm'), analysis_unique_words('tmaas'))
unique_words_by_author(author_unique_words('mary_shelley'), author_unique_words('charles_dickens'),
                       author_unique_words('agatha_christie'), author_unique_words('jane_austen'))
uncommon_words_by_author(author_uncommon_words('mary_shelley'), author_uncommon_words('charles_dickens'),
                         author_uncommon_words('agatha_christie'), author_uncommon_words('jane_austen'))
