#numerical variables
a = int()
b = int()
c = int()
d = int(a+b+c)
#string variables
name = 'Alberto'
greetings = 'Hi,'

hugeText = 'Hey this is a text, please type a word that is contained here'

multilineText = '''
This is a multiline text
created from the variables
'''
shortText = str('short text')


rightWord = str('that word is here :)')
wrongWord = str('that word does not appear in the text')
secretword = str("master")
passwordYey = str('that is the secret pasword, you won')
adminkey = str("admin")

#funtions
def greeting():
    print(greetings + " my name is ", name)
greeting()
def operation():
    print(d)
def passwordYeyPrint():
    for x in passwordYey:
        print(x)
def excercise():
    if value1 in hugeText:
        print(rightWord)
    #if value1 not in hugeText:
    else:
        if secretword in value1:
            passwordYeyPrint()
        else:
            if adminkey in value1:
                print(adminkey[0], ' ', adminkey[1], ' ', adminkey[2], ' ', adminkey[3], ' ', adminkey[4])
            else:
                print(wrongWord)

#first excercise
print(hugeText)
value1 = input('type a value here --')
excercise()
