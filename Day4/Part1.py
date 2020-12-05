def validate_dict(passport_values, required_fields):
    if all(fields in passport_values.keys() for fields in required_fields) or \
            "cid" not in passport_values.keys() and len(passport_values.keys()) == len(required_fields) - 1:
        return True
    return False

if __name__ == "__main__":
    with open("input", 'r') as input_file:
        required_fields = {'byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}
        num_valid_passports = 0
        passport_values = {}
        for line in input_file:
            if line.isspace():
                if all(fields in passport_values.keys() for fields in required_fields) or \
                        "cid" not in passport_values.keys() and len(passport_values.keys()) == len(required_fields) - 1:
                    num_valid_passports += 1
                passport_values = {}
                continue
            pairs = line.split(' ')
            for pair in pairs:
                pair_split = pair.split(':')
                passport_values[pair_split[0].strip()] = pair_split[1].split()
        pairs = line.split(' ')
        for pair in pairs:
            pair_split = pair.split(':')
            passport_values[pair_split[0].strip()] = pair_split[1].split()
        if validate_dict(passport_values, required_fields):
            num_valid_passports += 1
        print(num_valid_passports)


