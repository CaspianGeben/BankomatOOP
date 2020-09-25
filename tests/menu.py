main = ['1. Skapa Konto', '2. administrera', '3. Avsluta']
admin = ['1.deposit','2.withdraw', '3.balance', '4.return']
printMenu = main
menuChoice = 'main'
isRunning = True
while isRunning:
    for item in printMenu:
        print(item)
    if menuChoice == 'main':
        menuChoice = UserChoice()
        printMenu = main
    elif menuChoice == 'admin':
        menuChoice = UserChoice2()
        printMenu = admin
    if menuChoice == 'end':
        break
        
def UserChoice():
    userChoice = int(input('>'))

    if userChoice == 1:
        AddAccount()
        return 'main'
    elif userChoice == 2:
        return 'admin'
    elif userChoice == 3:
        return 'end'

def UserChoice2():
    userChoice = int(input('>'))

    if userChoice == 1:
        Deposit()
        return 'admin'
    elif userChoice == 2:
        WithDraw()
        return 'admin'
    elif userChoice == 3:
        Balance()
        return 'admin'
    elif userChoice == 4:
        return 'main'