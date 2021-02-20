import random

# game rules
rules = """
Welcome to 2 Dice 
Here are the rules.
The goal is to guess if the dice will roll under 6 or above it.
Pick a number from 1 through 12.
If you pick 6 then you only get a point if it lands on 6.
if pick any number under 6 or above you get a point.
If you pick the number the dice lands on then you get two points. 
"""
print(rules)

# need an input from player if its over 6 or under 6
answer = input("What is your bet number?:")
answer_int = int(answer)
dice = random.randint(1, 12)
# computer pick at random
import random
print("The dice rolled", dice)

# check to see if number is above 6 or under using nested if statments
low = [1,2,3,4,5,6]
high = [7,8,9,10,11,12]

if dice == answer_int:
  print("You get two points")
elif dice in low and answer_int in low:
  print("you got low")
elif dice in high and answer_int in high:
  print("you got high")
else:("what?")
#output number
#continue loop?
