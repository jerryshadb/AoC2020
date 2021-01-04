

def t5():
    with open("advent_of_code/T5/t5_input.txt", 'r') as f:
        liput = [x.replace("\n", " ").strip() for x in f.readlines()]  
    
    paikkaNumerot = list()
    for rivi in liput:
        
        r = rivi[:7]
        alku = 0
        loppu = 127
        row, col = 0, 0

        for char in r:
            if char == "F":
                loppu = int((alku + loppu + 1)/2) - 1      
            elif char == "B":
                alku = int((alku + loppu + 1)/2)

        row = alku

        r = rivi[7:]

        alku = 0
        loppu = 7

        for char in r: 
            if char == "L":
                loppu = ((alku + loppu + 1)/2) - 1
            elif char == "R":
                alku = ((alku + loppu +1 )/2)

        col = alku

        paikkaNro = row * 8 + col
        paikkaNumerot.append(paikkaNro)
    
    paikkaNrotJärjestyksessa = sorted(paikkaNumerot)
    puuttuvaID = 0

    for i in range(int(min(paikkaNumerot)), int(max(paikkaNumerot)+1)):
        if i != paikkaNrotJärjestyksessa[int(i-min(paikkaNumerot))-1]:
            puuttuvaID = i
    return max(paikkaNumerot), puuttuvaID



print(t5())
