if __name__ == "__main__":
    with open("input", "r") as input_file:
        num_correct = 0
        for line in input_file:
            params = line.split()
            range = params[0].split("-")
            pos1 = int(range[0])
            pos2 = int(range[1])
            letter_req = params[1].split(":")[0]
            password = params[2]
            if password[pos1-1] is letter_req:
                if password[pos2-1] is not letter_req:
                    num_correct += 1
            elif password[pos2-1] is letter_req:
                num_correct += 1
        print(str(num_correct))
