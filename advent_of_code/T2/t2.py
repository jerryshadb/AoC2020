
a = list()
part1 = 0
part2 = 0
with open("advent_of_code/T2/t2_input.txt", 'rb') as f:
    lines = [line.decode("utf-8") for line in f.readlines()]

for line in lines:
    line = line.split(" ")
    ranges = line[0]
    low = int(ranges.split("-")[0])
    high = int(ranges.split("-")[1])            #parsitaan tehtävädatasta tarvittavat rajat ratkaisulle jeejee String-manipulointia kärsimykseni on sanoinkuvaamaton 
    letter = line[1].strip(":")
    password = line[2].strip("")
    counter = 0

    for x in range (len(password)):
        if password[x] == letter:                   ##Part 1 
            counter += 1
    if counter >= low and counter <= high:
        part1 += 1
        
    if letter == password[low - 1] or letter == password[high-1]:
        if password[low-1] != password[high-1]:                    ##Part 2
            part2 += 1
            
print(f"Part1 solution: {part1}")
print(f"Part2 solution: {part2}")
        

