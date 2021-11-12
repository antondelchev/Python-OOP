class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        result = self.amount + sum(self._transactions)
        return result

    def validate_transaction(self, account, amount_to_add):
        if self.balance() < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance()}"

    def __gt__(self, other):
        return sum(self._transactions) > sum(other._transactions)

    def __ge__(self, other):
        return sum(self._transactions) >= sum(other._transactions)

    def __lt__(self, other):
        return sum(self._transactions) < sum(other._transactions)

    def __le__(self, other):
        return sum(self._transactions) <= sum(other._transactions)

    def __eq__(self, other):
        return sum(self._transactions) == sum(other._transactions)

    def __ne__(self, other):
        return not sum(self._transactions) == sum(other._transactions)

    def __add__(self, other):
        new_name = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        all_transactions = self._transactions + other._transactions
        new_acc = Account(new_name, new_amount)
        new_acc._transactions = all_transactions
        return new_acc

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        reversed_list = self._transactions[::-1]
        return reversed_list

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
