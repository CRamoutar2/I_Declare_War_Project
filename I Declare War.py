import random
def shuffled_deck():
  basic_deck = list(range(2,15))*2
  random.shuffle(basic_deck)
  return basic_deck

#Function_Name: I_Declare_war
#Arguements: None
#Purpose: If a player want to play a game of I declare war, this function will provide them with the necessities.
#Lines 88-91: Asks for player input about if they want to play a game of I declare war.

def I_Declare_war():
  a = shuffled_deck()
  player_1 = input("Please enter player 1's name: ")
  player_2 = input("Please enter plauer 2's name: ")
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
          Game = input("Do you want to play another game of I declare war?: ")
          if Game == 'yes':
            I_Declare_war()
          else:
            print("Thank you for playing")
        elif len(list_2) > len(list_1):
          print(player_2 + " wins")
          Game = input("Do you want to play another game of I declare war?: ")
          if Game == 'yes':
            I_Declare_war()
          else:
            print("Thank you for playing")
        elif len(list_1) == len(list_2):
          print("Tie")
          Game = input("Do you want to play another game of I declare war?: ")
          if Game == 'yes':
            I_Declare_war()
          else:
            print("Thank you for playing")
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
    Game = input("Do you want to play another game of I declare war ")
    if Game == 'yes':
      I_Declare_war()
    else:
      print("Thank you for playing")
  elif len(list_2) > len(list_1):
    print(player_2 + " wins")
    Game = input("Do you want to play another game of I declare war ")
    if Game == 'yes':
      I_Declare_war()
    else:
      print("Thank you for playing")
  elif len(list_1) == len(list_2):
    print("TIE")
    Game = input("Do you want to play another game of I declare war ")
    if Game == 'yes':
      I_Declare_war()
    else:
      print("Thank you for playing")
Game = input("Do you want to play a game of I declare war?: ")
if Game == 'yes':
  I_Declare_war()
else:
  print("Thank you for playing")
