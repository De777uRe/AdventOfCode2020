import numpy as np

if __name__ == "__main__":
    with open("input", 'r') as input_file:
        path_patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        input_file_lines = input_file.readlines()
        line_len = len(input_file_lines[0]) - 1
        slope_tree_count = []
        for pattern in path_patterns:
            num_trees = 0
            row = 0
            col = 0
            while row < len(input_file_lines):
                if input_file_lines[row][col % line_len] == '#':
                    num_trees += 1
                row += pattern[1]
                col += pattern[0]
            slope_tree_count.append(num_trees)
        print(np.prod(slope_tree_count))

