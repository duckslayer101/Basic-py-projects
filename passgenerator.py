import random
print("         '''Welcome to password generator'''        ")
print()
print()
chrs='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()<>?:,./;'
num=int(input("Enter the amount of password you want to create: "))
a=1

for i in range(num):
  passs=''
  len=int(input(f"Enter the length of {a} no. password: "))

  for j in range(len):
    passs+=random.choice(chrs)
  print(f"Your {a} no. password: {passs}")
  print()
  a+=1
