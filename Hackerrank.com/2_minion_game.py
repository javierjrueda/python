def minion_game(string):
    #variables para el bucle de substrings
    i = 0
    f = 1
    l = len(string)
    scoreb = 0
    scorea = 0

    #Generación de substrings
    while i < l+1:
        while f < l+1:
            substring = string[i:f]
            
            
            if len(substring) > 0:
                first = substring[0]

                #Detectamos si la primera letra de la substring es vocal o consonante
                if first in ('AEIOU'):
                    scorea += 1
                    print (substring)
                    print (txta.format(scorea)) 
                
                else:
                    scoreb += 1
                    txtb = "Stuart {}"
                    print (substring)
                    print (txtb.format(scoreb))
                f += 1
            else:
                f += 1
        
        #Reiniciamos la variable f y sumamos la variable i
        f = 1
        i += 1 
    
    if scorea > scoreb:
        txta = "Kevin {}"
        print (txta.format(scorea))
    else:
        txtb = "Stuart {}"
        print (txtb.format(scoreb))
 

if __name__ == '__main__':
    s = input()
    minion_game(s)