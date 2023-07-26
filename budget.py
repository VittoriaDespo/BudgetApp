class Category:
  ledger = []
  category = ""

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
      return True
    else:
      return False
   

  def check_funds (self,amount):
    if self.get_balance() >= amount:
      return True
    else:
      return False
      
  
    
  

def create_spend_chart(categories):
  return None