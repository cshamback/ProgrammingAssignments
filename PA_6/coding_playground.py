# I might have overcooked on this question on codedex so i wanted to share with you guys. have fun.

import time

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Welcome to Hogwarts, First Years! Let's find out what house you belong to. \n")

print("But first the Sorting Hat will need to ask you some questions to see where you belong.")

time.sleep(2)

while True:
  q1 = input(
    "\n🧙‍♂️: Do you like Dawn or Dusk?\n"
    "  1) Dawn \n"
    "  2) Dusk \n\n"
    "Your answer: "
    ).strip().lower()
  if q1 == "1" or q1 == "dawn":
    Gryffindor += 1
    Ravenclaw += 1
    time.sleep(1)
    print("\n🧙‍♂️: Ahhh interesting, morning person eh?")
    time.sleep(1)
    break
  elif q1 == "2" or q1 == "dusk":
    Hufflepuff += 1
    Slytherin += 1
    time.sleep(1)
    print("\n🧙‍♂️: Hmmm, one with the darkness...")
    time.sleep(1)
    break
  else:
    print("\n🧙‍♂️: Please input either '1' or '2' or type in dawn or dusk.")

while True:
  q2 = input(
    "\n🧙‍♂️: When I'm dead, I want people to remember me as?\n"
    "  1) The Good \n"
    "  2) The Great \n"
    "  3) The Wise \n"
    "  4) The Bold \n\n"
    "Your answer: "
    ).strip().lower()
  if q2 == "1" or q2 == "The Good":
    Hufflepuff += 2
    time.sleep(1)
    print("\n🧙‍♂️: The Good? Are you sure you're 'good'?")
    time.sleep(1)
    break
  elif q2 == "2" or q2 == "The Great":
    Slytherin += 2
    time.sleep(1)
    print("\n🧙‍♂️: I sense a pride and ego...")
    time.sleep(1)
    break
  elif q2 == "3" or q2 == "The Wise":
    Ravenclaw += 2
    time.sleep(1)
    print("\n🧙‍♂️: Smarty pants eh? You'll be tested here at Hogwarts for sure.")
    time.sleep(1)
    break
  elif q2 == "4" or q2 == "The Bold":
    Gryffindor += 2
    time.sleep(1)
    print("\n🧙‍♂️: So you think you've gotta pair on ya? We'll see.")
    time.sleep(1)
    break
  else:
    print("\n🧙‍♂️: Answer the question correctly. It's an easy 1, 2, 3, 4 or say the phrase. Gah are you actually a muggle?")

while True:
  q3 = input(
    "\n🧙‍♂️: Which kind of instrument pleases your ear the most?\n"
    "  1) The violin \n"
    "  2) The trumpet \n"
    "  3) The piano \n"
    "  4) The drum \n\n"
    "Your answer: "
    ).strip().lower()
  if q3 == "1" or q3 == "The violin":
    Slytherin += 4
    time.sleep(1)
    print("\n🧙‍♂️: Classical, you have rich ears huh?\n")
    time.sleep(1)
    break
  elif q3 == "2" or q3 == "The trumpet":
    Hufflepuff += 4
    time.sleep(1)
    print("\n🧙‍♂️: Loud, but not too loud. Odd choice out of the four.\n")
    time.sleep(1)
    break
  elif q3 == "3" or q3 == "The piano":
    Ravenclaw += 4
    time.sleep(1)
    print("\n🧙‍♂️: Peaceful, a calm soul you must have.\n")
    time.sleep(1)
    break
  elif q3 == "4" or q3 == "The drum":
    Gryffindor += 4
    time.sleep(1)
    print("\n🧙‍♂️: Bloody Hell, okay, I get ya.\n")
    time.sleep(1)
    break
  else:
    print("\n🧙‍♂️: Answer the question correctly. It's an easy 1, 2, 3, 4 or say the phrase. Gah are you actually a muggle?")

house_scores = [Gryffindor, Ravenclaw, Hufflepuff, Slytherin]
house_names = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

max_index = house_scores.index(max(house_scores))

print("🧙‍♂️: Let me think", end="", flush=True)
for _ in range(3):
    time.sleep(0.8)
    print(".", end="", flush=True)
print()  # new line
time.sleep(1)
print(f"🧙‍♂️: You belong in... {house_names[max_index]}!")