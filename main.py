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
