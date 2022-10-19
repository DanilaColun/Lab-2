import csv
import os
import time



def esc(code):
    return f'\u001b[{code}m'

BLACK = esc(40) # Escape последовательности
RED = esc(41)
GREEN = esc(42)
END = esc(0)
WHITE = esc(47)




# Задание с узором
def drawing():
    print(f'{BLACK}{"  " * 10}{END}{"  " * 6}{BLACK}{"  " * 10}{END}{"  " * 6}{BLACK}{"  " * 10}{END}',
          f'{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}',
          f'{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 6}{BLACK}{"  " * 2}{END}',
          f'{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 5}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 5}{END}{"  " * 6}{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 5}{END}',
          f'{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 2}{END}{"  " * 9}{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 2}{END}{"  " * 9}{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 2}{END}',
          f'{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 2}{END}{"  " * 9}{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 2}{END}{"  " * 9}{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 2}{END}',
          f'{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 9}{END}{"  " * 2}{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 9}{END}{"  " * 2}{BLACK}{"  " * 2}{END}{"  " * 3}{BLACK}{"  " * 9}{END}',
          sep="\n")


# Задание с флагом
def flag_bg():
    print(f'{GREEN}{"  " * 42}{END}', f'{GREEN}{"  " * 42}{END}', f'{GREEN}{"  " * 18}{RED}{"  " * 2}{GREEN}{"  " * 22}{END}',
          f'{GREEN}{"  " * 16}{RED}{"  " * 6}{GREEN}{"  " * 20}{END}',
          f'{GREEN}{"  " * 14}{RED}{"  " * 10}{GREEN}{"  " * 18}{END}',
          f'{GREEN}{"  " * 12}{RED}{"  " * 14}{GREEN}{"  " * 16}{END}',
          f'{GREEN}{"  " * 10}{RED}{"  " * 18}{GREEN}{"  " * 14}{END}',
          f'{GREEN}{"  " * 8}{RED}{"  " * 22}{GREEN}{"  " * 12}{END}',
          f'{GREEN}{"  " * 10}{RED}{"  " * 18}{GREEN}{"  " * 14}{END}',
          f'{GREEN}{"  " * 12}{RED}{"  " * 14}{GREEN}{"  " * 16}{END}',
          f'{GREEN}{"  " * 14}{RED}{"  " * 10}{GREEN}{"  " * 18}{END}',
          f'{GREEN}{"  " * 16}{RED}{"  " * 6}{GREEN}{"  " * 20}{END}',
          f'{GREEN}{"  " * 18}{RED}{"  " * 2}{GREEN}{"  " * 22}{END}',
          f'{GREEN}{"  " * 42}{END}', f'{GREEN}{"  " * 42}{END}',
          sep="\n")

print("\n", "Флаг страны Бангладеш:", "\n")
flag_bg()
print("\n", "Повторяющийся узор:", "\n")
drawing()
print("\n")


def array_init(array_in): # График функции 2x+3
    for i in range(11):
        for j in range(10):
            if j == 0:
                array_in[i][j] = step * (9 - i) + 3
            if i == 10:
                array_in[i][j] = j
    return array_in


def array_fill(array_fi, st):
    for i in range(10):
        for j in range(10):
            if abs(array_fi[i][0] - result[9 - j]) < st:
                for k in range(9):
                    if 8 - k == j:
                        array_fi[i][k + 1] = 1
    return array_fi


def print_plot(array_pl):
    for i in range(9):
        line = " "
        for j in range(10):
            if j == 0:
                line += WHITE + str(array_pl[i][j]) + "\t"
            if array_pl[i][j] == 0:
                line += "   "
            if array_pl[i][j] == 1:
                line += RED + "   " + WHITE
        line += END
        print(line)
    print(f' {WHITE}0.0\t1  2  3  4  5  6  7  8  9  {END}')


print("График функции y=2x+3:", "\n")
array_plot = [[0 for col in range(10)] for row in range(11)]
result = [0 for col in range(10)]
for i in range(10):
    result[i] = 2 * i + 3
step = round(abs(result[9] - result[0]) / 9, 1)
array_init(array_plot)
array_fill(array_plot, step)
print_plot(array_plot)
print()


with open("books-en.csv", "r", encoding="windows-1251") as csvfile: # Процент. соотношение
    table = csv.reader(csvfile, delimiter=";")
    data = []
    row_count = 0
    row_count_before_1990 = 0
    row_count_after_1990 = 0
    for row in table:
        row_count += 1
        data.append(list(row[3].split("-")))

    for i in range(1, row_count):
        if int(data[i][0]) < 1990:
            row_count_before_1990 += 1
        if int(data[i][0]) >= 1990:
            row_count_after_1990 += 1
    procent_before_1990 = (row_count_before_1990 / row_count) * 100
    procent_after_1990 = (row_count_after_1990 / row_count) * 100
    array_plot_new = [[0 for col in range(10)] for row in range(10)]


    def array_init_new(array_in):
        for i in range(10):
            for j in range(10):
                if j == 0 and i == 6:
                    array_in[i][j] = str(round(procent_before_1990)) + "%"
                if j == 0 and i == 1:
                    array_in[i][j] = str(round(procent_after_1990)) + "%"
                if array_in[i][0] == 0:
                    array_in[i][0] = "   "
                if i == 0 and j == 0:
                    array_in[i][j] = "100%"

        return array_in


    def array_fill(array_fi):
        for i in range(9):
            for j in range(10):
                if i >= 6:
                    array_fi[i][2] = 1
                if i >= 1:
                    array_fi[i][5] = 1


    def draw_plot_new(array_pl):
        for i in range(9):
            line = " "
            for j in range(10):
                if j == 0:
                    line += WHITE + str(array_pl[i][j])
                if array_pl[i][j] == 0:
                    line += "  "
                if array_pl[i][j] == 1 and j == 2:
                    line += RED + "  " + WHITE
                if array_pl[i][j] == 1 and j == 5:
                    line += GREEN + "   " + WHITE
            line += END
            print(line)
        print("   ", "<1990", ">=1990")


    print("Процентное соотношение книг выпуска до и после 1990-го года:", "\n")
    array_init_new(array_plot_new)
    array_fill(array_plot_new)
    draw_plot_new(array_plot_new)

print(f'Количество книжек выпуска раньше 1990: {row_count_before_1990}')
print(f'Количество книжек выпуска 1990-го года или позже: {row_count_after_1990}')



da = "" # Анимация (доп. задание)
print('Напишите "Да", если хотите увидеть анимацию: ')
da = input()
if da == "Да":
    os.system("cls")
    print(f'{BLACK}{"  " * 10}{END}')
    time.sleep(0.6)
    os.system("cls")
    print(f'{BLACK}{"  " * 10}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    time.sleep(0.6)
    os.system("cls")
    print(f'{BLACK}{"  " * 10}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  "}{END}')
    print(f'{BLACK}{"  " * 10}{END}')
    time.sleep(0.6)
    os.system("cls")
    print(f'{BLACK}{"  " * 10}{END}')
    print(f'{BLACK}{"  "}{END}{"  " * 8}{BLACK}{"  "}')
    print(f'{BLACK}{"  "}{END}{"  " * 8}{BLACK}{"  "}')
    print(f'{BLACK}{"  "}{END}{"  " * 8}{BLACK}{"  "}')
    print(f'{BLACK}{"  "}{END}{"  " * 8}{BLACK}{"  "}')
    print(f'{BLACK}{"  "}{END}{"  " * 8}{BLACK}{"  "}')
    print(f'{BLACK}{"  "}{END}{"  " * 8}{BLACK}{"  "}')
    print(f'{BLACK}{"  "}{END}{"  " * 8}{BLACK}{"  "}')
    print(f'{BLACK}{"  " * 10}{END}')

else:
    print("Неверный ответ.")
