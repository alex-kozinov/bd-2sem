input_file = "university"
output_file = "university_town"
university_len = 10

def parse_university(line):
    balance = 0
    school = []
    town = []
    for i in range(0, len(line)):
        if line[i] == '(':
            balance += 1
            continue
        if line[i] == ')':
            balance = i + 1
            break
        if balance > 0:
            school.append(line[i])

    while balance < len(line) and line[balance] == ' ':
        balance += 1
    while balance < len(line) and (line[balance] != ' ' and line[balance] != '\n'):
        town.append(line[balance])
        balance += 1

    return ("".join(school), "".join(town))

with open(input_file, "r") as in_:
    with open(output_file, "w") as out_:
        text = in_.read()
        university = text.split("\n")
        result = []
        for line in university:
            lol = parse_university(line)
            if len(lol[0]) == 0 or len(lol[0]) > university_len:
                continue
            result.append(lol)

        for i in result:
            out_.write(i[0] + "#" + i[1] + "\n")