from datetime import date, datetime

"""
Service data and functions
"""

asterisk_digits = {
    "0": '* * **   **   **   ** * *',
    "1": '  *    *    *    *    *  ',
    "2": '* * *    ** * **    * * *',
    "3": '* * *    ** * *    ** * *',
    "4": '*   **   ** * *    *    *',
    "5": '* * **    * * *    ** * *',
    "6": '* * **    * * **   ** * *',
    "7": '* * *    *    *    *    *',
    "8": '* * **   ** * **   ** * *',
    "9": '* * **   ** * *    ** * *',
    "s": '          * * *          ',
}

def asteriks_date_output( birth_date_string ):

    output = ''
    # five rows of asteriks
    for i in range(5):
        row_string = []
        for j in birth_date_string:
            if(j.isdigit()):
                idx = j
            else:
                idx = "s"
            row_string.append(asterisk_digits.get(idx)[i*5:(i+1)*5])
        print("\t".join(row_string))
    

def is_valid_integer_in_range(number, start, end):
    if number.isdigit():
        number = int(number)
        if number > start and number < end:
            return True
    return False

def is_leap_year(year):
    return ( year % 4 == 0 and year % 100 != 0 or year % 400 ==0 )

def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def years_as_word(number):
    number = number % 10
    if number == 1:
        return "год"
    if number > 1 and number < 5:
        return "года"
    return "лет"

"""
Actual program
"""

day, month, year = (0,) * 3

while True:
    day = input("Введите число вашего рождения ( от 1 до 31 ): ")
    if is_valid_integer_in_range(day, 0, 32):
        break
    else:
        print("\nЭто должно быть число от 1 до 31! Давайте еще раз!")

while True:
    month = input("Введите месяц вашего рождения ( от 1 до 12 ): ")
    if is_valid_integer_in_range(month, 0, 13):
        break
    else:
        print("\nЭто должно быть число от 1 до 12! Давайте еще раз!")

while True:
    year = input("Введите год вашего рождения ( от 1900 до 2020 ): ")
    if is_valid_integer_in_range(year, 1899, 2021):
        break
    else:
        print("\nЭто должно быть число от 1900 до 2020! Давайте еще раз!")

if is_leap_year(int(year)):
    print("\nГод вашего рождения был вискосоным.\n")
else:
    print("\nГод вашего рождения не был вискосоным.\n")

birth_date_string = "-".join([day, month, year])
birth_date = datetime.strptime(birth_date_string, '%d-%m-%Y').date()
num_years = calculate_age(birth_date)
years_as_word = years_as_word(num_years)

print(f"Вам {num_years} {years_as_word}.\n")

asteriks_date_output(birth_date_string)
