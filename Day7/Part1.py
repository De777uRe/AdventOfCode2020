import pprint


def parse_rule_to_dict(rule):
    rule_dict = {}
    this_contains_that = rule.split("contain")
    top_color = this_contains_that[0].split("bags")[0].strip()
    rule_dict[top_color] = {}
    # print(f"found top color {top_color}")
    contains_list = [contain_stmt.strip() for contain_stmt in this_contains_that[1].split(',')]
    # print(contains_list)
    if "no other bags" not in contains_list[0]:
        for contain_stmt in contains_list:
            contain_stmt_breakdown = contain_stmt.split(' ')
            number = int(contain_stmt_breakdown[0])
            color = contain_stmt_breakdown[1] + ' ' + contain_stmt_breakdown[2]
            rule_dict[top_color][color] = number
            # print(f"number: {number}, color: {color}")

    # print(rule_dict)
    return rule_dict


if __name__ == "__main__":
    with open("input", 'r') as input_file:
        bag_map = {}
        for rule in input_file:
            bag_map.update(parse_rule_to_dict(rule))

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(bag_map)

        searched_bags = []
        num_found = 0

        target_bag = "shiny gold"
        bag_search_list = []
        for bag in bag_map.keys():
            if target_bag in bag_map[bag].keys():
                bag_search_list.append(bag)
                searched_bags.append(bag)
                num_found += 1

        while len(bag_search_list) > 0:
            target_bag = bag_search_list[0]
            for bag in bag_map.keys():
                if target_bag in bag_map[bag].keys():
                    if bag not in bag_search_list and \
                            bag not in searched_bags:
                        bag_search_list.append(bag)
                        searched_bags.append(bag)
                        num_found += 1
            bag_search_list.remove(target_bag)

        print(num_found)
