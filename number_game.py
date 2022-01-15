
login_ids = {'Kalash7151970@yahoo.com':'Kalash@123'}


dictionary_students = {'Kalash','Glenn','Jeffery','Ambrose','Mikhail','Capablanca','Lasker','Morphy','Steinitz'}
dictionary_numbers = {10 , 12 , 11, 13 ,14 , 15, 16, 17, 18, 19, 20}



login = input('Your username - ')
password = input('Your password - ')





def act2():
    nameToShow=input('Which name do you choose? ')
    if nameToShow in dictionary_students:
        print('You\'re a genius...'.title())

    else:
        print('You\'re a fool...'.title())
        exit()

def act3():
    numToEnter = int(input('Enter the Number (11-20 only) - '))
    if numToEnter in dictionary_numbers:
        print('You\'re doing good job..')
    else:
        print('Fool you! leave the world immediately...'.title())
        exit()

def act4():
    nameToEnter=input('Who will you want to remove from your life? ')
    if nameToEnter in dictionary_students:
        del nameToEnter

    print('Hurray! you\'ve removed one of your enemies from the world..'.title())


def act5():
    print(dictionary_numbers)
    
    numToMean=input('Calculate the mean? ')
    
    means = '15'
    
    if means in numToMean:
        if numToMean == '15':
            print('You\'re a Good person, you can Become An engineer someday!!..'.title())

    
    else:
        print('Get bloody out of here you fool, a load on earth..'.title())






def kalash1():
        
    print("""
    [1] - Welcome, to my profile...
    [2] - What do you want to do?
    """)
    print("""
       ---  Only 1 to 5 keys will work.---
     ---    Press 'you' to exit..
    """)
    
    
    act1 = input("Press the keys to continue - ")
    
    if act1 == '1':
        act2()
    elif act1 == '2':
        act3()
    elif act1 == '3':
        act4()
    elif act1 =='4':
        act5()
    elif act1 == '5':
            
            num1 = int(input('Write A number to Calculation - '.title()))
            num2 = int(input('Write second number to calculate - '.title()))
            act_1=input('a for add, B for sub, c for multiply and d for divide - ')
            if act_1 == 'a':
                print('Sum of your numbers is ',num1+num2,'...')
            elif act_1=='b':
                print('Subtration of your numbers is ',num1-num2,'...')
            elif act_1=='c':
                print('Multiply of your numbers is ',num1*num2,'...')
            elif act_1 == 'd':
                print('Division of your numbers is ',num1/num2,'...')
    elif act1 == 'you':
                exit()
    else:
        print("Program Won't run if you don't show the spirit to play...".center())



if login in login_ids:
    
    if login_ids[login] == password:
        
        while True:
            
            kalash1()
            
            break
    
    else:
        
        print('Wrong Password, try again...')
        
        exit()

else:
    
    print('''Do you think it\'s a joke you fool!,

I\'ll get FBI involved in this for your non co-operating behaviour...

Type your very own UserName!...

Got it!! Better get it!.''')



