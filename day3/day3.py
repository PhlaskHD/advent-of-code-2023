def main():
    with open("input.txt") as file:
        content = file.read()
    
    split = content.splitlines()
    grid = []
    for each in split:
        grid.append(each)
    
    accounted_for = []
    total = 0
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].isdigit():
                if adjacency_checker(grid, y, x):
                    total += number_builder(grid, y, x, accounted_for)
                    accounted_for.append(f"{x}, {y}")
    
    print(total)

                    



def adjacency_checker(grid, y, x):
    height = len(grid)
    width = len(grid[y])
    if (
        (x-1 >= 0 and grid[y][x-1] != "." and grid[y][x-1].isdigit() == False) or 
        (x+1 < width and grid[y][x+1] != "." and grid[y][x+1].isdigit() == False) or 
        (y-1 >= 0 and grid[y-1][x] != "." and grid[y-1][x].isdigit() == False) or 
        (y+1 < height and grid[y+1][x] != "." and grid[y+1][x].isdigit() == False) or 
        (x-1 >= 0 and y+1 < height and grid[y+1][x-1] != "." and grid[y+1][x-1].isdigit() == False) or 
        (x+1 < width and y+1 < height and grid[y+1][x+1] != "." and grid[y+1][x+1].isdigit() == False) or 
        (x-1 >= 0 and y-1 >= 0 and grid[y-1][x-1] != "." and grid[y-1][x-1].isdigit() == False) or 
        (y-1 > 0 and x+1 < width and grid[y-1][x+1] != "." and grid[y-1][x+1].isdigit() == False)
    ):
        return True
    else:
        return False
    
def number_builder(grid, y, x, acct):
    width = len(grid[y])
    r = ""
    i = x
    while i > 0 and grid[y][i].isdigit():
        if f"{i}, {y}" in acct:
            return 0
        i -= 1
    if not grid[y][i].isdigit():
        i += 1
    start_index = i
    i = x
    while i < width - 1 and grid[y][i].isdigit():
        i += 1
    if not grid[y][i].isdigit():
        i -=1
    end_index = i
    for j in range(start_index, end_index+1):
        r += grid[y][j]
    return int(r)
        



main()