if __name__ == "__main__":
    with open("testinput", 'r') as input_file:
        adapters_by_voltage = {0: [1, 2, 3]}
        for line in input_file:
            voltage = int(line.strip())
            adapters_by_voltage[voltage] = [i for i in range(voltage+1, voltage+4)]

        print(adapters_by_voltage)

        

