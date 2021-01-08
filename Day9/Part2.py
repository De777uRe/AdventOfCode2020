if __name__ == "__main__":
    with open("input", 'r') as input_file:
        preamble = 25
        position = 1
        numbers_by_line = {}
        invalid_num = 0
        for line in input_file:
            numbers_by_line[position] = int(line.strip())
            position += 1

        # print(numbers_by_line)

        for i in range(preamble+1, len(numbers_by_line)):
            found_sum = False
            for j in range(i-preamble, i):
                value_set = list(numbers_by_line.values())
                value_set = value_set[i-preamble:i]
                print(value_set)
                if numbers_by_line[i] - numbers_by_line[j] in value_set:
                    found_sum = True
            if not found_sum:
                invalid_num = numbers_by_line[i]
                print(invalid_num)
                break

        span_found = False
        span_start = 1
        span = []
        while not span_found:
            sum = 0
            for i in range(span_start, len(numbers_by_line)):
                span.append(numbers_by_line[i])
                sum += numbers_by_line[i]
                if sum == invalid_num:
                    print(min(span) + max(span))
                    span_found = True
                    break
                if sum > invalid_num:
                    span = []
                    span_start += 1
                    break

