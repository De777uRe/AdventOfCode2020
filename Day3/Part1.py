if __name__ == "__main__":
    with open("input", 'r') as input_file:
        input_file_lines = input_file.readlines()
        row = 0
        col = 0
        line_len = len(input_file_lines[0]) - 1
        num_trees = 0
        while row < len(input_file_lines):
            if input_file_lines[row][col % line_len] == '#':
                num_trees += 1
            row += 1
            col += 3
        print(num_trees)

