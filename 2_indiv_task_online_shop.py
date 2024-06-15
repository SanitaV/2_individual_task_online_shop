class Client:
  def __init__(self, client_id, name):
      self.client_id = client_id
      self.name = name
      self.transactions = []

  def add_transaction(self, transaction):
      self.transactions.append(transaction)

  def __str__(self):
      return f"Client [ID: {self.client_id}, Name: {self.name}]"


class Item:
  def __init__(self, item_id, name, price):
      self.item_id = item_id
      self.name = name
      self.price = price

  def __str__(self):
      return f"Item [ID: {self.item_id}, Name: {self.name}, Price: EUR {self.price}]"


class Transaction:
  def __init__(self, transaction_id, client, items):
      self.transaction_id = transaction_id
      self.client = client
      self.items = items

  def __str__(self):
      item_str = ", ".join(str(item) for item in self.items)
      return f"Transaction [ID: {self.transaction_id}, Items: {item_str}]"


clients = [
  Client(1, "Anna"),
  Client(2, "Tom")
]

items = [
  Item(1, "Bed", 1000.00),
  Item(2, "Table", 250.00),
  Item(3, "Rug", 120.00)
]

transactions = [
  Transaction(1, clients[0], [items[0], items[2]]),
  Transaction(2, clients[1], [items[1]]),
  Transaction(3, clients[0], [items[1], items[2]])
]

clients[0].add_transaction(transactions[0])
clients[0].add_transaction(transactions[2])
clients[1].add_transaction(transactions[1])

print("Clients:")
for client in clients:
  print(client)

print("\nTransactions by Client:")
for client in clients:
  print(f"\n{client.name}'s Transactions:")
  for transaction in client.transactions:
      print(transaction)
print("\nItems in Each Transaction by Client:")
for client in clients:
  print(f"\n{client.name}'s Transactions:")
  for transaction in client.transactions:
      print(f"Transaction ID: {transaction.transaction_id}")
      for item in transaction.items:
          print(f"  {item}")
