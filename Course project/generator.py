import random

input_file = "data_for_generation/university_town"
output_file = "rand_faculty.sql"
table_name = "Faculty"
start_code = 50
alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ"
form = "INSERT INTO {} VALUES ({},  '{}', '{}', '{}', {}, {}, {}, {})"

def faculty_name():
    len = random.randint(4, 7)
    return "".join(random.sample(alphabet, len))


def form_query(file, university):
    result = []
    current_code = start_code

    for i in university:
        num = random.randint(1, 6)
        for j in range(0, num):
            budget = random.randint(30, 100)
            result.append(form.format(table_name, current_code, faculty_name(),
                                     i[0], i[1], budget,
                                        0, 1, random.randint(2, 8)))
            current_code += 1
    return result
with open(input_file, "r") as in_:
    with open(output_file, "w") as out_:
        result = []

        for i in in_:
            other = i.split("\n")[0]
            result.append(other.split("#"))


        queries = form_query(out_, result)
        for i in queries:
            out_.write(i + "\n")
