from classes import Bank 
from classes import Account
from datetime import datetime

def AddAccount():
    accountNumber = int(input('Kontonummer:'))
    account = Account(accountNumber)
    print(account.GetAccountNumber())
    

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