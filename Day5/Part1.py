if __name__ == "__main__":
    with open("input", 'r') as input_file:
        highest_id = 0
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
            if seat_id > highest_id:
                highest_id = seat_id
        print(highest_id)
        # print(f"row {final_row}, column {final_col}")
        # print(f"seat ID {final_row * 8 + final_col}")
