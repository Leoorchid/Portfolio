import datetime
import json
import os


print(f"[Personal Expense Tracker]")
fileName = "data.json"


class Transaction:

    def __init__(self, amount, category, description):

        self.amount = amount
        self.category = category
        self.date = datetime.datetime.now().strftime("%B %d, %Y")
        self.description = description

    def toDict(self):
        newDict = {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
        }
        return newDict

def dataToTransaction(data):
    tran = Transaction(
        data["amount"],
        data["category"],
        data["description"]
    )
    tran.date = data["date"]  
    return tran
    

class Account:
    def __init__(self, user, password, income):
        self.user = user
        self.password = password
        self.income = income
        self.spending = 0
        self.history = [] 

        try:
            with open(fileName, "r") as f:
                data = json.load(f)
                for d in data:
                    self.history.append(dataToTransaction(d))
        except FileNotFoundError:
            pass

    def addTransaction(self, amount, category, description):
        newTrans = Transaction(amount, category, description)
        self.history.append(newTrans)
        with open(fileName, "w") as f:
            json.dump([tran.toDict() for tran in self.history], f)

    def viewTrans(self):
        fil = input("Pick filter (1-category,2-date): ")

        match fil:
            case "1":
                cat = input("(Need,Want,Other): ")
                for trans in self.history:
                    if trans.category == cat:
                        print(
                            f"${trans.amount},{trans.category},{trans.description}"
                        )

            case "2":
                for i, trans in enumerate(self.history):
                    print(
                        f"${trans.amount},{trans.category},{trans.description},{trans.date}"
                    )


user = Account("Leo", 123, 1000)


while True:
    print("1. Add Expense\n2. View all expense")

    action = input(">")

    match action:
        case "1":
            amount = int(input("Amount: $"))
            category = input("(1-Need,2-Want,3-Other): ")
            description = input("Description: ")
            match category:
                case "1":
                    category = "Need"
                case "2":
                    category = "Want"
                case "3":
                    category = "Other"

            newTrans = user.addTransaction(amount, category, description)
        case "2":
            user.viewTrans()

        case "Q" | "q":
            pass
