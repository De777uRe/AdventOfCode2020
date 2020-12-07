def find_set_intersections(list_of_sets):
    intersect = list_of_sets[0]
    for i in range(1, len(list_of_sets)):
        intersect = intersect.intersection(list_of_sets[i])
    return len(intersect)

if __name__ == "__main__":
    with open("input", 'r') as input_file:
        sum_count = 0
        group_answers = []
        answer_set = set()
        for line in input_file:
            if line.isspace():
                sum_count += find_set_intersections(group_answers)
                answer_set = set()
                group_answers = []
            else:
                for letter in line.strip():
                    answer_set.add(letter)
                group_answers.append(answer_set)
                answer_set = set()
        for letter in line.strip():
            answer_set.add(letter)
        group_answers.append(answer_set)
        sum_count += find_set_intersections(group_answers)
        print(sum_count)
