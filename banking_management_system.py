class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def showdetail(self):
        print("Personal Details:-")
        print(f"Name:- {self.name.title()}")
        print(f"Age:- {self.age}")
        print(f"Gender:- {self.gender.title()}")


class Bank(User):
    __usercount = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.__balance = 0
        Bank.__usercount += 1
        self.accountno = f"denabank0000{Bank.__usercount}"

    def user_count(self):
        return Bank.__usercount

    def deposite(self, amount):
        self.__balance += amount
        print(f"Account balance updated :- Rs {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insufficient balance, balance available :- Rs {self.__balance}")
        elif 100 <= amount <= self.__balance:
            self.__balance -= amount
            print("Thank you for visiting")
            print(f"Current balance is:- Rs {self.__balance}")
        else:
            print("You cannot withdraw less than Rs.100")

    def viewbalance(self):
        self.showdetail()
        print(f"Account No:- {self.accountno}")
        print(f"Current balance is:- Rs {self.__balance}")

    def transfer(self, other_account, amount):
        if amount > self.__balance:
            print(f"Insufficient balance, balance available :- Rs {self.__balance}")
        elif 1 < amount <= self.__balance:
            other_account.__balance += amount
            self.__balance -= amount
            print("Amount transferred successfully")
            print(f"Current balance is :- Rs {self.__balance}")
        else:
            print("You cannot transfer less than Rs.1")


if __name__ == "__main__":
    user1 = Bank("siddharth", 25, "male")
    user2 = Bank("rohan", 24, "male")

    user1.deposite(5000)
    user1.viewbalance()

    user1.withdraw(1500)
    user1.transfer(user2, 1000)

    print("\nSender:")
    user1.viewbalance()
    print("\nReceiver:")
    user2.viewbalance()

    print("\nTotal bank users:", user1.user_count())
