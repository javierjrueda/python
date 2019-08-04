def minion_game(string):
  S_length = len(s)
  player1, player2 = 0,0

  for i in range(S_length):
      if s[i] in "AEIOU":
          player1 += S_length - i
      else:
          player2 += S_length - i   

     
          
  if player1 > player2:
      print ("Kevin", player1)
  elif player1 < player2:
      print ("Stuart", player2)
  else:
      print ("Draw")

if __name__ == '__main__':