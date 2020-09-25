class Account:
    def __init__(self,accountNumber):
        self._number = accountNumber
        self._transactions = {}

    def AddTransaction(self, date, amount):
        self._transactions[date]=amount
    
    def GetAccountNumber(self):
        return self._number
    
    def GetTransactions(self):
        return self._transactions

class Bank:
    def __init__(self):
        self._accounts = []

    def GetAccountsList(self):
        return self._accounts

    def AddAccount(self, account, accountNumber):
        print('add account')
        if not self._accounts:
            self._accounts.append(account)
        else:
            for account in self._accounts:
                print(account.GetAccountNumber())
                if account.GetAccountNumber() == accountNumber:
                    print('not added')
                    return False
                else: 
                    self._accounts.append(account)
                    print('added')
                    return True
    
    def AddTransaction(self, accountNumber,date, amount):
        for account in self._accounts:
            print(account.GetAccountNumber())
            if account.GetAccountNumber() == accountNumber:
                useraccount = account
                useraccount.AddTransaction(date, amount)


