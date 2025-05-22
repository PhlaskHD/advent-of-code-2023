def main():
    with open("input.txt") as file:
        content = file.read()
    
    split = content.strip().split("\n")
    total = 0

    cleaned = list(map(extract_digits, split))



    for each in cleaned:
        total += int(each[0] + each[len(each)-1])
    
    print(total)

def extract_digits(word):
    digits = []
    num_words = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "zero":"0"}
    for i in range(len(word)):
        if word[i].isnumeric():
            digits.append(word[i])
        else:
            for key in num_words:
                if word[i:i+len(key)] == key:
                    digits.append(num_words[word[i:i+len(key)]])
    return digits


main()