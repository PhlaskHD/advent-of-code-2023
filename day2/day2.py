def main():
    with open("input.txt") as file:
        content = file.read()
    content = content.strip()
    split = content.splitlines()
    games = {}
    for each in split:
        temp = each.split(":")
        games[temp[0]] = {}
        rounds = temp[1].strip().split(";")
        for i in range(len(rounds)):
            color_list = []
            colors = rounds[i].split(",")
            for color in colors:
                sep = color.strip().split(" ")
                color_list.append((sep[1].strip(), sep[0].strip()))
            games[temp[0]][f"Round {i}"] = color_list


    total = checker(games)
    print(total)

    print(fewest_possible(games))
            
            


def checker(dict):
    total = 0
    for each in dict:
        tester = True
        for round in dict[each]:
            for color in dict[each][round]:
                color_string, number = color
                number = int(number)
                if color_string == "red" and number > 12:
                    tester = False
                if color_string == "green" and number > 13:
                    tester = False
                if color_string == "blue" and number > 14:
                    tester = False
        if tester == True:
            total += int(each.split()[1])
    return total

def fewest_possible(dict):
    total = 0
    for each in dict:
        min_red, min_green, min_blue = 0, 0, 0
        for round in dict[each]:
            for color in dict[each][round]:
                color_string, number = color
                number = int(number)
                if color_string == "red" and number > min_red:
                    min_red = number
                if color_string == "green" and number > min_green:
                    min_green = number
                if color_string == "blue" and number > min_blue:
                    min_blue = number
        power = min_red * min_green * min_blue
        total += power
    return total




                




main()