"""
Знайти у тексті, введеному з клавіатури pattern (також введений з клавіатури),
кількість його повторів
"""
import re
def find_text(text):
    flag = True
    user_input=""
    while flag:
        if bool(re.match("^[A-Za-z .,:;!?]+$", user_input)) == True:
            user_input = input(text)
            flag = False
        else:
            user_input = input(text)
    return user_input.lower()
def spliter_finder(text):
    most_frequent = []
    for point_2 in text[::2]:
        most_frequent.append(point_2)
    return most_frequent
def finder(text):
    most_frequent = []
    for point_1 in text:
        pattern = point_1
        t = re.findall(pattern, text)
        most_frequent.append(len(t))
    return most_frequent
def find_most_frequent():
    text1 = find_text("Введіть текст: ")
    print(spliter_finder(finder(text1)))
find_most_frequent()
