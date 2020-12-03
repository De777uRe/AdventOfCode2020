if __name__ == "__main__":
    with open("input", "r") as input_file:
        num_correct = 0
        for line in input_file:
            params = line.split()
            range = params[0].split("-")
            min = int(range[0])
            max = int(range[1])
            letter_req = params[1].split(":")[0]
            password = params[2]
            letter_count = password.count(letter_req)
            if min <= letter_count <= max:
                num_correct += 1
        print(str(num_correct))
