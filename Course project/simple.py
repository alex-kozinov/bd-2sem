import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def read_str():
    ans = input(">")
    while ans == "":
        ans = input(">")
    return ans

def special_read(correct=[]):
    ans = input(">")
    while ans not in correct:
        ans = input(">")
    return ans

def end_command():
    input("Нажмите на любую клавишу для продолжения...")

def print_middle(our_string):
    ts = os.get_terminal_size()
    format_str = "{:^" + str(ts.columns) + "}"
    print(format_str.format(our_string))

def to_sql_format(str_to_format):
    if str_to_format == None:
        return "NULL"
    return str_to_format

def print_table(column_name, cort):
    n = len(column_name)
    lens = []

    for x in column_name:
        lens.append(len(x) + 2)

    for i in range(0, n):
        for j in cort:
            lens[i] = max(lens[i], len(str(j[i])))

    width = sum(lens[i] for i in range(0, n)) + n + 1
    format_str = "|"
    horisont_str = "+" + "-" * (width - 2) + "+"
    for i in range(0, n):
        number_format = "{0[" + str(i) + "]:^" + str(lens[i]) + "}|"
        format_str = format_str + number_format

    print_middle(horisont_str)
    print_middle(format_str.format(column_name))
    print_middle(horisont_str)
    for i in cort:
        print_middle(format_str.format(i))
        print_middle(horisont_str)
