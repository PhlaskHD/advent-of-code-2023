def main():
    with open("test.txt") as file:
        content = file.read()
    
    split = content.strip().split("\n")
    total = 0




    for each in split:
        found_first = False
        running = ""
        for char in each:
            running += char
            if char.isnumeric():
                if found_first == False:
                    found_first = True
                    first = char
                last = char
        total += int(first + last)
    
    print(total)


main()