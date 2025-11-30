class BankAccount: 


    def __init__(self, account_balance=0):
        #self.initial_balance = initial_balance 
        self.account_balance = account_balance 
    
    def deposit(self, deposit_amount): 
        self.account_balance += deposit_amount 

    def withdraw(self, withdraw_amount): 
        if self.account_balance > withdraw_amount:
            self.account_balance -= withdraw_amount 
            print(f"Withdrew: {withdraw_amount}")
            return True
        else: 
            print(f"Insufficient Funds")
            return False 
    def display_balance(self): 
        return print(f"Current Balance: {self.account_balance } ")