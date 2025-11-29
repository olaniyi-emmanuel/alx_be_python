class BankAccount: 


    def __init__(self, account_balance):
        #self.initial_balance = initial_balance 
        self.account_balance = account_balance 
    
    def deposit(self, deposit_amount): 
        self.account_balance += deposit_amount 

    def withdraw(self, withdraw_amount): 
        if self.account < withdraw_amount:
            self.account_balance -= withdraw_amount 
            return True
        else: 
            return False 
    def display_balance(self): 
        return print(f"The avaialable balance is: {self.account_balance } ")