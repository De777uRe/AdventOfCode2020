if __name__ == "__main__":
    with open("input", "r") as input_file:
        nums = [int(num.strip()) for num in input_file]
        for num in nums:
            complement = 2020 - num
            if complement in nums:
                print(num * complement)
