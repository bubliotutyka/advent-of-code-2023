import os

data_file_path = os.path.join(os.path.dirname(__file__), 'data')

lines = []

digits_in_letters = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open(data_file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())

int_result = []

for line in lines:
    first_int = ""
    last_int = ""

    i = 0

    while i < len(line) and (first_int == ""):
        if line[i].isdigit():
            first_int = line[i]
        elif line[i].isalpha():
            letters = line[i]
            j = i

            while len(letters) < 5 and line[j].isalpha() and (first_int == ""):
                letters += line[j + 1]

                if letters in digits_in_letters:
                    first_int = str(digits_in_letters[letters])

                j += 1

        i += 1

    i = len(line) - 1

    while i >= 0 and (last_int == ""):
        if line[i].isdigit():
            last_int = line[i]
        elif line[i].isalpha():
            letters = line[i]
            j = i

            while len(letters) < 5 and line[j].isalpha() and (last_int == ""):
                letters = line[j - 1] + letters

                if letters in digits_in_letters:
                    last_int = str(digits_in_letters[letters])

                j -= 1

        i -= 1

    if (first_int != "") & (last_int != ""):
        int_result.append(int(first_int + last_int))
    elif (first_int != "") & (last_int == ""):
        int_result.append(int(first_int + first_int))

print(sum(int_result))
