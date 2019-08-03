def minion_game(string):
    mb = "Stuart"
    ma = "Kevin"
    vocal = ['a','e','i','o','u']
    
    #Generamos la primera substring
    substring = string[0]
    word = substring.lower()
    
    #Detectamos si la primera letra de la substring es vocal o consonante
    first = word[0]
    if first == "a" or "e" or "i" or "o" or "u": 
        score = string.count(word)
        print (score)
    else:
        print ("Consonant")

    #len()
    #startswith()
    #strip()
    #count()



if __name__ == '__main__':
    s = input()
    minion_game(s)