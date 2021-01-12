if __name__ == "__main__":
    with open("testinput", 'r') as input_file:
        adapters_by_voltage = {0: [1, 2, 3]}
        for line in input_file:
            voltage = int(line.strip())
            adapters_by_voltage[voltage] = [i for i in range(voltage+1, voltage+4)]

        adapters_by_voltage = dict(sorted(adapters_by_voltage.items()))
        device_voltage = max(adapters_by_voltage.keys()) + 3
        print(adapters_by_voltage)

        num_combos_by_adapter = {}
        for k, v in adapters_by_voltage.items():
            num_combos_by_adapter[k] = len([i for i in v if i in adapters_by_voltage.keys()])
        num_combos_by_adapter[19] = 1

        num_variations = 1
        for num_combos in num_combos_by_adapter.values():
            num_variations *= num_combos

        print(num_combos_by_adapter)
        print(num_variations)
