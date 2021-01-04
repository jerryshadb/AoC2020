import re


#part1
def t4part1():
    with open("advent_of_code/T4/t4_input.txt",'r') as f:
        lista = f.read().split('\n\n') #muunnetaan tekstifilu listaksi, käsittelyn helpottamiseksi
        
        lista = [x.replace('\n', ' ').split() for x in lista] #muunnetaan listan datat omiksi listoikseen
        passit = list() #luodaan lista johon tiedot talletetaan hajautustauluina
    
        for hlö in lista:
            passit.append(dict(data.split(":") for data in hlö)) #lista hajautustauluja passien datoista.
    
    

        passit = [x for x in passit if len(x.keys()) == 8 or len(x) == 7 and 'cid' not in x.keys()] #tehtävänannon kriteerien mukaan, passi on ok jos siellä on vaadittu  data
                                                                                                    # CID (Country ID) sai kuitenkin puuttua, joten jos passissa on vain 7 tietoa ja puuttuva on CID
                                                                                                    # on passi edelleen ok. Muussa tapauksessa se ei ole ok.     

    return len(passit) #tehtävän vastaus eli listan passit jotka menee kriteereistä läpi 

 #part 2   
def t4part2():
    #häikäilemättömästi kopioidaan part1:n koodi säilyttääksemme jo-hyväksytyt passit
    with open("advent_of_code/T4/t4_input.txt",'r') as f:
        lista = f.read().split('\n\n') 
        
        lista = [x.replace('\n', ' ').split() for x in lista] 
        passit = list() 
    
        for hlö in lista:
            passit.append(dict(data.split(":") for data in hlö)) 
        passit = [x for x in passit if len(x.keys()) == 8 or len(x) == 7 and 'cid' not in x.keys()]
    #häikäilemättömyys lopppuu nyt.


        okPassit = list()

        for henkilö in passit:
            if (1920 <= int(henkilö['byr']) <= 2002
                and (2010 <= int(henkilö['iyr']) <= 2020)
                and (2020 <= int(henkilö['eyr']) <= 2030)
                and 
                ((henkilö['hgt'][-2:] == 'cm' and 150 <= int(henkilö['hgt'][:-2]) <= 193)
                or (henkilö['hgt'][-2:] == 'in' and 59 <= int(henkilö['hgt'][:-2]) <= 76))   #uusintarkastus uusin parametrein. 
                and (re.match(r'#[\da-f]{6}', henkilö['hcl']))
                and (henkilö['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
                and (re.match(r'\d{9}', henkilö['pid']))):
                okPassit.append(henkilö)
        return len(okPassit) - 1
print(f"Part 1 solution: {t4part1()}")
print(f"Part 2 solution: {t4part2()}")
                


