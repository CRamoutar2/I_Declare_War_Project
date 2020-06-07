import random
def shuffled_deck(): 
  basic_deck = list(range(2, 15)) * 2
  random.shuffle(basic_deck)
  return basic_deck
#function name: Shuffled Deck
#arguements: Two strings
#Purpose of line:
  #18 and 19 - Ask the players for their names
  #21 and 22 - The lists that holds each player's points
  #23 to 55 - Draws a card for each player, determines if one card is greater than another then proceeds to allocate score to the player of the winning round. Continue drawing cards for each player until the deck runs out of cards.
  #55 to 60 - Decides and prints out the winner of the game overall.


a = shuffled_deck()
player_1 = input("Please enter player 1's name: ")
player_2 = input("Please enter player 2's name: ")
print("The one with the highest points win")
list_1 = []
list_2 = []
while len(a) > 0:
  x = random.choice(a)
  print(player_1 + " got " + str((x)))
  a.remove(x)
  y = a.pop()
  print(player_2 + " got " + str((y)))
  if x > y:
    list_1.append(1)
    print("SCORE: " + player_1 + " has " + str(len(list_1)) + " and " + player_2 + " has " + str(len(list_2)))
  elif y > x:
    list_2.append(1)
    print("SCORE: " + player_1 + " has " + str(len(list_1))  + " and " + player_2 + " has " + str(len(list_2)))
  elif x == y:
    if a == 0 or a == 1:
      print("We are out of cards!")
      if len(list_1) > len(list_2):
        print(player_1 + " wins")
      elif len(list_2) > len(list_1):
        print(player_2 + " wins")
      elif len(list_1) == len(list_2):
        print("Tie")
    else:
      m = random.randint(2, 13)
      print(player_1 + " got " + str((m)))
      n = random.randint(2, 13)
      print(player_2 + " got " + str((n)))
      if m > n:
        list_1.append(1)
        print("SCORE: " + player_1 + " has " + str(len(list_1)) + " and " + player_2 + " has " + str(len(list_2)))
      elif n > m:
        list_2.append(1)
        print("SCORE: " + player_1 + " has " + str(len(list_1))  + " and " + player_2 + " has " + str(len(list_2)))
if len(list_1) > len(list_2):
  print(player_1 + " wins")
elif len(list_2) > len(list_1):
  print(player_2 + " wins")
elif len(list_1) == len(list_2):
  print("TIE")
