from classes import Bank 
from classes import Account
from datetime import datetime

bank = Bank()

def Main():
    while True:
        main = [
            '1. Skapa Konto',
            '2.deposit',
            '3.withdraw', 
            '4.balance',
            '5. Avsluta']
        for item in main:
            print(item)

        userChoice = int(input('>'))
        if userChoice == 1:
            AddAccount()
            continue
        elif userChoice == 2:
            Deposit()
            continue
        elif userChoice == 3:
            WithDraw()
            continue
        elif userChoice == 4:
            Balance()
            continue
        elif userChoice == 6:
            PrintAllAccounts()
            continue
        elif userChoice == 5:
            break
        

def AddAccount():
    accountNumber = int(input('Kontonummer:'))
    account = Account(accountNumber)
    print(account.GetAccountNumber())
    bank.AddAccount(account, accountNumber)

def Deposit():
    print('deposit')
    accountNumber = int(input('konto: '))
    amount = int(input('ta ut: '))
    date = datetime.now
    bank.AddTransaction(accountNumber,date,amount)

def WithDraw():
    print('withdraw')


def Balance():
    print('balance')

def PrintAllAccounts():
    accountList = bank.GetAccountsList()
    for account in accountList:
        print(account.GetAccountNumber())
        print(account.GetTransactions() )
Main()
