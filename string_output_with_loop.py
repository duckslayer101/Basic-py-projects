#This code is for SMALL LETTERS only. In this py project you will be in a loop until your message/sentence are not found. Enjoy! 

def into_the_loopWego(sentence):
    lsentence=sentence.lower()
    constline=''
    finaline=''
    midline=''
    smalla=97
    for i in lsentence:
        if ord('a')<=ord(i)<=ord('z'):
            while True:
                if chr(smalla)!=i:
                    constline=chr(smalla)
                    smalla+=1
                    midline=finaline[:len(finaline)]+constline
                    print(midline)
                else:
                    finaline+=i
                    print(finaline)
                    break
            smalla=97

        else:
            finaline+=i
            print(finaline)
               
a=input("Enter your sentence: ")
into_the_loopWego(a)
