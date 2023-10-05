# Python program that can answer any “Yes” or “No” question 
# with a different fortune each time it executes.

import random 

name = " " # put your name 
question = "Is it raining?" # assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball
answer = "" 

 # Generating random number
random_number = random.randint(1, 9)
# print(random_number)

# 9 possible answers for Magic 8-Ball
if random_number == 1:
  print("Yes - definitely.")
elif random_number == 2:
  print("It is decidedly so.")  
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:  
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Outlook not so good.")
elif random_number == 9:
  print("Very doubtful.")
else:
  print("Error")

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)