import statistics as s


admins = {'Python': 'password123@', 'user2':'pass2@123'}


stu1={		 'Kalash':[76,87,98],
             'Sahil':[92,89,98],
             'Arush':[87,90,86],
             'Bhavesh':[78,89,76],
             'Vishesh':[67,76,77]
             }



def entgrs():
    nte= input('Student name:  ')
    gradeToEnter = input('Grade:  ')

    if nte in stu1:
        print('Adding Grade...')
        stu1[nte].append(float(gradeToEnter))
    else:
        print('Student does not exist.')


    print(stu1)
    


def rstu():
    ntr= input('What student to remove?:  ')
    if ntr in stu1:
        print('Removing student...')
        del stu1[ntr]
    print(stu1)


def stavs():
    for stu in stu1:
        grLs = stu1[stu]
        avgg = s.mean(grLs)


        print(stu,'has an average grade of:',avgg)




def main():


    print("""
Welcome to Grade Central
[1] - Enter Grade
[2] - Remove Student
[3] - Studet Average Grades
[4] - Exit
""")


    action = input('What would you like to do today? (Enter a number) ')


    if action == '1':
        entgrs()
    elif action == '2':
        rstu()
    elif action == '3':
        stavs()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again')

        

login = input('Username: ')
password = input('Your Password: ')


if login in admins:
    if admins[login]== password:
        print('Welcome,', login)
        while True:
            main()
    else:
        print('Invalid Password, will detonate in 5 seconds!')
else:
    print('Invalid username, calling the FBI to report this..')



# practice through simplilearn..
