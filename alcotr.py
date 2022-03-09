#from typing import List
#python3
timesToBeExecuted = 5 #used in functions to determine if they have to be executed
# string variables
greetings = 'Hi,'
name = 'Alberto'
hugeText = 'Hey this is a text, please type a word that is contained here'
multilineText = '''
                   This is a multiline text
                    created from the variables  
                '''
veryClose = str('Very close')
rightWord = str('Well done!!')
wrongWord = str('try again!!')
secretWord = str("master")
passwordYey = str('that was the secret password, you won')
passwwordKey = str("admin")
positiveAnswer = ['y', 'Y', 'yes', 'Yes', 'YES', 'sure', 'yep', 'si']

# functions
def passwordyeyprint():
    for x in passwordYey:
        print(x)


def game1():
    def excerciseA():
        if value1 in hugeText:
            print(rightWord)
        else:
            if secretWord in value1:
                passwordyeyprint()
            else:
                if passwwordKey in value1:
                    print(passwwordKey[0], ' ', passwwordKey[1], ' ', passwwordKey[2], ' ', passwwordKey[3], ' ',
                          passwwordKey[4])
                else:
                    print(wrongWord)
    i = 1
    while i < timesToBeExecuted:
        print(hugeText)
        value1 = input('type a value here --')
        excerciseA()
        if passwwordKey in value1:
            break
        i += 1


def game2():
    def excersiceB():
        # numerical variables
        a = int(input('Add a number here        -- '))
        b = int(input('add a second number here -- '))
        c = int(input('add a third number here  -- '))
        d = (a + b - c)
        print(d)
    for x in range(6):
        excersiceB()


def greeting():
    print(greetings + " my name is ", name)
    yourName = input('what is your name? ')
    print('Nice to meet you ', yourName +' lets play a game')
    print('are you ready?')
    answer =  input()
    if answer in positiveAnswer:
        game1()


#FIrst things first
greeting()
game2()










