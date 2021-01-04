
#part one
#For-loopilla mennään inputin loppua kohti, aina pykälä kerrallaan (parametri "down"). 
#tarkastetaan, onko input-listan kohdassa sijainti puuta. Jos on, inkrementoidaan puulaskuri. Sitten lisätään sijaintiin 3 (parametri "right") eli montako pykälää mennään "mäessä" oikealle
#jatketaan tätä niin kauan, kunnes lista on käyty läpi. ts "mäki laskettu". Lopussa tarkastetaan vielä jäljelle jäänyt kohta.
# eli mennään siis yksi alas, kolme oikalle. yksi alas, kolme oikealle kunnes koko mäki on laskettu = lista luettu 
def day3teht1(right=3, down=1):
    sijainti = 0
    puidenMaara = 0
    with open('advent_of_code/T3/t3_input.txt') as f:      
        lines = f.readlines()
        for i in range(0, len(lines), down):
            line = lines[i].strip()
            if '#' == line[sijainti]:
                puidenMaara += 1
            sijainti += right
            sijainti = sijainti % len(line)

    return puidenMaara

#part 2
#Varmaan suht itsestäänselvä. 
def day3teht2():
    return day3teht1(1,1) * day3teht1(5,1) * day3teht1(7,1) * day3teht1(1,2) * day3teht1()


    
print(f"Part 1 solution: {day3teht1()}")
print(f"Part 2 solution: {day3teht2()}")
