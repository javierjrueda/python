def minion_game(string):
    #variables para el bucle de substrings
    i = 0
    f = 1
    l = len(string)
    scoreb = 0
    scorea = 0
    kset ={""}
    sset ={""} 

    #Generación de substrings
    while i < l+1:
        while f < l+1:
            substring = string[i:f]
            if substring in kset or substring in sset:
              f += 1
            else:  
                if len(substring) > 0:
                    first = substring[0]

                    #Detectamos si la primera letra de la substring es vocal o consonante
                    if first in ('AEIOU'):
                        sset.add(substring)
                        scorea = scorea + string.count(substring)
                        #print(substring)
                        #txta = "Kevin +{}, total {}"
                        #print (txta.format(string.count(substring),scorea))
                        
                    else:
                        kset.add(substring)
                        scoreb = scoreb + string.count(substring)
                        #print(substring)
                        #txtb = "Stuart +{}, total {}"  
                        #print (txtb.format(string.count(substring),scoreb))

                f += 1
            
        
        #Reiniciamos la variable f y sumamos la variable i
        f = 1
        i += 1 
    
    if scorea > scoreb:
        txta = "Kevin {}"
        print (txta.format(scorea))
    elif scorea == scoreb:
        print ("Draw")
    else:
        txtb = "Stuart {}"
        print (txtb.format(scoreb))
 
 

if __name__ == '__main__':
    s = input()
    minion_game(s)

if __name__ == '__main__':