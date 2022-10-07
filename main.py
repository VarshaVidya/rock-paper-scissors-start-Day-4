# Day 4
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
r_p_s = [rock,paper,scissors]
ur_input = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))
print(r_p_s[ur_input])
print("Computer chose ")
comp_choice= random.randint(0,2)
print(r_p_s[comp_choice])

if ur_input == comp_choice:
  print("Draw")
else:
  if ur_input == 0:
    if comp_choice == 1:
      print("You Lose")
    else:
      print("You Win")
  if ur_input==1:
    if comp_choice == 2:
      print("You Lose")
    else:
      print("You Win")
  if ur_input==2:
    if comp_choice == 0:
      print("You Lose")
    else:
      0
      print("You Win")
  
    

    

  




