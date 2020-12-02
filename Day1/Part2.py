if __name__ == "__main__":
    with open("input", "r") as input_file:
        nums = [int(num.strip()) for num in input_file]
        nums.sort(reverse=True)
        for num in nums:
            cap = 2020 - num
            filtered_nums = list(filter(lambda num: num <= cap, nums))
            for filtered_num in filtered_nums:
                final_num = 2020 - num - filtered_num
                if final_num in filtered_nums:
                    print(num * filtered_num * final_num)
