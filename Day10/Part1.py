if __name__ == "__main__":
    with open("input", 'r') as input_file:
        adapters_by_voltage = {0: [1, 2, 3]}
        for line in input_file:
            voltage = int(line.strip())
            adapters_by_voltage[voltage] = [i for i in range(voltage+1, voltage+4)]

        adapters_by_voltage = dict(sorted(adapters_by_voltage.items()))
        device_voltage = max(adapters_by_voltage.keys()) + 3
        print(adapters_by_voltage)

        voltage_differences = {3: 1}
        for k, v in adapters_by_voltage.items():
            for voltage in v:
                if voltage in adapters_by_voltage.keys():
                    if voltage - k in voltage_differences:
                        voltage_differences[voltage - k] += 1
                    else:
                        voltage_differences[voltage - k] = 1
                    break

        voltage_differences = dict(sorted(voltage_differences.items()))
        print(voltage_differences)
        print(voltage_differences[1] * voltage_differences[3])

