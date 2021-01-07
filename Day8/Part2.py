from collections import OrderedDict

def reset_program(program_map):
    for key in program_map.keys():
        program_map[key][1] = False
    return program_map

if __name__ == "__main__":
    with open("input", 'r') as input_file:
        instruction_map = {}
        line_number = 1
        for instruction in input_file:
            instruction = instruction.strip()
            instruction_map[line_number] = [instruction, False]
            line_number += 1

        swapped_instructions = []
        current_instruction = 1
        while current_instruction <= len(instruction_map):
            acc = 0
            current_instruction = 1
            is_valid_program = True
            first_pass = True
            while is_valid_program and current_instruction <= len(instruction_map):
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
                            if current_instruction not in swapped_instructions and first_pass:
                                swapped_instructions.append(current_instruction)
                                current_instruction += arg1
                                first_pass = False
                            else:
                                current_instruction += 1
                        elif operation == "acc":
                            acc += arg1
                            current_instruction += 1
                        elif operation == "jmp":
                            if current_instruction not in swapped_instructions and first_pass:
                                swapped_instructions.append(current_instruction)
                                current_instruction += 1
                                first_pass = False
                            else:
                                current_instruction += arg1
            instruction_map = reset_program(instruction_map)
        print(acc)



