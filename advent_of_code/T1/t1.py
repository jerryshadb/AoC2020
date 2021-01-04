
def part1():
    with open("advent_of_code/T1/t1_input.txt", 'r') as f:
        syöte = [int(x) for x in f.readlines()]
    
    for x in syöte:
        for y in syöte:
            if x + y == 2020:
                return x * y

def part2():
    with open("advent_of_code/T1/t1_input.txt", 'r') as f:
        syöte = [int(x) for x in f.readlines()]
    
    for x in syöte:
        for y in syöte:
            for j in syöte:
                if x + y + j== 2020:
                    return x * y * j

print(f"Part 1 solution: {part1()}")
print(f"Part 2 solution: {part2()}")