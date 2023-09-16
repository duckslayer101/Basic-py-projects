import random
print("       rock,paper,scissors!       ")
print()


# 'r' for rock, 'p' for paper, 's' for scissors
pc=['r','p','s']


def game(user):
  bot=random.choice(pc)
  for i in bot:
    if i=='r':
      print('Bot gives: rock')
    elif i=='p':
      print('Bot gives: paper')
    else:
      print('ot gives: scissors')

  print()

  if user[0]==bot:
    print("It's a tie!")

  # 'r' beats 's', 's' beats 'p', 'p' beats 'r'
  elif (user[0]=='r' and bot=='s') or (user[0]=='s' and bot=='p') or (user[0]=='p' and bot=='r'):
    print("Congrats! You win.")

  else:
    print("You lost!")


'''
user has to input one of these three characters:
    1. rock
    2. paper
    3. scissors
'''

game(input("You give: "))
