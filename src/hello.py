def summ(num1,num2):
    return num1+num2

def div(num1,num2):
    if num2<0:
        print('probleme you cannot divid with 0')
    else:
        return num1/num2 

def multip(num1,num2):
    return num1*num2 

def sus(num1,num2):
    return num1-num2

def math(num1,num2):
    choix=int(input('give me your choix 1 -> sum / 2 -> div / 3 -> multip / 4 -> sus'))
    match choix :
        case 1: 
                value=summ(num1,num2) 
                print(value)
        case 2: 
                value=div(num1,num2)
                print(value)
        case 3: 
                value=multip(num1,num2)
                print(value)
        case 4: 
                value=sus(num1,num2)
                print(value)
        case _: print('goodby')


num1=int(input('give me first value'))
num2=int(input('give me 2 value'))
math(num1,num2)