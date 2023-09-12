'''''Caesar Cipher'''''

'''
Gaius Julius Caesar used ciphers so that important information, such as the location of a attack or the date it would be carried out,
would be unknown to enemies but know to the rest of his troop.
If his messages were ever intercepted, the enemy would't immediately understand what the cipher meant.
'''

'''
Imagine Alice and Bob decided to communicate using the Caesar
Cipher First, they would need to agree in advance on a shift
to use-- say, three.
So to encrypt her message, Alice would
need to apply a shift of three to each letter in her original message.
So A becomes D, B becomes E, C becomes F, and so on. This is known as Caesar Cipher.
By the way, it took 800 years to crack the caesar cipher :3
'''

def caesar_cipher(a):
  encript=''
  for i in a:
    if 48<=ord(i)<=57 or 65<=ord(i)<=90 or 97<=ord(i)<=122:

      if ord(i)==57:
          encript+=chr((ord(i)-9)+2)
      elif ord(i)==56:
        encript+=chr((ord(i)-8)+1)
      elif ord(i)==55:
        encript+=chr(ord(i)-7)
      elif ord(i)==90 or ord(i)==122:
          encript+=chr((ord(i)-25)+2)
      elif ord(i)==89 or ord(i)==121:
        encript+=chr((ord(i)-24)+1)
      elif ord(i)==88 or ord(i)==120:
        encript+=chr(ord(i)-23)

      else:
        encript+=chr(ord(i)+3)

    else:
      encript+=i

  return encript


b=caesar_cipher(input("Insert your message here: "))
print()
print("Your encrypted messege:")
print(b)
