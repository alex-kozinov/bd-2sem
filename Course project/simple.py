import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def read_str():
    ans = input(">")
    while ans == "":
        ans = input(">")
    return ans


def print_table(column_name, cort):
    n = len(column_name)
    lens = []

    for x in column_name:
        lens.append(len(x))

    for i in range(0, n):
        for j in cort:
            lens[i] = max(lens[i], len(j[i]))

    width = sum(lens[i] for i in range(0, n)) + n + 1
    format_str = "|"
    horisont_str = "+" + "-" * (width - 2) + "+"
    for i in range(0, n):
        number_format = "{0[" + str(i) + "]:>" + str(lens[i]) + "}|"
        format_str = format_str + number_format

    print(horisont_str)
    print(format_str.format(column_name));
    print(horisont_str)
    for i in cort:
        print(format_str.format(i))
        print(horisont_str)
