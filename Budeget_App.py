class Category:
    def __init__(self,name):
        self.name = name
        self.ledger =[]
    def deposit(self, amount, description = ''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({
            'amount': -amount,
            'description': description
        })
            return True
        else:
            return False
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        total = 0
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"
            items += f'{desc:<23}{amt:>7}\n'
            total += item['amount']
        return title + items + f"Total: {total:.2f}"

def create_spend_chart(categories):

    spent = []
    total_spent = 0

    for category in categories:
        category_total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                category_total += -item['amount']
        spent.append(category_total)
        total_spent += category_total
    percentages = []
    for amount in spent:
        percent = int((amount / total_spent) * 100)
        percent = percent - (percent % 10)
        percentages.append(percent)
    #graph
    result = 'Percentage spent by category\n'
    for i in range(10,-1,-1):
        result += f'{i*10:>3}| '
        for percent in percentages:
            if percent >= i*10:
                result += 'o  '
            else:
                result += '   '
        result += '\n'
    #graph's bar
    result += '    ' + '-'*(len(categories)*3 + 1) + '\n'
    #category names
    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        result += '     '
        for category in categories:
            if i<len(category.name):
                result += category.name[i] + '  '
            else:
                result += '   '
        result += '\n'
    return result.rstrip('\n')