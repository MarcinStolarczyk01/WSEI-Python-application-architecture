"""
Napisz klasę BankAccount, która implementuje podstawowe operacje na koncie
bankowym, takie jak wpłacanie, wypłacanie i sprawdzanie salda. Klasa powinna
wywoływać wyjątek przy próbie wpłaty lub wypłaty niepoprawnej kwoty.
Następnie napisz testy jednostkowe za pomocą unittest, które sprawdzą
poprawność działania metod oraz obsługę błędów.
"""


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        self._balance += amount

        return self._balance

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Not enough money!")

        self._balance -= amount
        return self._balance
