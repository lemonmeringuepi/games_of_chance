import random

money = 100

def coin_flip(bet, guess):
  if bet <= 0:
    print("Please place a bet.")
    return 0
  if bet > money:
    print("You bet $" + str(bet) + ". You don't have enough money.")
    return 0
  if guess != "heads" and guess != "tails":
    print("Please guess heads or tails.")
    return 0
  num = random.randint(1,2)
  print("******************\nLet's flip a coin!\n******************\nYou guessed " + guess + ".")
  if num == 1:
    print("Heads!")
  elif num == 2:
    print("Tails!")
  if (num == 1 and guess == "heads") or (num == 2 and guess == "tails"):
    print("You win! $" + str(bet) + " has been credited to your account.")
    return bet
  else:
    print("You lost. $" + str(bet) + " has been removed from your account.")
    return -bet
  
def cho_han(bet, guess):
  if bet <= 0:
    print("Please place a bet.")
    return 0
  if bet > money:
    print("You bet $" + str(bet) + ". You don't have enough money.")
    return 0
  if guess != "odd" and guess != "even":
    print("Please guess odd or even.")
    return 0
  num1 = random.randint(1,6)
  num2 = random.randint(1,6)
  if (num1 + num2) % 2 == 1:
    result = "odd"
  if (num1 + num2) % 2 == 0:
    result = "even"
  print("******************\nLet's play Cho-Han!\n******************\nYou guessed " + guess + ".\nThe dealer rolled " + str (num1) + " and " + str(num2) + ".\nThat's " + result + "!")
  if result == guess:
    print("You win! $" + str(bet) + " has been credited to your account.")
    return bet
  if result != guess:
    print("You lost. $" + str(bet) + " has been removed from your account.")
    return -bet
  
def draw_card(bet):
  if bet <= 0:
    print("Please place a bet.")
    return 0
  if bet > money:
    print("You bet $" + str(bet) + ". You don't have enough money.")
    return 0
  deck = [["One of Hearts", 1], ["Two of Hearts", 2], ["Three of Hearts", 3], ["Four of Hearts", 4], ["Five of Hearts", 5], ["Six of Hearts", 6], ["Seven of Hearts", 7], ["Eight of Hearts", 8], ["Nine of Hearts", 9], ["Ten of Hearts", 10], ["Jack of Hearts", 11], ["Queen of Hearts", 12], ["King of Hearts", 13], ["Ace of Hearts", 14], ["One of Spades", 1], ["Two of Spades", 2], ["Three of Spades", 3], ["Four of Spades", 4], ["Five of Spades", 5], ["Six of Spades", 6], ["Seven of Spades", 7], ["Eight of Spades", 8], ["Nine of Spades", 9], ["Ten of Spades", 10], ["Jack of Spades", 11], ["Queen of Spades", 12], ["King of Spades", 13], ["Ace of Spades", 14], ["One of Diamonds", 1], ["Two of Diamonds", 2], ["Three of Diamonds", 3], ["Four of Diamonds", 4], ["Five of Diamonds", 5], ["Six of Diamonds", 6], ["Seven of Diamonds", 7], ["Eight of Diamonds", 8], ["Nine of Diamonds", 9], ["Ten of Diamonds", 10], ["Jack of Diamonds", 11], ["Queen of Diamonds", 12], ["King of Diamonds", 13], ["Ace of Diamonds", 14], ["One of Clubs", 1], ["Two of Clubs", 2], ["Three of Clubs", 3], ["Four of Clubs", 4], ["Five of Clubs", 5], ["Six of Clubs", 6], ["Seven of Clubs", 7], ["Eight of Clubs", 8], ["Nine of Clubs", 9], ["Ten of Clubs", 10], ["Jack of Clubs", 11], ["Queen of Clubs", 12], ["King of Clubs", 13], ["Ace of Clubs", 14], ["Joker", 15], ["Joker", 15]]
  num1 = random.randint(1,52)
  num2 = random.randint(1,51)
  card1 = deck.pop(num1)
  card2 = deck.pop(num2)
  print("******************\nLet's draw cards!\n******************\nYou drew " + card1[0] + ".\nThe computer drew " + card2[0] + ".")
  if card1[1] > card2[1]:
    print("You win! $" + str(bet) + " has been credited to your account.")
    return bet
  elif card1[1] == card2[1]:
    print("It's a tie! Your bet has been returned to you.")
    return 0
  else:
    print("You lost. $" + str(bet) + " has been removed from your account.")
    return -bet
  
def roulette(bet, guess):
  if bet <= 0:
    print("Please place a bet.")
    return 0
  if bet > money:
    print("You bet $" + str(bet) + ". You don't have enough money.")
    return 0
  error_message = """
  Please place a bet. Acceptable bets are as follows:
  "red"
  "black"
  "00"
  Any number between 0 and 36, without quotation marks
  "row"
  "basket"
  "first column"
  "second column"
  "third column"
  "first dozen"
  "second dozen"
  "third dozen"
  "odd"
  "even"
  "1 to 18"
  "19 to 36"
  "split 1 4" (or split plus the two adjacent numbers to split, the lower number going first, eg "split 7 8" or "split 28 31")
  "street 1" (or street plus any first number of a row, eg "street 7" or "street 34")
  "six line 1" (or six line plus any first number of a set of two consecutive rows, eg "six line 10" or "six line 31")
  "corner 1 2 4 5" (or corner plus the four surrounding numbers, ordered top left, top right, bottom left, bottom right)
  "snake"
  """
  string_guesses = ["red", "black", "00", "row", "black", "basket", "first_column", "second column", "third column", "first dozen", "second dozen", "third dozen", "odd", "even", "1 to 18", "19 to 36", "street 1", "street 4", "street 7", "street 10", "street 13", "street 16", "street 19", "street 22", "street 25", "street 28", "street 31", "street 34", "snake", "six line 1", "six line 4", "six line 10", "six line 13", "six line 16", "six line 19", "six line 22", "six line 25", "six line 28", "six line 31", "corner 1 2 4 5", "corner 2 3 5 6", "corner 4 5 7 8", "corner 5 6 8 9", "corner 7 8 10 11", "corner 8 9 11 12", "corner 10 11 13 14", "corner 11 12 14 15", "corner 13 14 16 17", "corner 14 15 17 18", "corner 16 17 19 20", "corner 17 18 20 21", "corner 19 20 22 23", "corner 20 21 23 24", "corner 22 23 25 26", "corner 23 24 26 27", "corner 25 26 28 29", "corner 26 27 29 30", "corner 28 29 31 32", "corner 29 30 32 33", "corner 31 32 34 35", "corner 32 33 35 36", "split 1 2", "split 1 4", "split 2 3", "split 2 5", "split 3 6", "split 4 5", "split 4 7", "split 5 6", "split 5 8", "split 6 9", "split 7 10", "split 7 8", "split 8 9", "split 8 11", "split 9 12", "split 10 11", "split 10 13", "split 11 12", "split 11 14", "split 12 15", "split 13 14", "split 13 16", "split 14 15", "split 14 17", "split 15 18", "split 16 17", "split 16 19", "split 17 18", "split 17 20", "split 18 21", "split 19 20", "split 19 22", "split 20 21", "split 20 23", "split 21 24", "split 22 23", "split 22 25", "split 23 24", "split 23 26", "split 24 27", "split 25 26", "split 25 28", "split 26 27", "split 26 29", "split 27 30", "split 28 29", "split 28 31", "split 29 30", "split 29 32", "split 30 33", "split 31 32", "split 31 34", "split 32 33", "split 32 35", "split 33 36", "split 34 35", "split 35 36"]
  if type(guess) is str and guess not in string_guesses:
    print(error_message)
    return 0
  if type(guess) is int and (guess < 0 or guess > 36):
    print(error_message)
    return 0
  result = random.randint(-1,36)
  if result == -1:
    result = "00"
  snake = [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]
  print("******************\nLet's play roulette!\n******************\nYou bet on " + str(guess) + ".\nThe marble landed on " + str(result) + ".")
  if guess == result:
    print("You win! $" + str(bet*35) + " has been credited to your account.")
    return bet*35
  elif guess == "row" and (result == "00" or result == 0):
    print("You win! $" + str(bet*17) + " has been credited to your account.")
    return bet*17
  elif guess == "basket" and (result == "00" or result <= 3):
    print("You win! $" + str(bet*6) + " has been credited to your account.")
    return bet*6
  elif guess == "snake" and result in snake:
    print("You win! $" + str(bet*2) + " has been credited to your account.")
    return bet*2
  elif result != "00" and result != 0:
    if (guess == "red" and (((result < 11 or 18 < result < 29) and result % 2 == 1) or ((10 < result < 19 or result > 28) and result % 2 == 0))) or (guess == "black" and (((result < 11 or 18 < result < 29) and result % 2 == 0) or (10 < result < 19 or result > 28) and result % 2 == 1)) or (guess == "odd" and result % 2 == 1) or (guess == "even" and result % 2 == 0) or (guess == "1 to 18" and result <= 18) or (guess == "19 to 36" and result >= 19):
      print("You win! $" + str(bet) + " has been credited to your account.")
      return bet
    elif (guess == "first column" and result % 3 == 1) or (guess == "second column" and result % 3 == 2) or (guess == "third column" and result % 3 == 0) or (guess == "first dozen" and 1 <= result <= 12) or (guess == "second dozen" and 13 <= result <= 24) or (guess == "third dozen" and 25 <= result <= 36):
      print("You win! $" +str(bet*2) + " has been credited to your account.")
      return bet*2
    elif guess[0:6] == "street":
      if len(guess) == 8 and (int(guess[7]) <= result <= (int(guess[7]) +2)):
        print("You won! $" + str(bet*11) + " has been credited to your account.")
        return bet*11
      elif len(guess) == 9 and (int(guess[7]+guess[8]) <= result <= (int(guess[7]+guess[8]) + 2)):
        print("You won! $" + str(bet*11) + " has been credited to your account.")
        return bet*11
      else:
        print("You lost. $" + str(bet) + " has been removed from your account.")
        return -bet
    elif guess[0:8] == "six line":
      if len(guess) == 10 and (int(guess[-1]) <= result <= (int(guess[-1]) + 5)):
        print("You won! $" + str(bet*5) + " has been credited to your account.")
        return bet * 5
      elif len(guess) == 11 and (int(guess[-2]+guess[-1]) <= result <= (int(guess[-2]+guess[-1]) + 5)):
        print("You won! $" + str(bet*5) + " has been credited to your account.")
        return bet*5
      else:
        print("You lost. $" + str(bet) + " has been removed from your account.")
        return -bet
    elif guess[0:6] == "corner":
      if len(guess) == 14 and (result == int(guess[7]) or result == int(guess[9]) or result == int(guess[11]) or result == int(guess[13])):
        print("You won! $" + str(bet*8) + " has been credited to your account.")
        return bet*8
      elif len(guess) == 16 and (result == int(guess[7]) or result == int(guess[9]) or result == int(guess[11]+guess[12]) or result == int(guess[14]+guess[15])):
        print("You won! $" + str(bet*8) + " has been credited to your account.")
        return bet*8
      elif len(guess) == 18 and (result == int(guess[7]+guess[8]) or result == int(guess[10]+guess[11]) or result == int(guess[13]+guess[14]) or result == int(guess[16]+guess[17])):
        print("You won! $" + str(bet*8) + " has been credited to your account.")
        return bet*8
      else:
        print("You lost. $" + str(bet) + " has been removed from your account.")
        return -bet
    elif guess[0:5] == "split":
      if len(guess) == 9 and (result == int(guess[-1]) or result == int(guess[-3])):
        print("You won! $" + str(bet*17) + " has been credited to your account.")
        return bet*17
      elif len(guess) == 10 and (result == int(guess[-2]+guess[-1]) or result == int(guess[-4])):
        print("You won! $" + str(bet*17) + " has been credited to your account.")
        return bet*17
      elif len(guess) == 11 and (result == int(guess[-2]+guess[-1]) or result == int(guess[-5]+guess[-4])):
        print("You won! $" + str(bet*17) + " has been credited to your account.")
        return bet*17
      else:
        print("You lost. $" + str(bet) + " has been removed from your account.")
        return -bet
    else:
      print("You lost. $" + str(bet) + " has been removed from your account.")
      return -bet
  else:
    print("You lost. $" + str(bet) + " has been removed from your account.")
    return -bet
    
#Call your game of chance functions here
money += coin_flip(10, "tails")
money += cho_han(10, "even")
money += draw_card(20)
money += roulette(60, "split 35 36")

print("\nYou have $" + str(money) + " in your account.")