import re

def validate_dict(passport_values, required_fields):
    all_fields_valid = True
    if all(fields in passport_values.keys() for fields in required_fields) or \
            "cid" not in passport_values.keys() and len(passport_values.keys()) == len(required_fields) - 1:
        if not re.match(valid_year_patterns, passport_values['byr'][0]) or \
                not re.match(valid_year_patterns, passport_values['iyr'][0]) or \
                not re.match(valid_year_patterns, passport_values['eyr'][0]):
            all_fields_valid = False
        if not 1920 <= int(passport_values['byr'][0]) <= 2002 or \
                not 2010 <= int(passport_values['iyr'][0]) <= 2020 or \
                not 2020 <= int(passport_values['eyr'][0]) <= 2030:
            all_fields_valid = False
        if not re.match(valid_height_patterns, passport_values['hgt'][0]):
            all_fields_valid = False
        if 'cm' in passport_values['hgt'][0]:
            if not 150 <= int(passport_values['hgt'][0][:-2]) <= 193:
                all_fields_valid = False
        if 'in' in passport_values['hgt'][0]:
            if not 59 <= int(passport_values['hgt'][0][:-2]) <= 76:
                all_fields_valid = False
        if passport_values['hcl'][0][0] != '#':
            all_fields_valid = False
        if not re.match(valid_hcl_pattern, passport_values['hcl'][0]):
            all_fields_valid = False
        if len(passport_values['ecl']) != 1:
            all_fields_valid = False
        if passport_values['ecl'][0] not in valid_ecl:
            all_fields_valid = False
        if not re.match(valid_pid_pattern, passport_values['pid'][0]):
            all_fields_valid = False
    return all_fields_valid


if __name__ == "__main__":
    with open("input", 'r') as input_file:
        required_fields = {'byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}
        valid_year_patterns = re.compile("^[0-9]{4}$")
        valid_height_patterns = re.compile("[0-9]{2,3}(cm|in)")
        valid_hcl_pattern = re.compile("^#[a-f0-9]{6}$")
        valid_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        valid_pid_pattern = re.compile("^[0-9]{9}$")
        num_valid_passports = 0
        passport_values = {}
        all_fields_valid = True
        for line in input_file:
            if line.isspace():
                if all(fields in passport_values.keys() for fields in required_fields) or \
                        "cid" not in passport_values.keys() and len(passport_values.keys()) == len(required_fields) - 1:
                    if not re.match(valid_year_patterns, passport_values['byr'][0]) or \
                            not re.match(valid_year_patterns, passport_values['iyr'][0]) or \
                            not re.match(valid_year_patterns, passport_values['eyr'][0]):
                        all_fields_valid = False
                    if not 1920 <= int(passport_values['byr'][0]) <= 2002 or \
                            not 2010 <= int(passport_values['iyr'][0]) <= 2020 or \
                            not 2020 <= int(passport_values['eyr'][0]) <= 2030:
                        all_fields_valid = False
                    if not re.match(valid_height_patterns, passport_values['hgt'][0]):
                        all_fields_valid = False
                    if 'cm' in passport_values['hgt'][0]:
                        if not 150 <= int(passport_values['hgt'][0][:-2]) <= 193:
                            all_fields_valid = False
                    if 'in' in passport_values['hgt'][0]:
                        if not 59 <= int(passport_values['hgt'][0][:-2]) <= 76:
                            all_fields_valid = False
                    if passport_values['hcl'][0][0] != '#':
                        all_fields_valid = False
                    if not re.match(valid_hcl_pattern, passport_values['hcl'][0]):
                        all_fields_valid = False
                    if len(passport_values['ecl']) != 1:
                        all_fields_valid = False
                    if passport_values['ecl'][0] not in valid_ecl:
                        all_fields_valid = False
                    if not re.match(valid_pid_pattern, passport_values['pid'][0]):
                        all_fields_valid = False

                    if all_fields_valid:
                        num_valid_passports += 1
                passport_values = {}
                all_fields_valid = True
            else:
                pairs = line.split(' ')
                for pair in pairs:
                    pair_split = pair.split(':')
                    passport_values[pair_split[0].strip()] = pair_split[1].split()
        all_fields_valid = True
        pairs = line.split(' ')
        for pair in pairs:
            pair_split = pair.split(':')
            passport_values[pair_split[0].strip()] = pair_split[1].split()

        if validate_dict(passport_values, required_fields):
            num_valid_passports += 1
        print(num_valid_passports)
