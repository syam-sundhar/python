class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def display(self):
        print(self.name,"balance is: ",self.balance)

syam=bankaccount('syam',20000)
syam.display()
print("--------------------")
syam.deposit(10000)
syam.display()
print("--------------------")
syam.withdraw(200)
syam.display()
print("--------------------")