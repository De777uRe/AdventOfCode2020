from collections import OrderedDict

if __name__ == "__main__":
    with open("input", 'r') as input_file:
        instruction_map = {}
        line_number = 1
        for instruction in input_file:
            instruction = instruction.strip()
            instruction_map[line_number] = [instruction, False]
            line_number += 1

        print(instruction_map)

        acc = 0
        current_instruction = 1
        is_valid_program = True
        while is_valid_program:
            if current_instruction <= len(instruction_map):
                parsed_instructions = instruction_map[current_instruction][0].split(' ')
                operation = parsed_instructions[0]
                arg1 = int(parsed_instructions[1])
                was_visited = instruction_map[current_instruction][1]
                if was_visited:
                    is_valid_program = False
                    break
                else:
                    instruction_map[current_instruction][1] = True
                    if operation == "nop":
                        current_instruction += 1
                    elif operation == "acc":
                        acc += arg1
                        current_instruction += 1
                    elif operation == "jmp":
                        current_instruction += arg1
        print(acc)



