import math
import sys



# --------------- открытие файла и возврат списка строк---------#
def reading_file_and_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        return data

    except IOError:
        print("ошибка открытия файла: ", filename)
        sys.exit()


# -----------возврат списка слов---------------------#
def spliting_lines_to_list_words(data):

    fields = data.split()
    return fields

#----------------подсчет частоты появления слова---------#
def count_frequency_word(word_list):

    D = {}

    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D

#--------------------возврат словаря слово - количество появления---------------#
def word_frequencies_for_file(filename):

    lines = reading_file_and_data(filename)
    fields = spliting_lines_to_list_words(lines)
    freq_mapping = count_frequency_word(fields)

    return freq_mapping

#---------------------расчет расстояния ---------------#
def dotProduct(D1, D2):

    Sum = 0.0

    for key in D1:

        if key in D2:
            Sum += (D1[key] * D2[key])
    return Sum

#-------------расчет и возврат угла между векторами--------------#
def vector_angle(D1, D2):

    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1) * dotProduct(D2, D2))

    return math.acos(numerator / denominator)


def documentSimilarity(filename_one, filename_two):

    sorted_word_list_1 = word_frequencies_for_file(filename_one)
    sorted_word_list_2 = word_frequencies_for_file(filename_two)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)

    return distance



#----------открываем файл input---------------#
with open("input.txt", 'r') as file_input:
    lines = file_input.read()
    words_lines = lines.replace('\n',' ')
    words = words_lines.split()
    file_input.close()

#попарно сравниваем файлы и записываем результат в файл scores
    for i, j in zip(words[0::2],words[1::2]):
        print(documentSimilarity(i,j))
        with open("scores.txt", "a") as simp_file:
            simp_file.write(str(documentSimilarity(i,j)) + "\n")

        simp_file.close()






