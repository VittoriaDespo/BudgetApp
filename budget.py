class Category:
  ledger = []
  category = ""
  withdraws = 0

  def __init__(self, category):
    self.category = category 
    self.ledger = list()

  def __str__(self):
    title = f'*************{self.category}*************\n'
    total = 0
    row = ''
    for item in self.ledger:
      row = row + f'{item["description"][:23]:23}{item["amount"]:7.2f}\n'
      total = total + item["amount"]

    display_menu = title + row + "Total: " + str(total)
    return display_menu
    
  def deposit (self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw (self,amount,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.withdraws += amount
      return True 
    else: return False
 
  def get_balance (self):
    balance = 0
    for item in self.ledger:
      balance = balance + item["amount"]
    return balance

  def transfer (self,amount,name):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + name.category)
      name.deposit(amount,"Transfer from " + self.category)
      self.withdraws += amount
      return True
    else:
      return False
   

  def check_funds (self,amount):
    if self.get_balance() >= amount:
      return True
    else:
      return False
      

def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    category = Category
    expenses = dict()
    total = 0
    percentage = []
    count = 0
    max_len = 0
    for category in categories:
        expenses[category.category] = category.withdraws
        total += category.withdraws
        count += 1

    for k, v in expenses.items():
        percentage.append(v / total * 100)
        if len(k) > max_len:
            max_len = len(k)

    for i in range(100, -1, -10):
        chart += f'{str(i).rjust(3)}|'
        for percent in percentage: 
            if percent > i:
                chart += ' o '  
            else:
                chart += ' ' * 3
        chart += " \n"
                    
    chart += '    ' + ('-' * (count * 3 + 1)) + '\n'
    for i in range(max_len):
        chart += ' ' * 4
        for k in expenses.keys():
            if i < len(k):
                chart += ' ' + k[i] + ' '
            else:
              chart += " " * 3  
        chart += " \n"     
    return chart.rstrip("\n") 
                    