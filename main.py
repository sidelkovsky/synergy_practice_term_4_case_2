asterisk_digits = [
    '* * **   **   **   ** * *',
    '  *    *    *    *    *  ',
    '* * *    ** * **    * * *',
    '* * *    ** * *    ** * *',
    '*   **   ** * *    *    *',
    '* * **    * * *    ** * *',
    '* * **    * * **   ** * *',
    '* * *    *    *    *    *',
    '* * **   ** * **   ** * *',
    '* * **   ** * *    ** * *',
]

number_to_print = '0123456789'

def asteriks_output( number_to_print ):

    # five rows of asteriks
    for i in range(5):
        row_string = []
        for j in number_to_print:
            row_string.append(asterisk_digits[int(j)][i*5:(i+1)*5])
        print("\t".join(row_string))

asteriks_output(number_to_print)


def is_valid_integer_in_range(number, start, end):
    if number.isdigit():
        number = int(number)
        if number > start and number < end:
            return True
    return False


day, month, year = (0,) * 3


while True:
    day = input("Введите число вашего рождения ( от 1 до 31 ):\n")
    if is_valid_integer_in_range(day, 0, 32):
        day = int(day)
        break
    else:
        print("\n Это должно быть число от 1 до 31! Давайте еще раз!\n")

while True:
    month = input("Введите месяц вашего рождения ( от 1 до 12 ):\n")
    if is_valid_integer_in_range(month, 0, 13):
        month = int(month)
        break
    else:
        print("\n Это должно быть число от 1 до 12! Давайте еще раз!\n")

while True:
    year = input("Введите год вашего рождения ( от 1900 до 2020 ):\n")
    if is_valid_integer_in_range(year, 1899, 2021):
        year = int(year)
        break
    else:
        print("\n Это должно быть число от 1900 до 2020! Давайте еще раз!\n")


