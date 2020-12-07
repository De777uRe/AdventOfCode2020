if __name__ == "__main__":
    with open("input", 'r') as input_file:
        sum_count = 0
        group_answers = set()
        for line in input_file:
            if line.isspace():
                sum_count += len(group_answers)
                group_answers = set()
            for letter in line.strip():
                group_answers.add(letter)
        sum_count += len(group_answers)
        print(sum_count)
