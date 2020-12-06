if __name__ == "__main__":
    with open("input", 'r') as input_file:
        id_set = set()
        for line in input_file:
            min_row = 0
            max_row = 127
            min_col = 0
            max_col = 7
            for letter in line:
                if letter == 'B':
                    min_row = (min_row + max_row) // 2 + 1
                elif letter == 'F':
                    max_row = (min_row + max_row) // 2
                elif letter == 'R':
                    min_col = (min_col + max_col) // 2 + 1
                elif letter == 'L':
                    max_col = (min_col + max_col) // 2
            final_row = (min_row + max_row) // 2
            final_col = (min_col + max_col) // 2
            seat_id = final_row * 8 + final_col
            id_set.add(seat_id)
        print(sorted(set(range(min(id_set), max(id_set))) - id_set))
        # print(id_set)
        # print(f"row {final_row}, column {final_col}")
        # print(f"seat ID {final_row * 8 + final_col}")
