'''Morse Code Generator'''

'''
Morse code is a method used in telecommunication to encode text characters as standardized 
sequences of two different signal durations, called dots and dashes, or dits and dahs. 
Morse code is named after Samuel Morse, one of the inventors of the telegraph.
'''

'''
In the 'word_bag' variable, there are the morse codes. Only the space(' ') isn't the morse code here. 
For space( ) we get ' / ' , this is necessary for understanding the coded messages as it separates encoded words 
so that the user can understand their coded messege.
'''

WORD_BAG = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 
    'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 
    'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 
    'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',  '1':'.----', 
    '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...'
    , '8':'---..', '9':'----.', '0':'-----', '?':'..--..', '!':'-.-.--', '.':'.-.-.-', 
    ',':'--..--', ';':'-.-.-.', ':':'---...', '+':'.-.-.','-':'-....-', '/':'-..-.', 
    '=':'-...-', "'":'.----.', '"':'.-..-.', ')':'-.--.-', '(':'-.--.', ' ':' / '
    }

def generator(a):
  s=''
  for i in a:
    s+=WORD_BAG[i]+' '  #The extra space(' ') is for the space between letters in a word
  return s

b=input("Please give your statements: ").lower()
print("Your encoded message:")
print()
generator(b)
