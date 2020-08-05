import datetime

import pytz





class Account:
    """ Simple account class with balance. Name starting with '_'  are generally non-public. """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print(f"Account created for {self.name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance.")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print(f"{amount:6} {tran_type} on {date} local time was {date.astimezone()}")


if __name__ == '__main__':
    # sanket = Account('Sanket', 0)
    #
    # sanket.show_balance()
    #
    # sanket.deposit(10000000)
    # sanket.withdraw(1000)
    # sanket.withdraw(1)
    # sanket.show_transactions()

    Jennifer = Account("Jennifer", 2343455)
    Jennifer.__balance = 134514551
    Jennifer.deposit(1234)
    Jennifer.withdraw(234345)
    Jennifer.show_transactions()
    Jennifer.show_balance()
    Jennifer.show_balance()

    print(Jennifer.__dict__)


print(Account.__doc__)
help(Account)