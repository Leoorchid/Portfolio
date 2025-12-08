import datetime


print(f"[Personal Expense Tracker]")



class Transaction:
    
    def __init__(self,amount,category,description):
        
        self.amount = amount
        self.category = category
        self.date = datetime.datetime.now().strftime("%B %d, %Y")
        self.description = description

    def view(self):
        print(f"{self}")


class Account:
    def __init__(self,user,password,income):
        self.history = []
        self.user = user
        self.password = password
        self.spending = 0
        self.income = income


    def addTransaction(self,amount,category,description):
        newTrans = Transaction(amount,category,description)
        self.history.append(newTrans)
    
    def viewTrans(self):
        for trans in self.history:
            print(trans.view)


user = Account("Leo",123,1000)



while True:
    print("1. Add Expense\n2. View all expense")

    action = input(">")

    match action:
        case "1":
            amount = int(input("Amount: $"))
            category = (input("Need,Want,Other: "))
            description = (input("Description: "))
            newTrans = user.addTransaction(amount,category,description)
        case "2":
            user.viewTrans()



        case "Q"|"q":
            pass






