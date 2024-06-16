# Creating word dictionary
def CAPITAL_word_dictionary():
    dic = {}
    for i in range(65, 90+1):
        dic[chr(i)] = 0
    return dic
Counter = CAPITAL_word_dictionary()

# Word frequency tester
def Frequency_tester(sentence):
    for i in sentence:
        if i in Counter.keys():
            Counter[i] = Counter[i]+1
    return Counter

# Showing the result
def Show_frequency(result):
    print('The frequency results:')
    for key, value in result.items():
        print(f"{key} = {value} times.")
        print()



statements = input("The messages: ").upper()
Tester = Frequency_tester(statements)
print()
Show_frequency(Tester)