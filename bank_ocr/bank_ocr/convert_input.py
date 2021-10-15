def _parse_digit(digit_str):
    cleaned_digit = digit_str.replace(' ', '')
    lines = cleaned_digit.split('\n')
    non_empty_lines = [line for line in lines if line != '']

    digit_converter = {
        ('_', '||', '|_|'): '0',
        ('|', '|'): '1',
        ('_', '_|', '|_'): '2',
        ('_', '_|', '_|'): '3',
        ('|_|', '|'): '4',
        ('_', '|_', '_|'): '5',
        ('_', '|_', '|_|'): '6',
        ('_', '|', '|'): '7',
        ('_', '|_|', '|_|'): '8',
        ('_', '|_|', '_|'): '9',
    }

    digit_value = digit_converter[tuple(non_empty_lines)]
    return digit_value
